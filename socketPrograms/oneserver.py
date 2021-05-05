"""
Author - vishnu.
Date - 05/05/2021
Title - Chat Application using socket programming(One server and multiple clients).
"""
import socket
from _thread import *
class server:
    def connection(self):
        ServerSocket = socket.socket()
        host = '127.0.0.1'
        port = 1233
        ThreadCount = 0
        try:
            ServerSocket.bind((host, port))
        except socket.error as e:
            print(str(e))

        print('Waiting for a Connection..')
        ServerSocket.listen(5)


        def threaded_client(connection):
            connection.send(str.encode('Welcome to the Server'))
            while True:
                data = connection.recv(2048)
                reply = 'Server Says: ' + data.decode('utf-8')
                if not data:
                    break
                connection.sendall(str.encode(reply))
            connection.close()

        while True:
            Client, address = ServerSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(threaded_client, (Client, ))
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount))
        ServerSocket.close()
connect = server()
connect.connection()
