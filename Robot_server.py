import socket

serversocket = socket.socket()

host = 'localhost'
port = 6666

serversocket.bind(('', port))

serversocket.listen(1)

clientsocket, addr = serversocket.accept()
print("got a connection from %s" % str(addr))

while True:
    msg = input("> ") + "\r\n"
    clientsocket.send(msg.encode('ascii'))
