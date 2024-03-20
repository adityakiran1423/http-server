import socket


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    (connection, address) = server_socket.accept()
    data = connection.recv(1024).decode(encoding="utf-8").splitlines()

    # index=data.index("/")
    # for i in range(index,len(data)):
    #     if i==" ":
    #         break
    # http_path=data[index:i]

    path = data[0].split(" ") 

    start_line=data[0] #extracting start line
    temp=start_line.split(" ")
    content=temp[1]
    content_length=len(content)
    content=content[5:len(content_length)] # removing echo from the content

    if path[1] == "/":
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")
    elif path[1]!="/":
        connection.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: '{}'.format(content_length, encoding='utf-8')\r\n \n {}.format(content, encoding='utf-8')\r\n\r\n")
    else:
        connection.send(b"HTTP/1.1 404 Not Found\r\n\r\n")

    connection.send(b"HTTP/1.1 200 OK\r\n\r\n")


if __name__ == "__main__":
    main()
