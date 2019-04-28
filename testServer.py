import socket
import select
import threading
 
def Main_server():
    

        port = 1459

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.bind(('', 1459))


    mySocket = socket.socket()
    mySocket.bind(('',port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    #print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            #data = str(data).upper()
            #print ("sending: " + str(data))
            #conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()