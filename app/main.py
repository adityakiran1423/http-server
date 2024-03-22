import socket
import threading


def server(data, connection)->None:
    path = data[0].split(" ")  # list containing start line contents
    http_path = path[1]

    content = http_path[6:]
    content_length = len(content)

    _, user_agent = data[2].split(" ")
    length_user_agent = len(user_agent)

    if http_path == "/":
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")

    elif http_path.startswith("/echo/"):
        data_to_send = (
            "HTTP/1.1 200 OK"+ "\n"
            + "Content-Type: text/plain"+ "\n"
            + "Content-Length: " + str(content_length)+ "\n\n"
            # + "\n"
            + content+ "\n"
        )
        connection.sendall(data_to_send.encode())

    elif http_path == "/user-agent":
        data_to_send = (
            "HTTP/1.1 200 OK"+ "\n"
            + "Content-Type: text/plain"+ "\n"
            + "Content-Length: " + str(length_user_agent)+ "\n\n"
            # + "\n"
            + user_agent + "\n"
        )
        connection.sendall(data_to_send.encode())

    # connection.send(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {content_length}\r\n \n {content}\r\n\r\n")

    else:
        connection.send(b"HTTP/1.1 404 Not Found\r\n\r\n")


def main() -> None:

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True) # creating intial server socket

    while True:
        (connection, address) = server_socket.accept()
        data = connection.recv(1024).decode(encoding="utf-8").splitlines()

        thread = threading.Thread(target=server, args=(data, connection))
        thread.start()


if __name__ == "__main__":
    main()
