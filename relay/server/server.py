import os
from os import system as sys
import socket as soc
import time as tm
import subprocess as sub
from datetime import datetime as dt
import threading

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

class calculations:
    def __init__(self):
        #create a global variable for constants
        try:
            #global variable here
            self.error = 'error'
            self.userdata = sub.getoutput('pwd')+'/UTILS/users.txt'
            self.timestamp = sub.getoutput('pwd')+'/UTILS/timestamp.txt'
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

        try:
            for line in lines:
                if search_key in line:
                    #user_line = line.strip()
                    return True
                    break
            #id[0] user[1] key range[2] ip addr [3]

        except:
            return False




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
            print('User Connected To Relay')
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
        formated_time_time = current_datetime.strftime('%H:%M:%S')

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
        self.timestamp =sub.getoutput('pwd')+'/UTILS/timestamp.txt'
        self.soc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
        self.lock = threading.Lock()

    def open_server_timestamp(self):
        sock = self.soc
        ip = '0.0.0.0'
        port = 6060
        sock.bind((ip, port))
        sock.listen()

        while True:
            try:
                #with self.lock:
                if True:
                    open_file = open(self.timestamp, 'r')
                    read_file = open_file.readline().strip()
                    data = read_file
                    open_file.close
            
                conn, addr = sock.accept()
                conn.send(data.encode())

            except KeyboardInterrupt:
                conn.close()
            

    def connect_server_timestamp(self):
        while True:
            try:
                ipaddr = ['192.168.1.214', '192.168.1.208']
                for ip in ipaddr:
                    sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
                    tm.sleep(5)
                    #with self.lock:
                    if True:
                        open_file = open(self.timestamp, 'r')
                        read_file = open_file.readline().strip()
                        home_data = read_file
                        open_file.close()

                    status = sock.connect_ex((ip, 6060))
                    if status == 0:
                        data = sock.recv(1024).decode()
                        mate_data = data

                        mate = dt.strptime(mate_data, '%y-%m-%d %H:%M:%S')
                        home = dt.strptime(home_data, '%y-%m-%d %H:%M:%S')

                        if mate > home:
                            #with self.lock:
                            if True:
                                open_file = open(self.timestamp, 'w')
                                write_file = open_file.write(mate_data)
                                open_file.close()
                                print('Time Stamp Updated')

                            sock.close()
                        else:
                            print('Time Stamp Up TO Date')
                            sock.close()
                    else:
                        sock.close()
                        continue

            except KeyboardInterrupt:
                 sock.close()


class client_server:
    def __init__(self):
        self.soc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
        self.key = sub.getoutput('pwd')+'/UTILS/key.found'
        self.lastkey = sub.getoutput('pwd')+'/UTILS/lastkeys.txt'

    def create_user(self, conn, addrr):        
        user_key = conn.recv(1024).decode()
        key_range = calculations.create_id(user_key, addrr)
        print('User created Succesfully')
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
        user_secret, last_key = conn.recv(1024).decode().split(':')
        filter_data = calculations.check_id_info(user_secret)

        if filter_data == True:
            #with self.lock:
            if True:
                open_file = open(self.lastkey, 'r')
                read_file = open_file.readlines()
                open_file.close()

            user_found = False
            for data in read_file:
                if data.startswith(f'{user_secret}:'):
                    data = f'{user_secret}:{last_key}\n'
                    print('user exist')
                    user_found = True
                    break

            if not user_found:
                data = f'{user_secret}:{last_key}\n'
                print('user doesnt exist')

            #with self.lock:
            if True:
                open_file = open(self.lastkey, 'w')
                open_file.write(str(data))
                print('User key updated')
                open_file.close()
        else:
            print("User doesn't exist in database")







    def conn_relay(self):
        sock = self.soc
        sock.bind(('0.0.0.0', 5050))
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
                conn.close()








    


#code wont be executed, not a working code !!!!!!!

calculations, server_server, client_server = calculations(), server_server(), client_server()
engine1 = threading.Thread(target=calculations.create_id)
engine2 = threading.Thread(target=server_server.open_server_timestamp)
engine3 = threading.Thread(target=server_server.connect_server_timestamp)
engine4 = threading.Thread(target=client_server.conn_relay)

#program still on build
try:
    engine2.start()
    engine3.start()
    engine4.start()
except:
    conn.close()
    




