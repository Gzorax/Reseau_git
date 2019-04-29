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

def LIST (dictChannel):
        data = "\n\n   List of availble channels:\n"
        for channel in dictChannel:
                data = data + channel + "\n"
        return data 

def JOIN(dictChannel, name, conn):
        if name in dictChannel:
                dictChannel[name] = dictChannel[name].append(conn)
        else:
                dictChannel[name] = [conn]
        return dictChannel

def Main():
#init
    host = "127.0.0.1"
    port = 1459
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    mySocket.bind((host,port))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
#données
    dictClient = {}
    dictChannel = {}

#initialisation des données pour test a un seul client
    dictChannel["kiwitopia"] = 1
    dictChannel["licornTime"] = 2

    # demande la pseudo avant toute autre action!
    dictClient, name = pseudo(dictClient, conn)
    conn.send("done".encode())
    print("name saved : " + name)

    while True:
            # recoie les données
            data = conn.recv(1024).decode()
            print ("reveved data : " + data)
            if not data:
                    break
            print ("from connected " + name + ":" + str(data))
            if data == 'LIST':
                    print ("comande enter : LIST")
                    reponce = LIST(dictChannel)
                    print ("sending : " + reponce)
                    conn.send(reponce.encode())
                    break
        
            if data == 'JOIN':
                    print("commande enter : JOIN")
                    chanel = conn.recv(1024).decode()
                    print("chanel receved : "+ chanel)
                    dictChannel = JOIN(dictChannel,chanel,conn)
                    reponce = "Your now connected to : " + chanel
                    print ("sending : " + reponce)
                    conn.send(reponce.encode())
                    break
            
            #repond au donénes
            # str(data).upper()
            data = "erreur"
            #print ("sending: " + str(data))
            conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    Main()
