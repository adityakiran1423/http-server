import socket


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    (clientsocket, address) = server_socket.accept()
    clientsocket.send(b"HTTP/1.1 200 OK\r\n\r\n")


if __name__ == "__main__":
    main()
