import socket
import select
import threading


def auxReadInput(text, i):
    commande = ''
    condition = (i < len(text)-1) & (text[i] != ' ')
    while condition:
        commande = commande + text[i]
        i += 1
        condition = (i < len(text)-1) & (text[i] != ' ')
    return (commande, i)


def ReadInput(text):
    data = []
    if text[0] != '/':
        return (0, text)
    else:
        while i != len(text):
            commande, y = auxReadInput(text, i)
            data = data.append(commande)
            i = y + 1


def Main():
    host = '127.0.0.1'
    port = 1459

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    soc.connect((host, port))

    documentation = "\n   Documentation :\n/HELP: print this message\n/LIST: list all available channels on server\n/JOIN <channel>: join (or create) a channel\n/LEAVE: leave current channel\n/WHO: list users in current channel\n<message>: send a message in current channel\n/MSG <nick> <message>: send a private message in current channel\n/BYE: disconnect from server\n/KICK <nick>: kick user from current channel [admin]\n/REN <channel>: change the current channel name [admin]\n"

    data = ''
    while data != 'done':
        # recoi le text envoyer par le server
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
        else:
            typ, data = ReadInput(message)
            if typ == 1:
                for i in range(len(data)):
                    soc.send(data[i].encode())
                reponce = soc.recv(1024).decode()
                print('Received from server: ' + reponce)
            else:
                # envoie le message au channel
                # envoie la demande de texte
                soc.send(data.encode())
                # recoi le text envoyer par le server
                data = soc.recv(1024).decode()
                print(data)

        message = input(" -> ")

    soc.close()


if __name__ == '__main__':
    Main()
