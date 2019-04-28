import socket
import select
import threading


def Server():
    # init
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('', 1459))
    serversocket.listen(10)

while True :