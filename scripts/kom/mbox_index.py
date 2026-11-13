"""Stream a Gmail mbox from stdin and write one JSON line per message.

Keeps headers, attachment names and a capped plain-text body.
Spam and Trash keep headers only. Attachment content is never stored.
"""
import email
import email.policy
import html
import json
import re
import sys

BODY_CAP = 6000
out = open(sys.argv[1], "w", encoding="utf-8")


def text_of(msg):
    plain, htm, atts = [], [], []
    for part in msg.walk():
        if part.is_multipart():
            continue
        fn = part.get_filename()
        disp = (part.get("Content-Disposition") or "").lower()
        if fn or "attachment" in disp:
            try:
                size = len(part.get_payload(decode=False) or "") * 3 // 4
            except Exception:
                size = 0
            atts.append({"name": str(fn or ""), "type": part.get_content_type(), "approx_bytes": size})
            continue
        ct = part.get_content_type()
        if ct not in ("text/plain", "text/html"):
            continue
        try:
            payload = part.get_payload(decode=True) or b""
            cs = part.get_content_charset() or "utf-8"
            txt = payload.decode(cs, errors="replace")
        except Exception:
            continue
        (plain if ct == "text/plain" else htm).append(txt)
    body = "\n".join(plain)
    if not body.strip() and htm:
        body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", "\n".join(htm), flags=re.S | re.I)
        body = html.unescape(re.sub(r"<[^>]+>", " ", body))
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\n\s*\n+", "\n\n", body).strip()
    return body[:BODY_CAP], atts


def h(msg, name):
    try:
        v = msg.get(name)
        return str(v) if v is not None else ""
    except Exception:
        return ""


def flush(idx, raw):
    try:
        msg = email.message_from_bytes(raw, policy=email.policy.default)
    except Exception as e:
        out.write(json.dumps({"i": idx, "error": str(e)}) + "\n")
        return
    labels = h(msg, "X-Gmail-Labels")
    rec = {
        "i": idx,
        "date": h(msg, "Date"),
        "from": h(msg, "From"),
        "to": h(msg, "To"),
        "cc": h(msg, "Cc"),
        "subject": h(msg, "Subject"),
        "labels": labels,
        "thread": h(msg, "X-GM-THRID"),
        "msgid": h(msg, "Message-ID"),
        "bytes": len(raw),
    }
    skip_body = bool(re.search(r"\b(Spam|Trash)\b", labels))
    try:
        body, atts = text_of(msg)
    except Exception:
        body, atts = "", []
    rec["attachments"] = atts
    rec["body"] = "" if skip_body else body
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")


idx, buf = 0, []
for line in sys.stdin.buffer:
    if line.startswith(b"From ") and buf:
        flush(idx, b"".join(buf))
        idx += 1
        buf = []
        if idx % 5000 == 0:
            print(idx, file=sys.stderr, flush=True)
    if line.startswith(b"From ") and not buf:
        buf = [b""]  # drop the mbox separator line
        continue
    buf.append(line)
if buf:
    flush(idx, b"".join(buf))
    idx += 1
print("done", idx, file=sys.stderr, flush=True)
out.close()
