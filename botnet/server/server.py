import os
from os import system as sys
import socket as soc
import time as tm
import subprocess as sub
from datetime import datetime as dt
import threading

'''
-check last id
-create id
-create key range
-create database text format
-assign key range and id
-calculate key range
-see active users
-receive valid key
-get total key scanned from users every 10secs
-if a user not active for 5days, send a destruct and assign new id
-receive last key scanned from users every 5mins

''' 

class calculations:
    def __init__(self):
        #create a global variable for constants
        try:
            #global variable here
            self.error = 'error'
            self.userdata = sub.getoutput('pwd')+'/users.txt'
            self.timestamp = sub.getoutput('pwd')+'/timestamp.txt'
        except:
            pass

    def check_id_info(self):
        #open file 
        open_file = open(self.userdata, 'r')
        lines = open_file.readlines()
        open_file.close()
        #input user detail to fetch full information
        search_keyword = input('key: ')
        for line in lines:
            if search_keyword in line:
                user_line = line.strip()
        #input number to get specific user data
        info = int(input('id[] user[1] key range[2]'))
        print(user_line.split('-')[info])


    def create_id(self):
        #open file
        open_file = open(self.userdata, 'r')
        lines = open_file.readlines()
        open_file.close
        for line in lines:
            user_line = line.strip().split('-')[0]
        create_file = open(self.userdata, 'a')
        while True:
            user_spe = input('enter any 8 random letter: ')
            length = len(user_spe)
            if length < 8 or length > 8:
                print('text should be 8')
            else:
                break
        new_id = int(user_line) + 10
        key_range = self.calc_range()+'\n'
        new_data = str(new_id) + '-' + user_spe + '-' + key_range 
        create_file.write(new_data)
        #initiate time stamp
        self.create_time_stamp()
        create_file.close()

    def calc_range(self):
        #open file to get the last assigned key range
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
        open_file = open(self.timestamp, 'w')
        open_file.write(calculated_stamp)
        open_file.close()







class server_server:
    def __init__(self):
        #declare global variable
        self.timestamp =sub.getoutput('pwd')+'/timestamp.txt'
        self.soc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

    def open_server_timestamp(self):
        sock = self.soc
        ip = '0.0.0.0'
        port = 6060
        try:
            data = sock.bind((ip, int(port)))
        except OSError:
            print('error occured: run again')
            data = sub.getoutput(f'sudo kill -9 $(sudo lsof -t -i :6060)')


        while True:
            try:
                open_file = open(self.timestamp, 'r')
                data = open_file.read()

                sock.listen(5)
                conn, addr = sock.accept()
                conn.send(data.encode())
            except KeyboardInterrupt:
                conn.close()
                break

    def connect_server_timestamp(self):
        sock = self.soc
        while True:
            try:
               ip_A_B = ['192.168.1.40', '192.168.2.1']
               port = 6060
               for ip in ip_A_B:
                   try:
                       sock.settimeout(100)
                       sock.connect((ip, int(port)))
                       break
                   except (soc.error, ConnectionRefusedError):
                      pass
               data = sock.recv(20480).decode()
               #compare stamps
               mate_server_stamp = str(data)
               open_file_home = open(self.timestamp, 'r')
               home_server_stamp = open_file_home.read()
               stp1 = datetime.strptime(mate_server_stamp, '%y-%m-%d %H:%M:%S')
               stp2 = datetime.strptime(home_server_stamp, '%y-%m-%d %H:%M:%S')
               if stp1 > stp2:
                   open_file = open(self.timestamp, 'w')
                   open_file.write(str(data))
                   open_file.close()
               else:
                   pass
            except KeyboardInterrupt:
                sock.close()







       
#code wont be executed, not a working code !!!!!!!

calculations, server_server = calculations(), server_server()
engine1 = threading.Thread(target=calculations.create_id)
engine2 = threading.Thread(target=server_server.open_server_timestamp)
engine3 = threading.Thread(target=server_server.connect_server_timestamp)

engine2.start()
engine3.start()




