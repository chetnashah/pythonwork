import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostbyname('localhost')
print("host = ", host)
port = 9999

serversocket.bind((host, port))

serversocket.listen(5)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    print("got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()

