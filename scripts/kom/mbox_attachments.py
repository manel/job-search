"""Stream a Gmail mbox from stdin and save attachments whose file name matches.

Usage: mbox_attachments.py out_dir name [name ...]
Saves each match as <date>_<msg index>_<name>. Prints one line per saved file.
"""
import email
import email.policy
import email.utils
import os
import sys

out_dir = sys.argv[1]
wanted = set(sys.argv[2:])


def scan(idx, raw):
    if not any(w.encode() in raw for w in wanted) and b"=?" not in raw:
        return
    msg = email.message_from_bytes(raw, policy=email.policy.default)
    for part in msg.walk():
        fn = part.get_filename()
        if fn not in wanted:
            continue
        try:
            dt = email.utils.parsedate_to_datetime(str(msg["Date"])).strftime("%Y-%m-%d")
        except Exception:
            dt = "unknown"
        path = os.path.join(out_dir, f"{dt}_{idx}_{fn}")
        with open(path, "wb") as f:
            f.write(part.get_payload(decode=True) or b"")
        print(path, "| from", msg["From"], "| labels", msg["X-Gmail-Labels"], flush=True)


idx, buf = 0, []
for line in sys.stdin.buffer:
    if line.startswith(b"From ") and buf:
        scan(idx, b"".join(buf))
        idx += 1
        buf = []
    if line.startswith(b"From ") and not buf:
        buf = [b""]
        continue
    buf.append(line)
if buf:
    scan(idx, b"".join(buf))
print("done", idx + 1, file=sys.stderr)
