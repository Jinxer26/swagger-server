from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import json

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/spec":
            specs = [
                f for f in os.listdir(".")
                if f.endswith((".yaml", ".yml", ".json"))
            ]
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(specs).encode())
        else:
            super().do_GET()

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

