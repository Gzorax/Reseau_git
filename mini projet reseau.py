import socket
import select
import threading

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
        chanel_dict[chanel] =  [client]
    #sinon ajouter le client au chanel
    else:
        chanel_dict[chanelName] = chanel_dict[chanelName].append(client)
    return chanel_dict
    

def who (chanelName, chanel_dict):
    #affiche l'admin : @admin_name@
    #affiche les noms des clients du chanel
    listclient = chanel_dict[chanelName]
    print ("@",listclient[0],"@")
    for client in range (1,listclient.length):
      print (listclient[client])

def prv_msg (pseudo, message, client_dict):
     #affiche le message au client concerné uniquement
     for client in client_dict:
           if (client == pseudo):
                 #affiche le message au client

def leave (pseudo, chanelDict):
      #le client decide de quitte le chanel
      #retoruver le client dans son chanel
      for chanel in chanelDict:
            for client in chanelDict[chanel]:
                  if (client == pseudo):
                        chanelDict[chanel] = del chanelDict[chanel][client]
                        return chanelDict
      
def bye ():
    #fonction inconue 
    #quitte le chat ?

    
def kill (client):
    # si demande d'admin:
    #   ferme le chanel

def ban (client):
    #si demande d'admin:
    #   leave (client,chanel)
    #   banList += client

def send_msg_channel (client_dict, channel_dict, chanel, message #, envoyeur):
      for client in channel_dict[chanel]:
            #if client != envoyeur
              client_dict[client].send(message)
            
    


        #appel des commandes
        #commande = input()
        #if (commande == "\name <pseudo>"):
            # change le pseudo du client
            # retourne le dictionnaire des client modifiés
            DictClient = nick(pseudo, client, DictClient)
        
        if (commande == "\chanel_list"):
            # affiche la liste des chanel actifs
            # ne retourne rien
            chanel_list( DictChannel )
        
        if (commande == "\join <name>"):
            # ajoute le client dans le chanel demandé
            # s'il n'existe pas, le crée
            # retourne le nouveau dictionnaire des channel
            DictChannel = join(pseudo, name, DictChannel)

        if (commande == "\who" ):
            #affiche la liste des clients du chanel
            # ne retourne rien
            who(channel, DictChannel)
        
        if (commande ==  "\ prv_msg <name>"):
            # affiche le message en question seulement pour le client
            # ne retourne rien
            message = input("votre messgage pour" name "?")
            prv_msg(name, message)
        
        if (commande ==  "\ leave"):
            # supprime le client du channel
            # retourne le nouveau dictionnaire de channel
            DictChannel = leave(client,DictChannel)
        
        if (commande ==  "\ bye"):
            # quitte le server ?
            # ne retourne rien
            bye()


