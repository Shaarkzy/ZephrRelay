import os
from os import system as sys
import socket as soc
import time as tm
import subprocess as sub
import threading
from datetime import datetime as dt
import uuid


'''
run keyhunt
save keyrange to cache file
ask keyhunt to store last scanned key every 10mins
send key scanned to server every 15mins
send valid key to server
send session time to server
receive destruct sequence
'''

class client_keyhunt:
    def __init__(self):
        #....global for keyhunt
        self.true = True
        self.lastkey = sub.getoutput('pwd')+'/UTILS/lastkey.txt'



class client_server:
    def __init__(self):
        self.user = sub.getoutput('pwd')+'/UTILS/user.txt'
        self.lastkey = sub.getoutput('pwd')+'/UTILS/lastkey.txt'
        self.keyfound = sub.getoutput('pwd')+'/UTILS/key.found'
        self.lock = threading.Lock()





    def create_secret(self):
        data = str(uuid.uuid4()).replace(':', '')[:14]
        data = data.replace('-', '')

        return data


    def user_exists(self):
        open_file = open(self.user, 'r')
        read_file = open_file.read()
        open_file.close()
        if read_file:
            return True
        else:
            return False





    def create_user(self):
        #sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
        if not self.user_exists():
            user_cr = False
            while not user_cr:
                try:
                    #configure server ip
                    ipaddr = ['n.n.n.n']
                    for ip in ipaddr:
                        sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
                        tm.sleep(2)
                        status = sock.connect_ex((ip, 5050))

                        secret = self.create_secret()

                        if status == 0:
                            sock.send('create'.encode())
                            tm.sleep(4)
                            sock.send(secret.encode())
                            print('Connected To Server Relay')
                            key_range = sock.recv(1024).decode()
                            data = secret + '-' + key_range
                  
                            #with self.lock:
                            if True:
                                open_file = open(self.user, 'w')
                                open_file.write(data)
                                open_file.close()
                                sock.close()
                                print('User created')
                                user_cr = True
                                break

                        else:
                            sock.close()
                            continue
                except KeyboardInterrupt:
                    sock.close()

        else:
            print('Your Data Already Exists')





    def send_validkey(self):
        #with self.lock:
        if True:
            open_file = open(self.keyfound, 'r')
            data = open_file.read()
            open_file.close()

        if data:
            return True
        else:
            return False




    def last_key(self):
        #with self.lock:
        if True:
            open_file = open(self.lastkey, 'r')
            data = open_file.read()
            open_file.close()

        return data




    def server_validkey(self, sock, key):
        sock.send('valid'.encode())
        tm.sleep(1)
        sock.send(key.encode())
        print('Valid Key Sent To Server')

    def update_key(self, sock, data):
        sock.send('update'.encode())
        tm.sleep(1)
        sock.send(data.encode())
        print('Last Key Scanned Sent To Server')



    def conn_relay(self):
        while True:
            try:
                tm.sleep(3)
                #configure server ip
                ipaddr = ['n.n.n.n']
                for ip in ipaddr:
                    sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
                    tm.sleep(2)
                    '''
                    valid key
                    update key scanned
                    '''
                    #code for valid key
                    status = sock.connect_ex((ip, 5050))
                    if status == 0:
                        if self.send_validkey():
                            #with self.lock:
                            if True:
                                open_file = open(keyfound, 'r')
                                keyx = open_file.read()
                                self.server_validkey(sock, keyx)
                        else:
                            pass


                        #code to write last key to server
                        last_key = self.last_key()
                        #with self.lock:
                        if True:
                            open_file = open(self.user, 'r')
                            user = open_file.readline().split('-')[0]
                            open_file.close()

                        data = user+':'+last_key
                        self.update_key(sock, data)
                        sock.close()

                    else:
                        continue

            except KeyboardInterrupt:
                sock.close()





                            
client_server = client_server()
engine1 = threading.Thread(target=client_server.create_user)
engine2 = threading.Thread(target=client_server.conn_relay)

#still on build
#engine1.start()
#engine2.start()






                




