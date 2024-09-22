import os
from os import system as sys
import socket as soc
import time as tm
import subprocess as sub


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

class botnet:
    def __init__(self):
        #create a global variable for constants
        try:
            #global variable here
            self.error = 'error'
            self.directory = sub.getoutput('pwd')
        except:
            pass

    def check_id_info(self):
        #open file 
        open_file = open(self.directory+'/users.txt', 'r')
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
        open_file = open(self.directory+'/users.txt', 'r')
        lines = open_file.readlines()
        open_file.close
        for line in lines:
            user_line = line.strip().split('-')[0]
        create_file = open(self.directory+'/users.txt', 'a')
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
        create_file.close()

    def calc_range(self):
        #open file to get the last assigned key range
        open_file = open(self.directory+'/users.txt', 'r')
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


botnet = botnet()
botnet.create_id()

