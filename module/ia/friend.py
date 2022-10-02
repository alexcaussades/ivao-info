import sqlite3 
import os
import logging
import socket
import json
import re
import asyncio
from pathlib import Path


docs = "info-ivao"
dossier_data = "friends"
path = Path.home()

def pathData():
    return os.path.join(path, "AppData", "Roaming", docs, dossier_data)



def get_dossier():
    if os.path.exists(pathData()):
        return True
    else:
        os.makedirs(pathData(), mode=0o777)

def opendocs():
    os.system("start "+ os.path.join(path, "AppData", "Roaming", docs))




class add_friends():

    def __init__(self, vid, name=None, lastname=None):
        self.vid = vid
        self.name = name
        self.lastname = lastname
    
    def srvid(self):
        return self.vid
    
    def creatdic(self):
        dic = {"vid": self.vid, "name": self.name, "lastname": self.lastname}
        return dic

    def creatjson(self):
        creatfile = json.dumps(self.creatdic(), indent=4)
        localfile = open(pathData()+"/"+ str(self.srvid())+".json", "w")
        localfile.write(creatfile)
        localfile.close()
        try:
            with open (pathData()+"/"+ str(self.srvid())+".json", "r"): pass
            print("Add your friends successful")

        except IOError:
            print("Add friends is bad ")
        


class verify_friends():

    def __init__(self, vid=None):
        self.vid = vid
    
    def creat_dic_verify_friends(self):
        dic_friends = []
        arr = os.listdir(pathData())
        i = 0 
        while i <= len(arr):
            for r in range(0, len(arr)):
                txt = arr[r].split(".")
                dic_friends.append(txt[0])
            i = i +1
            break
        return dic_friends
    
    def verify_friends(vid):
        if vid in self.creat_dic_verify_friends():
            print("je suis present !")
        

def fiends_pilote(vid, p):
    for a in range(0, len(p)):
        if(p[a]["userId"] == vid):
            print("Callsign: " + p[a]["callsign"])

def fiends_atc(vid):
    x = verify_friends()
    x.verify_friends(str(vid))
    
