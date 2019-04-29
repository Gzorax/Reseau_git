import socket
import select
import threading



def Main():
    host = '127.0.0.1'
    port = 1459

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    soc.connect((host, port))

    message = input(" -> ")

    while message != 'q':  # \BYE':
        soc.send(.encode())
        # recoi le text envoyer par le server
        data = soc.recv(1024).decode()
        print(data)

        message = input(" -> ")

    soc.close()


if __name__ == '__main__':
    Main()
