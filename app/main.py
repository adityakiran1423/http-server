import socket
import threading
import os
import sys


def server(connection)->None:

    data = connection.recv(1024).decode(encoding="utf-8")
    post_data=data
    data=data.splitlines()
    path = data[0].split(" ")  
    post=path[0]
    http_path = path[1]

    content = http_path[6:]
    content_length = len(content)


    user_agent_parts = data[2].split(" ")
    if len(user_agent_parts) < 2:
        user_agent = ""
    else:
        _, user_agent = user_agent_parts

    if http_path == "/":
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")

    elif http_path.startswith("/echo/"):
        data_to_send = (
            "HTTP/1.1 200 OK"+ "\n"
            + "Content-Type: text/plain"+ "\n"
            + "Content-Length: " + str(content_length)+ "\n\n"
            # + "\n"
            + content+ "\r\n"
        )
        connection.sendall(data_to_send.encode())

    elif http_path == "/user-agent":
        data_to_send = (
            "HTTP/1.1 200 OK"+ "\n"
            + "Content-Type: text/plain"+ "\n"
            + "Content-Length: " + str(len(user_agent))+ "\n\n"
            # + "\n"
            + user_agent + "\r\n"
        )
        connection.sendall(data_to_send.encode())

    elif http_path.startswith("/files/") and post!="POST":
        directory = ""
        if sys.argv[1] == "--directory":
            directory = sys.argv[2]
        filename = http_path[len("/files/") :]
        file_path = os.path.join(directory, filename)
        response = "HTTP/1.1 404 Not Found \r\n\r\n"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                fileContent = file.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(fileContent)}\r\n\r\n{fileContent}\r\n"
        print(response)

        connection.send(response.encode())
    
    elif post=="POST":
        file_content = post_data.split("\r\n\r\n")[-1]
        directory = ""
        if sys.argv[1] == "--directory":
            directory = sys.argv[2]
        filename = http_path[len("/files/") :]
        file_path = os.path.join(directory, filename)
        with open(file_path, "w") as file:
            file.write(file_content)

        response = "HTTP/1.1 201 Created \r\n\r\n"

        connection.send(response.encode())

    else:
        connection.send(b"HTTP/1.1 404 Not Found\r\n\r\n")

    connection.close()

def main() -> None:

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True) # creating intial server socket

    while True:
        (connection, address) = server_socket.accept()
        thread = threading.Thread(target=server, args=(connection,))
        thread.start()


if __name__ == "__main__":
    main()
