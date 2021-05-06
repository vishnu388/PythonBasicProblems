"""
Author - vishnu.
Date - 05/05/2021
Title - Chat Application using socket programming(One server and multiple clients).
"""
from decouple import config
import socket
IP = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1233       # Port to listen on (non-privileged ports are > 1023)
ADDRESS = (IP, PORT)
SIZE = 1024       #BufferSize
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    connected = True
    while connected:
        msg = input(">")
        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

if __name__ =="__main__":
    main()