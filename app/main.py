import socket


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    (connection, address) = server_socket.accept()
    data = connection.recv(1024).decode(encoding="utf-8").splitlines()

    path = data[0].split(" ") 

    start_line=data[0] #extracting start line
    temp=start_line.split(" ")
    content=temp[1]
    content_length=len(content)
    content=content[5:content_length] # removing echo from the content

    if path[1] == "/":
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")

    elif path[1].startswith("/echo/"):
        data_to_send="HTTP/1.1 200 OK"+"Content-Type: text/plain"+"Content-Length: "+str(content_length)+content
        connection.sendall(data_to_send.encode())
        #connection.send(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {content_length}\r\n \n {content}\r\n\r\n")
    else:
        connection.send(b"HTTP/1.1 404 Not Found\r\n\r\n")


if __name__ == "__main__":
    main()
