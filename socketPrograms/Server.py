import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 64323       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connect, address = s.accept()
    print('Connected by', address)
    while True:
        sendData=input('Server: ')
        connect.send(bytes(sendData,'utf-8'))
        recvData=connect.recv(1024).decode()
        print('client: ',recvData)
connect.close()