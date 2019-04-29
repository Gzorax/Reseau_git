import socket
import select
import threading

def Main():
#init
    host = "127.0.0.1"
    port = 1459
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    mySocket.bind((host,port))
    mySocket.listen(1)

    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    while True:
        #repond au donénes
        data = str(data).upper()
        print ("sending: " + str(data))
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    Main()
