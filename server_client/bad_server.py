import socket

# domain:port - socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    True
)
server_socket.bind(("localhost", 8000))
server_socket.listen()

while True:
    print("Before accept()")
    client_socket, addr = server_socket.accept()
    print(f"Connected from: {addr}")
    
    while True:
        print("Before recv")
        request = client_socket.recv(4096) # 4 kb
        print("After recv")
        
        print("request is: ", request)
        
        if not request:
            break
        else:
            response = "Hello From Server\n".encode() # to bytes
            print()
            print("Before response")
            client_socket.send(response)
            print("response is: ", response)
            print("After response")
    
    print("Outside inner while loop")
    client_socket.close()
    
# python server.py
# nc localhost 8080