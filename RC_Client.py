import socket


class MySocket:

    def __init__(self):
        self.sock = socket.socket()

    def open_connection(self, host="localhost", port=6666):
        self.sock.connect((host, port))

    def get_data(self):
        return self.sock.recv(1024)
