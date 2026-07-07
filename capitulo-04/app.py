import http.server
import os
import socketserver

PORTA = 8080
ARQUIVO = "/data/contador.txt"


def ler_contador():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO) as f:
            return int(f.read().strip() or 0)
    return 0


def salvar_contador(valor):
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    with open(ARQUIVO, "w") as f:
        f.write(str(valor))


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        contador = ler_contador() + 1
        salvar_contador(contador)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background:#0d1b2a;
                     color:#fff; text-align:center; padding-top:4rem;">
          <h1 style="color:#00b4d8;">Contador de visitas</h1>
          <p style="font-size:4rem; margin:1rem;">{contador}</p>
          <p style="color:#adb5bd;">Dado salvo em: <code>{ARQUIVO}</code></p>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        print(f"Visita registrada -> contador atual: {ler_contador()}")


with socketserver.TCPServer(("", PORTA), Handler) as httpd:
    print(f"Servindo na porta {PORTA}")
    httpd.serve_forever()
