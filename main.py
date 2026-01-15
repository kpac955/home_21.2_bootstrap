from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote_plus


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обработка GET-запроса"""
        try:
            with open("contacts.html", "r", encoding="utf-8") as f:
                html_content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(html_content, "utf-8"))
        except FileNotFoundError:
            self.send_error(404, "Файл contacts.html не найден")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Декодируем URL-символы в нормальный текст
        decoded_data = unquote_plus(post_data)

        print("\n=== ПОЛУЧЕНЫ ДАННЫЕ ИЗ ФОРМЫ ===")
        print(decoded_data)
        print("===============================\n")

        self.do_GET()


if __name__ == "__main__":
    web_server = HTTPServer(("localhost", 8080), MyServer)
    print("Сервер запущен: http://localhost:8080")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        web_server.server_close()
        print("\nСервер остановлен.")