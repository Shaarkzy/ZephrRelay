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
print('-Welcome User-\n-Please When Closing The program: Hit Enter Key Thrice-')
tm.sleep(4)


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


    def inp(self):
        data = input()
        data = input('-Again-')
        data = input('-Again-')
        print('Disconnected')
        os._exit(0)





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
                    ipaddr = ['192.168.1.40']
                    for ip in ipaddr:
                        sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
                        tm.sleep(2)
                        status = sock.connect_ex((ip, 5050))

                        secret = self.create_secret()

                        if status == 0:
                            tm.sleep(2)
                            sock.send('create'.encode())
                            tm.sleep(2)
                            sock.send(secret.encode())
                            print('-Connected To Server Relay-')
                            key_range = sock.recv(1024).decode()
                            data = secret + '-' + key_range
                  
                            #with self.lock:
                            if True:
                                open_file = open(self.user, 'w')
                                open_file.write(data)
                                open_file.close()
                                sock.close()
                                print('-User created-')
                                user_cr = True
                                break

                        else:
                            sock.close()
                            continue
                except KeyboardInterrupt:
                    os._exit(0)

        else:
            print('-Your Data Already Exists-')





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
        tm.sleep(2)
        sock.send('valid'.encode())
        tm.sleep(2)
        sock.send(key.encode())

    def update_key(self, sock, data):
        tm.sleep(2)
        sock.send('update'.encode())
        tm.sleep(2)
        sock.send(data.encode())


    def funct1(self):
        ipaddr = ['192.168.1.40']
        for ip in ipaddr:
            sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
            status = sock.connect_ex((ip, 5050))
            if status == 0:
                if self.send_validkey():
                    open_file = open(self.keyfound, 'r')
                    keyx = open_file.read()
                    self.server_validkey(sock, keyx)
                    sock.close()
                else:
                    sock.close()
                    pass


    def funct2(self):
        ipaddr = ['192.168.1.40']
        for ip in ipaddr:
            sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
            status = sock.connect_ex((ip, 5050))
            if status == 0:
                last_key = self.last_key()
                open_file = open(self.user, 'r')
                user = open_file.readline().split('-')[0]
                open_file.close()

                data = user+':'+last_key
                self.update_key(sock, data)
                sock.close()

            else:
                sock.close()
                pass
                




    def conn_relay(self):
        while True:
            try:
                self.funct1()
                self.funct2()
            except KeyboardInterrupt:
                os._exit(0)





                            
client_server = client_server()
engine1 = threading.Thread(target=client_server.create_user)
engine2 = threading.Thread(target=client_server.conn_relay)
engine3 = threading.Thread(target=client_server.inp)

#still on build
engine1.start()
engine2.start()
engine3.start()
