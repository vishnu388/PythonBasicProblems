"""
Author - vishnu.
Date - 05/05/2021
Title - Chat Application using socket programming(One server and multiple clients).
"""


import socket
import threading  #To handle multiple clients
IP = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 1233      # Port to listen on (non-privileged ports are > 1023)
ADDRESS = (IP, PORT)
SIZE = 1024      #BufferSize
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")
    connected = True
    while connected:
        msg = connection.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            print(f"[{address}] {msg}")
            msg = f"MSG received: {msg}"
            connection.send(msg.encode(FORMAT))
    connection.close()

def main():
    print("[STARTING] server is starting..")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")


if __name__ == "__main__":
    main()