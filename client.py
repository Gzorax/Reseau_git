import socket
import select
import threading

def Main():
    host = ''
    port = 1459
         
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    soc.connect((host,port))

    message = input(" -> ")
    while message != 'q':
        data = soc.recv(1024).decode()
        print ('Received from server: ' + data)
        message = input(" -> ")


        
 
if __name__ == '__main__':
    Main()      