import socket
import select
import threading


def auxReadInput(text, i):
        commande = ''
        if not i < len(text):
                condition = False
        else: 
                condition = text[i] != ' '
        #condition = (i < len(text)) & (text[i] != ' ' )
        while condition:
                commande = commande + text[i]
                print("lettre " + str(i) +" "+ text[i])
                i += 1

                if not i < len(text):
                        condition = False
                else: 
                        condition = text[i] != ' '
                
                #condition = (i < len(text)) & (text[i] != ' ' )
        return (commande , i)

def ReadInput (text,soc):
        data = ''
        if text[0] != '/':
                print("la commande entrée est un message")
                return (1,text)      
        else: 
                print("la commande entrée est une instruction")
                i = 1
                while i < len(text):
                        commande ,y = auxReadInput(text,i)
                        print ("instruction : " + commande)
                        soc.send(commande.encode())
                        i = y + 1
                return(2,data)
                
                

def Main():
    host = '127.0.0.1'
    port = 1459

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    soc.connect((host, port))

    documentation = "\n   Documentation :\n/HELP: print this message\n/LIST: list all available channels on server\n/JOIN <channel>: join (or create) a channel\n/LEAVE: leave current channel\n/WHO: list users in current channel\n<message>: send a message in current channel\n/MSG <nick> <message>: send a private message in current channel\n/BYE: disconnect from server\n/KICK <nick>: kick user from current channel [admin]\n/REN <channel>: change the current channel name [admin]\n"

    data = ''
    while data != 'done':
        # recoi le text envoyé par le server
        data = soc.recv(1024).decode()
        if data == 'done':
            print("Received from server: name saved")
            break
        print('Received from server: ' + data)
        message = input(" -> ")
        soc.send(message.encode())

    print(documentation)
    message = input(" -> ")

    while message != 'q':  # \BYE':
        if message == '/HELP':
            print(documentation)
        elif message[0] == '/':
                #code = ''
                #for i in range (1,len(message)):
                 #       code  = code + message[i]
                soc.send(message.encode())
                reponce = soc.recv(1024).decode()
                print('Received from server: ' + reponce)
                
        else:
                print(message)

        message = input(" -> ")


    soc.close()


if __name__ == '__main__':
    Main()
