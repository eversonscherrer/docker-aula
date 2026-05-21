from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"><title>Docker na Pratica</title>
        <style>
          body { font-family: Arial, sans-serif; background: #0d1b2a; color: #fff;
                 display: flex; justify-content: center; align-items: center;
                 height: 100vh; margin: 0; flex-direction: column; }
          h1   { color: #00b4d8; font-size: 3rem; }
          p    { font-size: 1.2rem; color: #adb5bd; }
          .box { background: #1b2a3b; padding: 2rem 3rem; border-radius: 12px;
                 border-left: 4px solid #00b4d8; text-align: center; }
        </style>
        </head>
        <body>
          <div class="box">
            <h1>Ola do Docker!</h1>
            <p>Se voce esta vendo isso, seu container esta rodando.</p>
            <p><strong>Imagem</strong> = caixa congelada &nbsp;|&nbsp;
               <strong>Container</strong> = pizza no forno</p>
          </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        print(f"[servidor] {self.address_string()} - {format % args}")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Servidor rodando na porta 8080...")
    server.serve_forever()
