import socket
import select
import threading
def pseudo (dictClient, conn):
        data = "what's your name ?"
        conn.send(data.encode())
        pseudo = conn.recv(1024).decode()
        while pseudo in dictClient:
                data = "name alredy taken, please chose an other"
                conn.send(data.encode())
                pseudo = conn.recv(1024).decode()
        dictClient[pseudo] = conn
        return (dictClient,pseudo)

def Main():
#init
    host = "127.0.0.1"
    port = 1459
    mySocket = socket.socket()
    mySocket.bind((host,port))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
#données
    dictClient = {}

    # demande la pseudo avant toute autre action!
    dictClient, name = pseudo(dictClient, conn)
    conn.send("done".encode())
    print("name saved")

    while True:
            # recoie les données
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected " + name + ":" + str(data))

            #repond au donénes
            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()