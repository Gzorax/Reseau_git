import socket
import select
import threading


def ReadCode(text, i):
    commande = ''
    while text[i] != ' ':
        commande = commande + text[i]
        #p 
        i += 1
        if i >= len(text):
            return (commande, i)
    return (commande, i)

def SEND(conn,message,dictPseudo, dictChannel):
    clitext = 'You : ' + message + '\n'
    pseudo = dictPseudo[conn]
    for chan in dictChannel:
        if conn in dictChannel[chan]:
            chanList = dictChannel[chan]
            break
    for i in range(len(chanList)):
        #print (str(chanList[i]))
        if chanList[i] != conn:
            text = pseudo + " : " + message + "\n"
            print (text)
            chanList[i].send(text.encode())
    return clitext

def PSEUDO(dictClient, conn):
    data = "what's your name ?"
    conn.send(data.encode())
    ps = conn.recv(1024).decode()
    while ps in dictClient:
        data = "name alredy taken, please chose an other"
        conn.send(data.encode())
        ps = conn.recv(1024).decode()
    dictClient[ps] = conn
    return (dictClient, ps)

def Admin(conn, dictChannel):
    for channel in dictChannel:
            if conn in dictChannel[channel]:
                    channelList = dictChannel[channel]
                    break
    if conn == channelList[0]:
        return (True,channel)
    return (False,channel)


def LIST(dictChannel):
    data = "\n\n   List of availble channels:\n"
    for channel in dictChannel:
        data = data + channel + "\n"
    return data


def JOIN(dictChannel, name, conn):
    if name in dictChannel:
        print("\n added to existing channel")
        chanList = dictChannel[name]
        chanList = chanList + [conn]
        dictChannel[name] = chanList
    else:
        print ("channel created")
        dictChannel[name] = [conn]

    print (dictChannel)
    return dictChannel

def LEAVE(dictChannel,conn):
        for channel in dictChannel:
                if conn in dictChannel[channel]:
                        dictChannel[channel] = dictChannel[channel].remove(conn)
                        if not (dictChannel[channel]):
                            del dictChannel[channel] 
                        return dictChannel

def WHO(dictChannel, conn, dictPseuod):
        for channel in dictChannel:
            if conn in dictChannel[channel]:
                    channelList = dictChannel[channel]
                    break
        rep = '@' + dictPseuod[channelList[0]] + '@\n'
        for connection in range(1 ,len(channelList)):
                rep = rep + dictPseuod[channelList[connection]] + '\n'
        return rep

def KICK(pseudo,chanel, dictChannel,dictClient):
    conn = dictClient[pseudo]
    dictChannel[chanel] = dictChannel[chanel].remove(conn)
    return dictChannel

def REN(channel,dictChannel,name):
    chanList = dictChannel[channel]
    del dictChannel[channel]
    if name in dictChannel:
        return (dictChannel,False)
        
    else:
        dictChannel[name] = chanList
        return (dictChannel,True)

def Main():
# init
    #host = "127.0.0.1"
    CONNECTION_LIST = []
    RECV_BUFFER = 4096

    port = 1459
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_soc.bind(('localhost', port))
    server_soc.listen(10)
    
    #conn, addr = server_soc.accept()
    #print("\n Connection from: " + str(addr))
    CONNECTION_LIST.append(server_soc)


# données
        #dictClient[pseudo] = conn
    dictClient = {}
    #dictPseudo[conn] = pseudo
    dictPseudo = {}
    #dictChannel[channel] = [conn]
    dictChannel = {}

# initialisation des données pour pseudoest a un seul client
    dictChannel["kiwitopia"] = []
    dictChannel["licornTime"] = []


    while True:
    #check for interactions
        rSoc, w, e = select.select(CONNECTION_LIST, [], [], 0)
    #affect interactions
        for conn in rSoc:
            
        #nouveau client
            if conn == server_soc:
                conn,adr = server_soc.accept()
            # demande la pseudo avant toute autre action!
                dictClient, name = PSEUDO(dictClient, conn)
                dictPseudo[conn] = name
                CONNECTION_LIST.append(conn)
                conn.send("done".encode())
                print("\n name saved : " + name)


            #interactions des clients deja connectés
            else:
            # recoie les données
                reponse = ''
                data = conn.recv(RECV_BUFFER).decode()
                print("\n reveved data : " + data)
                code, i = ReadCode(data, 0)

                if code == 'chanellMSG':
                    message, i = ReadCode(data, i+1)
                    reponse = SEND(conn,message,dictPseudo,dictChannel)

                elif code == '/LIST':
                    print("\n comande enter : LIST")
                    reponse = LIST(dictChannel)
                    #break

                elif code == '/JOIN':
                    print("\n commande enter : JOIN")
                    chanel, i = ReadCode(data, i+1)
                    dictChannel = JOIN(dictChannel, chanel, conn)
                    reponse = "Your now connected to : " + chanel
                    #break

                elif code == '/LEAVE':
                    print("\n comande enter : LEAVE")
                    dictChannel = LEAVE(dictChannel,conn)
                    reponse = "You have leave the channel"
                    #break

                elif code == '/WHO':
                    print("\n comande enter : WHO")
                    reponse = "Users in current channel :\n" + WHO(dictChannel,conn,dictPseudo)
                    #break

                elif code == '/KICK':
                    print("\n commande enter : KICK")
                    ps, i = ReadCode(data, i+1)
                    adm, chan = Admin(conn,dictChannel)
                    if adm:
                        dictChannel = KICK(ps,chan,dictChannel,dictClient)
                        reponse = ps + " has been kicked of the channel"
                    else:
                        reponse = "you are not alowed to do that"
                    #break

                elif code == '/REN':
                    print("\n commande enter : REN")
                    name, i = ReadCode(data, i+1)
                    adm, chan = Admin(conn,dictChannel)
                    if adm:
                        change,done = REN(chan,dictChannel,name)
                        if done:
                            reponse = "channel name has been change to : " + name
                            dictChannel = change
                        else:
                            reponse = "chose an other name, this one is not avaiable"
                    else:
                        reponse = "you are not alowed to do that"
                    #break

                elif code == '/MSG':
                    pseudo, i = ReadCode(data,i+1)
                    message,i= ReadCode(data,i+1)
                    cli = dictClient[pseudo]
                    cli.send(message.encode())
                    reponse = "You to " + pseudo + ' : ' + message

                elif code == 'bye':
                    CONNECTION_LIST.remove(conn)

                else:
                    reponse = 'wrong commade, /HELP for usage'


                print("\n sending : " + reponse)
                conn.send(reponse.encode())


    server_soc.close()


if __name__ == '__main__':
    Main()
