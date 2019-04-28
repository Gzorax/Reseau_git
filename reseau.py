import socket
import select
import threading



def send_msg_channel (client_dict, channel_dict, chanel, message):
    for client in channel_dict[chanel]:
            #if client != envoyeur
        client_dict[client].send(message)

def nick (name, client, client_dict):
      # redefini le pseudo du client
  pseudo = input("quel est ton nouveau pseudo ?")
  while ((pseudo in client_dict) == True):
    pseudo = input ("ce pseudo est deja utilisé, choisis-en un autre")
  client_dict[pseudo] = client
  del client_dict[name]
  return client_dict

def chanel_list (chanel_dict):
    #affiche les chanels disponibles
    for i in chanel_dict:
        print (chanel_dict[i])

def join (name,chanelName,chanel_dict,):
    #permet de rejoindre un chanel
    #   si le chanel n'existe pas, le créer
    if ((chanelName in chanel_dict) == False):
        chanel_dict[chanelName] =  [name]
    #sinon ajouter le client au chanel
    else:
        chanel_dict[chanelName] = chanel_dict[chanelName].append(name)
    return chanel_dict
    

def who (chanelName, chanel_dict):
    #affiche l'admin : @admin_name@
    #affiche les noms des clients du chanel
    listclient = chanel_dict[chanelName]
    print ("@" + listclient[0] + "@")
    for client in range (1,listclient.length):
      print (listclient[client])

def prv_msg (pseudo, message, client_dict):
     #affiche le message au client concerné uniquement
     for client in client_dict:
           if (client == pseudo):
                client_dict[client].send(message)
                break

def leave (pseudo, chanelDict):
      #le client decide de quitte le chanel
      #retoruver le client dans son chanel
    for chanel in chanelDict:
        for client in chanelDict[chanel]:
            if (client == pseudo):
                del chanelDict[chanel][client]
                return chanelDict

def Server():
    #init
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soc.bind(('', 1459))
    soc.listen(10)

    #données
    i = 1
    soc_list = [soc]
    outputs = []
    serverClients = []
    serverAdresses = []
    DictClient = {} ## dict()
    DictChannel = {}

    while i == 1:
        readable, writable, exceptions = select.select(soc_list, outputs, soc_list)
        for s in readable:
            #un client se connecte au server
            if s is soc:
                client, adresse = s.accept()
                client.send('vous etes connecté'.encode())
                message = " bonjour a toi, quel est ton pseudo\n"
                s.send(message.encode())
                pseudo = s.recv(4096)
                
            # ajout du client au dicti onnaire de socket clients
                while ((pseudo in DictClient) == True):
                    pseudo = s.input("ce pseudo est deja utilisé, choisis-en un autre\n")
                    

                DictClient[pseudo] = client
                
                s.input("/name <pseudo> -> pour changer de nom\n /chanel_list -> affiche la liste des caneaux \n /join <name> -> rejoindre le chanel <name> \n /who -> affiche la liste des autres participents du canal \n /prv_msg <name> -> Envoie le prochain message a l'ulisateur concerné uniquement\n /leave -> quitter le chanel\n /bye -> quitter le server\n")

                soc_list.append(client)
                serverClients.append(client)
                serverAdresses.append(adresse)
                #s.send(bytes('Name ?', 'utf-8'))
            
            #client deja connecté interagis
            else: 
                data_client, clientName = s.recvfrom(4096)

            #appel des commandes
                commande = input()
                #if (commande == "\name <pseudo>"):
                # change le pseudo du client
                # retourne le dictionnaire des client modifiés
                DictClient = nick(pseudo, client, DictClient)
        
                if (commande == "\chanel_list"):
                    # affiche la liste des chanel actifs
                    # ne retourne rien
                    chanel_list( DictChannel )
        
                #if (commande == "\join <name>"):
                    # ajoute le client dans le chanel demandé
                    # s'il n'existe pas, le crée
                    # retourne le nouveau dictionnaire des channel
                    #DictChannel = join(pseudo, name, DictChannel)

                #if (commande == "\who" ):
                    #affiche la liste des clients du chanel
                    # ne retourne rien
                    #who(channel, DictChannel)
        
                #if (commande ==  "\ prv_msg <name>"):
                    # affiche le message en question seulement pour le client
                    # ne retourne rien
                    # message = input("votre messgage pour" name "?")
                #    message = s.recv(4096)
                #prv_msg(name, message)
        
                if (commande ==  "\ leave"):
                    # supprime le client du channel
                     # retourne le nouveau dictionnaire de channel
                     DictChannel = leave(client,DictChannel)
        
                #if (commande ==  "\ bye"):
                    # quitte le server ?
                    # ne retourne rien
                 #   bye()   
            
            # envoyer a tout le server
   
            #    print(data_client)
            #   if len(data_client) == 0:
            #       print("no data")
            #       s.close()
            #       soc_list.remove(s)   
            #   else: 
            #       print("data_sending")
            #       for y in serverClient:
            #           y.send(data_client)
            #       print("data_sent")

                for chanel in DictChannel:
                    for client in DictChannel[chanel]:
                        if (client  ==clientName):
                            send_msg_channel(DictClient,DictChannel, chanel, data_client)
                            break
                        
        else:
            for s in exceptions:
                print ("closed socket")
                s.close()
                soc_list.remove(s)

        
            



Server()
