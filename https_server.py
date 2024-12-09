import http.server
import ssl

# Настройки сервера
server_address = ('0.0.0.0', 8000)  # Привязка ко всем IP-адресам
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Настройка SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="localhost.pem", keyfile="localhost-key.pem")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving on https://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
