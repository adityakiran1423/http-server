# http-server

An asynchronous http server implemented in Python. 

# Features
 - It can respond with a 200.
 - It can respond with a 404.
 - It can respond with content.
 - It can handle concurrent connections.
 - It can GET a file.
 - It can handle POST requests and write to a file.

 # Concurrency 
 In order to be able to handle multiple concurrent connections, threading has been implemented
 Whenever a new request is sent to the http-server, it creates a new thread which handles the user request independently 

# To run the server
use `python -m app.main` or `./your_server.sh`