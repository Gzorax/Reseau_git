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



# main function
if __name__ == "__main__":




    host = '127.0.0.1'
    port = 1459

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    while True:
        try:
            s.connect((host, port))
            break
        except:
            print('Unable to connect')
            #sys.exit()

    print('Connected to remote host. Start sending messages')
    #prompt()
    
    for i in range(1):
        socket_list = [input(), s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(
            socket_list, [], [])

        for sock in read_sockets:
            # incoming message from remote server
            if sock == s:
                data = sock.recv(4096)

                # else:
                # print data
                s.send(data.decode())


            # user entered a message
            else:
                msg = input('your message here')
                s.send(msg.encode())
         

    i -=1


