import socket
import time
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket=socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #AF-INET6 FOR IP V6 AND SOCK_STREAM FOR TCP , WE CAN USE DGRAM FOR UDP(STREAMING)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind((SERVER_HOST,SERVER_PORT))  #port 0-1023 reserved for os system use, for http req port 80, for https req port 443, port range 0-65535, 0.0.0.0 for accessing from any device, 127.0.0.1 for computer only.
server_socket.listen(6)  #creates a req queue of size 6
print(f"listening on port {SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    request=client_socket.recv(1500).decode() #to request something from the server, recv function returns byte so we decode it into string
    print(request)
    header = request.split('\n')         #split the req at new line to fetch all the headers
    print(header[0])
    first_header_components = header[0].split()
    http_method = first_header_components[0]
    path = first_header_components[1]
    if path == '/' :    #they are comming at homepage
        file_input = open('index.html')
        content = file_input.read()
        file_input.close()

        #http respose fomate
        #STATUS LINE -- MANDATORY
        #HEADERS
        #MESSAGE-BODY
        response = 'HTTP/1.1 200 OK\n\n' + content   #200 is status code for ok
        client_socket.sendall(response.encode())
        client_socket.close()
        
    


