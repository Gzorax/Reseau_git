import socket
import select
import threading
import string
import time





# main function
if __name__ == "__main__":

    if(len(sys.argv) < 3):
        print('Usage : python tryclient.py hostname port')
        #sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

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
