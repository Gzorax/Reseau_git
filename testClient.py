import socket
import select
import threading
 
def Main():
        host = '127.0.0.1'
        port = 1459
         
        soc = socket.socket()
        soc.connect((host,port))

        #soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        #soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #soc.bind(('', 1459))
        #soc.listen(10)
        #soc.connect((?,port))
         
        message = input(" -> ")
         
        while message != 'q':
                #envoie la demande de texte
                soc.send(message.encode())
                #recoi le text envoyer par le server
                data = soc.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                #message = input(" -> ")
                 
        soc.close()
 
if __name__ == '__main__':
    Main()      