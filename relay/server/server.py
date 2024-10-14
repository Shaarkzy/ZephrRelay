import os
from os import system as sys
import socket as soc
import time as tm
import subprocess as sub
from datetime import datetime as dt
from datetime import timedelta as tmd
import threading
import signal

'''
-check last id done
-create id done
-create key range done
-create database text format done
-assign key range and id done
-calculate key range done
-see active users
-receive valid key done
-get total key scanned from users every 10secs
-if a user not active for 5days, send a destruct and assign new id
-receive last key scanned from users every 5mins done

''' 

print('-Welcome Host-\n-To Close The Program Properly: Hit Enter Key Thrice-')
tm.sleep(4)

class calculations:
    def __init__(self):
        #create a global variable for constants
        try:
            #global variable here
            self.error = 'error'
            self.userdata = sub.getoutput('pwd')+'/UTILS/users.txt'
            self.timestamp = sub.getoutput('pwd')+'/UTILS/timestamp.txt'
            self.lastkey = sub.getoutput('pwd')+'/UTILS/lastkeys.txt'
            self.lock = threading.Lock()
        except:
            pass

    def check_id_info(self, search_key):
        #open file
        #with self.lock:
        if True:
            open_file = open(self.userdata, 'r')
            lines = open_file.readlines()
            open_file.close()

        for line in lines:
            if search_key in line:
                return True
                #id[0] user[1] key range[2] ip addr [3]
            else:
                continue


    def check_lastsec(self, searchsec):
        if True:
            open_file = open(self.lastkey, 'r')
            lines = open_file.readlines()
            open_file.close()

        for line in lines:
            if searchsec in line:
                return True
            #usersec[0] key[1]
            else:
                continue






    def create_id(self, user_secret, ip_addr):
        #open file
        #with self.lock:
        if True:
            open_file = open(self.userdata, 'r')
            lines = open_file.readlines()
            open_file.close

        for line in lines:
            user_line = line.strip().split('-')[0]
        with self.lock:
            create_file = open(self.userdata, 'a')

            new_id = int(user_line) + 10
            key_range = self.calc_range()
            ip = (ip_addr)[0]+'\n'
            new_data = str(new_id) + '-' + user_secret + '-' + key_range +'-'+ ip 
            create_file.write(new_data)

            #initiate time stamp
            self.create_time_stamp()
            create_file.close()
            print('-User Connected To Relay-')
        return key_range





    def calc_range(self):
        #open file to get the last assigned key range
        #with self.lock:
        if True:
            open_file = open(self.userdata, 'r')
            lines = open_file.readlines()
            open_file.close()

        for line in lines:
            last_range = line.strip().split('-')[2].split(':')[1]
        interv = 10000000 #number of key to be scanned by every users
        start = int(last_range, 16) #start for every users
        stop = int('7ffffff', 16) #key range end value

        #create key range
        while start <= stop:
            end = start + interv
            key_range = hex(start).lstrip('0x').zfill(12) + ':' + hex(min(end, stop +1) -1).lstrip('0x').zfill(12)
            start = end + 1
            return key_range

    def create_time_stamp(self):
        current_datetime = dt.now()
        formated_time_date = current_datetime.strftime('%y-%m-%d')
        formated_time_time = current_datetime.strftime('%H:%M:%S.%f')

        #calculate timestamp
        calculated_stamp = formated_time_date + ' ' + formated_time_time
        #create file to store timestamp
        #with self.lock:
        if True:
            open_file = open(self.timestamp, 'w')
            open_file.write(calculated_stamp)
            open_file.close()







class server_server:
    def __init__(self):
        #declare global variable
        self.timestamp = sub.getoutput('pwd')+'/UTILS/timestamp.txt'
        self.userdata = sub.getoutput('pwd')+'/UTILS/users.txt'
        self.lastkey = sub.getoutput('pwd')+'/UTILS/lastkeys.txt'
        self.soc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
        self.lock = threading.Lock()
        self.flag = True

    def kill_(self):
        os.kill(os.getpid(), signal.SIGKILL)


    def inp(self):
        data = input()
        data = input('-Again-')
        data = input('-Again-')
        self.flag = False
        print('-Server Closed-')
        os._exit(0)


    def open_server_timestamp(self):
        sock = self.soc
        ip = '0.0.0.0'
        port = 6060
        sock.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)

        try:
            sock.bind((ip, port))
        except:
            print('-An Error Occured: Killing Process -> TMPSERVER-\n-Please Do Close The Program Properly Next Time: Try Restarting The Program Now-')
            sys('kill -9 $(lsof -t -i :6060)')
        sock.listen()

        while True:
            try:
                if self.flag:
                #with self.lock:
                    if True:
                        open_file = open(self.timestamp, 'r')
                        read_file = open_file.readline().strip()
                        time_data = read_file
                        open_file.close

                        open_file = open(self.userdata, 'r')
                        read_file = open_file.read()
                        user_data = read_file
                        open_file.close()

                        open_file = open(self.lastkey, 'r')
                        read_file = open_file.read()
                        user_lastkey = read_file
                        open_file.close()
            

                    conn, addr = sock.accept()
                    tm.sleep(2)
                    conn.send(user_data.encode())
                    tm.sleep(2)
                    conn.send(time_data.encode())
                    tm.sleep(2)
                    conn.send(user_lastkey.encode())
                    conn.close()
                else:
                    conn.close()
                    break

            except KeyboardInterrupt:
                os._exit(0)
            except:
                os._exit(0)
            

    def connect_server_timestamp(self):
        while True:
            try:
                if True:
                    #configure server ip
                    ipaddr = ['192.168.1.214']
                    for ip in ipaddr:
                        sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
                        #tm.sleep(2)
                        #with self.lock:
        
                        if True:
                            open_file = open(self.timestamp, 'r')
                            read_file = open_file.readline().strip()
                            home_data = read_file
                            open_file.close()
 
                        status = sock.connect_ex((ip, 6060))

                        if status == 0:
                            user_data = sock.recv(2048).decode()
                            database = user_data.splitlines()
 
                            time_data = sock.recv(1024).decode()
                            mate_data = time_data

                            user_lastkey = sock.recv(2048).decode()
                            lastkeys = user_lastkey.splitlines()

                            mate = dt.strptime(mate_data, '%y-%m-%d %H:%M:%S.%f')
                            home = dt.strptime(home_data, '%y-%m-%d %H:%M:%S.%f')

                            if mate > home:
                                #with self.lock:
                                if True:
                                    for line in database:
                                        user = line.split('-')[1]
                                        if calculations.check_id_info(user):
                                            print('user exist')
                                            continue
                                        else:
                                            open_file = open(self.userdata, 'a')
                                            open_file.write(line+'\n')
                                            open_file.close()
                                    print('-Database Updated-')

                                    open_file = open(self.timestamp, 'w')
                                    write_file = open_file.write(mate_data)
                                    open_file.close()
                                    print('-Time Stamp Updated-')

                                    for line in lastkeys:
                                        secret = line.split(':')[0]
                                        if calculations.check_searchsec(secret):
                                            continue
                                        else:
                                            open_file = open(self.lastkey, 'a')
                                            write_file = open_file.write(line+'\n')
                                            open_file.close()
                                    print('-Last.Key DB Updated-')


                                sock.close()
                            else:
                               print('-Time Stamp Up TO Date-')
                               sock.close()
                        else:
                            sock.close()
                            continue
                else:
                    sock.close()
                    break

            except KeyboardInterrupt:
                os._exit(0)
            except:
                os._exit(0)


class client_server:
    def __init__(self):
        self.soc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
        self.key = sub.getoutput('pwd')+'/UTILS/key.found'
        self.lastkey = sub.getoutput('pwd')+'/UTILS/lastkeys.txt'

    def create_user(self, conn, addrr):        
        user_key = conn.recv(1024).decode()
        key_range = calculations.create_id(user_key, addrr)
        print(f'-Connected Device: {addrr[0]}-')
        print('-User Created Succesfully-')
        tm.sleep(2)
        conn.send(key_range.encode())


    def receive_key(self, conn):
        key = conn.recv(1024).decode()
        #with self.lock:
        if True:
            open_file = open(self.key, 'w')
            open_file.write(key)
            open_file.close()

            #initiate all client self destruct
            #self destruct funcrion ...... here


    def update_client_key(self, conn):
        try:
            user_secret, last_key = conn.recv(1024).decode().split(':')

            filter_data = calculations.check_id_info(user_secret)

            if filter_data == True:
                #with self.lock:
                if True:
                    open_file = open(self.lastkey, 'r')
                    read_file = open_file.readlines()
                    open_file.close()

                    check = False
                    database = []
                    for data in read_file:
                        data = data.replace('\n', '')
                        if data.startswith(f'{user_secret}:'):
                            new_data = f'{user_secret}:{last_key}'
                            database.append(new_data)
                            check = True
                        elif data.startswith(':'):
                            database.append('')

                        else:
                            database.append(data+'\n')

                    if not check:
                        open_file = open(self.lastkey, 'r')
                        read_file = open_file.readlines()
                        user_data = f'{user_secret}:{last_key}'
                        database = []
                        for data in read_file:
                            database.append(data)
                        database.append(user_data)
                        open_file.close()

                        open_file = open(self.lastkey, 'w')
                        open_file.writelines(database)
                        open_file.close()

                    else:
                        open_file = open(self.lastkey, 'w')
                        open_file.writelines(database)
                        open_file.close()
                    print('-User Key Updated-')



            else:
                print("-User doesn't exist in database-")
        except:
            pass







    def conn_relay(self):
        sock = self.soc
        sock.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
        try:
            sock.bind(('0.0.0.0', 5050))
        except:
            print('-An Error Occured: killing Process -> RELAY-\n-Please Close The Program Properly Next Time, Try Restarting The Program Now- ')
            sys('kill -9 $(lsof -t -i :5050)')
        sock.listen()

        while True:
            try:
                conn, addr = sock.accept()
                request = conn.recv(1024).decode()

                if request == 'create':
                    self.create_user(conn, addr)
                elif request == 'valid':
                    self.receive_key(conn)
                elif request == 'update':
                    self.update_client_key(conn)

            except KeyboardInterrupt:
                os._exit(0)
            except:
                continue








    



calculations, server_server, client_server = calculations(), server_server(), client_server()
engine1 = threading.Thread(target=server_server.open_server_timestamp)
engine2 = threading.Thread(target=server_server.connect_server_timestamp)
engine3 = threading.Thread(target=client_server.conn_relay)
engine4 = threading.Thread(target=server_server.inp)

#program still on build

engine1.start()
engine2.start()
engine3.start()
engine4.start()
    




