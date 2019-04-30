import socket
import select
import threading
import string
import time


def ReadCode(text, i):
    commande = ''
    while text[i] != ' ':
        commande = commande + text[i]
        print("lettre " + str(i) + " " + text[i])
        i += 1
        if i >= len(text):
            return (commande, i)
    return (commande, i)


def Main():
    host = '127.0.0.1'
    port = 1459
    RECV_BUFFER = 4096

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    #soc.settimeout(2)

# connect to remote host
    connected = False
    while not connected:
        try:
            soc.connect((host, port))
            connected = True
        except:
            print('Unable to connect')

    bye = "bye"
    documentation = "\n   Documentation :\n/HELP: print this message\n/LIST: list all available channels on server\n/JOIN <channel>: join (or create) a channel\n/LEAVE: leave current channel\n/WHO: list users in current channel\n<message>: send a message in current channel\n/MSG <nick> <message>: send a private message in current channel\n/BYE: disconnect from server\n/KICK <nick>: kick user from current channel [admin]\n/REN <channel>: change the current channel name [admin]\n"


# sauvegarde le nom utilisateur
    data = ''
    while data != 'done':
        # recoi le text envoyé par le server
        print ('connected to server')
        data = soc.recv(RECV_BUFFER).decode()
        if data == 'done':
            print("Server: name saved")
            break
        print('Server: ' + data)
        message = input(" -> ")
        soc.send(message.encode())

    print(documentation)
    message = input(" -> ")

# gestion commandes
    while message != 'q':  # \BYE':
        
        
        if message == '/HELP':
            print(documentation)
        elif message[0] == '/':
            #code = ''
            # for i in range (1,len(message)):
                 #       code  = code + message[i]
            #print ("sendition to server " + message)
            soc.send(message.encode())
            reponse = soc.recv(RECV_BUFFER).decode()
            print('Server: ' + reponse)

        elif message[0]:
            
            code = 'chanellMSG ' + message
            #print ("sendition to server " + code)
            soc.send(code.encode())
            reponse = soc.recv(RECV_BUFFER).decode()
            print(reponse)
            # print(message)

        else:
                print ("lecture")
                reponse = soc.recv(RECV_BUFFER).decode()
                print(reponse)

        message = input(" -> ")

    soc.send(bye.encode())
    print("disconnected from the server")
    soc.close()


if __name__ == '__main__':
    Main()
