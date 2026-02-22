import socket


HOST = "127.0.0.1"
PORT = 8080


def handle_client(connection):
    request = connection.recv(1024).decode()
    print("----- Incoming Request -----")
    print(request)

    if not request:
        connection.close()
        return

    # Parse first line of HTTP request
    request_line = request.split("\r\n")[0]
    method, path, version = request_line.split()

    if method == "GET":
        if path == "/":
            body = "<h1>Welcome to My Custom HTTP Server</h1>"
            status = "HTTP/1.1 200 OK"
        elif path == "/about":
            body = "<h1>About Page</h1><p>This is built from scratch.</p>"
            status = "HTTP/1.1 200 OK"
        else:
            body = "<h1>404 Not Found</h1>"
            status = "HTTP/1.1 404 Not Found"
    else:
        body = "<h1>405 Method Not Allowed</h1>"
        status = "HTTP/1.1 405 Method Not Allowed"

    response = (
        f"{status}\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{body}"
    )

    connection.send(response.encode())
    connection.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[+] HTTP Server running on http://{HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"[+] Connection from {addr}")
        handle_client(conn)


if __name__ == "__main__":
    start_server()