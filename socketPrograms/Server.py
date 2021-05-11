"""
Author - vishnu.
Date - 04/05/2021
Title - Socket programming simple program (Connection and print hello message).
"""

import socket
import logging
from decouple import config
from socketlogger import logger
logger.setLevel(logging.INFO)

class server:
    def connection(self):
        HOST = config('HOST')  # Standard loopback interface address (localhost)
        PORT = config('PORT')     # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    
            s.bind((HOST, PORT))
            s.listen()
            connect, address = s.accept()
        print('Connected by', address)
        try:
            while True:
                sendData=input('Server: ')
                connect.send(bytes(sendData,'utf-8'))
                recvData=connect.recv(1024).decode()
                print('client: ',recvData)
            connect.close()
        except Exception as e:
            print(e)
connect=server()
connect.connection()