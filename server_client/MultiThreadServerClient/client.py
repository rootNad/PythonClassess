import socket


IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 4096
DISCONNECT_MSG = "!DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    
    connected = True
    while connected:
        msg = input(" -> ")
        
        client.send(msg.encode(FORMAT))
        
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

if __name__ == "__main__":
    main()
    
    
