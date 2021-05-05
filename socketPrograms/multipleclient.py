"""
Author - vishnu.
Date - 05/05/2021
Title - Chat Application using socket programming(One server and multiple clients).
"""

import socket
class client:
    def connection(self):
        ClientSocket = socket.socket()
        host = '127.0.0.1'
        port = 1233
        print('Waiting for connection')
        try:
            ClientSocket.connect((host, port))
        except socket.error as e:
            print(str(e))

        Response = ClientSocket.recv(1024)
        while True:
            Input = input('Say Something: ')
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
            print(Response.decode('utf-8'))

        ClientSocket.close()
connect=client()
connect.connection()