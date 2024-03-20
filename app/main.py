import socket

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    (connection, address) = server_socket.accept()
    # connection.send(b"HTTP/1.1 200 OK\r\n\r\n")
    data = socket.recv(1024).decode(encoding='utf-8').splitlines()
    # index=data.index("/")
    # for i in range(index,len(data)):
    #     if i==" ":
    #         break
    # http_path=data[index:i]
    path=data[0].split(" ")
    if path[1]=="/":
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")
    else:
        connection.send(b"HTTP/1.1 404 Not Found\r\n\r\n")



if __name__ == "__main__":
    main()
