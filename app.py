from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = json.dumps({
                "message": "Backend Innovatech operativo",
                "status": "ok",
                "version": "1.0"
            })
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"[Innovatech Backend] {format % args}")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 3000), Handler)
    print("Backend corriendo en puerto 3000...")
    server.serve_forever()