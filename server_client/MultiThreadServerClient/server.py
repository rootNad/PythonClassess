import socket
import threading


IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 4096
DISCONNECT_MSG = "!DISCONNECT"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            msg = conn.recv(SIZE).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] {msg}")

            msg = "AAAAAAAAAAAA"
            conn.send(msg.encode(FORMAT))
        except Exception as e:
            print(e)
    conn.close()


def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        True
    )
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    main()


"""
    Add functional to server.
    Use wikipedia package(pip install wikipedia)
    User send to server an article name and sentence 
    count from article begining.
    
    Server respond with first N-sentences of article.
    
    Client must safe reveived sentensec in file
    File name example ArticleNameN.txt where N is sentece amount.
    
    Use that code to get articles from wikipedia
    In terminal:
        1. pip install wikipedia(in terminal)
    In code:
        1. import wikipedia
        2. article = wikipedia.summary(<ArticleName>, sentences=<NumOfSentences>)
        
    OpenWeather

"""