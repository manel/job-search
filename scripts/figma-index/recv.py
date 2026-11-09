import http.server, os, sys, urllib.parse
ROOT = sys.argv[2]
class H(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()
    def do_POST(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        rel = q.get('p', ['x.bin'])[0].replace('..', '')
        dest = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(dest), exist_ok=True)
        n = int(self.headers.get('Content-Length', 0))
        with open(dest, 'wb') as f: f.write(self.rfile.read(n))
        self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(b'ok')
    def log_message(self, *a): pass
import socket, threading
class S6(http.server.ThreadingHTTPServer): address_family = socket.AF_INET6
p=int(sys.argv[1])
threading.Thread(target=S6(('::1',p),H).serve_forever,daemon=True).start()
http.server.ThreadingHTTPServer(('127.0.0.1', p), H).serve_forever()
