import socket


class MySocket:

    def __init__(self, host="localhost", port=6666):
        self.sock = socket.socket()
        self.host = host
        self.port = port

    def open_connection(self):
        try:
            self.sock.connect((self.host, self.port))
            return True
        except socket.error as msg:
            print("Could not connect with the socket-server: %s\n terminating program" % msg)
            return False

    def get_data(self):
        return self.sock.recv(1024)

    def close_connection(self):
        self.sock.close()

    def send_data(self, message=""):
        print('sending "%s"' % message)
        self.sock.sendto(message.encode(), (self.host, self.port))
