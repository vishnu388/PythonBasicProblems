import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 64323  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        recvData = s.recv(1024).decode()
        print('server: ', recvData)
        sendData = input('Client: ')
        s.send(bytes(sendData,'utf-8'))
        print('Data Sent')
s.close()