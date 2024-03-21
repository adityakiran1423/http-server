import socket


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    (connection, address) = server_socket.accept()
    data = connection.recv(1024).decode(encoding="utf-8").splitlines()

    path = data[0].split(" ") # list containing start line contents
    http_path=path[1]

    content=http_path[6:]
    content_length=len(content)

    if http_path== "/":
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")

    elif http_path.startswith("/echo/"):
        data_to_send="HTTP/1.1 200 OK"+"Content-Type: text/plain"+"Content-Length: "+str(content_length)+"\n"+content
        connection.sendall(data_to_send.encode())
        #connection.send(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {content_length}\r\n \n {content}\r\n\r\n")

    else:
        connection.send(b"HTTP/1.1 404 Not Found\r\n\r\n")


if __name__ == "__main__":
    main()