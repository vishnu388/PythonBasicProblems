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

class client:
    def connection(self):
        HOST = config('HOST')  # The server's hostname or IP address
        PORT = config('PORT')  # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            try:
                while True:
                    recvData = s.recv(1024).decode()
                    print('server: ', recvData)
                    sendData = input('Client: ')
                    s.send(bytes(sendData,'utf-8'))
                    print('Data Sent')
                s.close()
            except Exception as e:
                print(e)
connect=client()
connect.connection()