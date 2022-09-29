import sqlite3 
import os
import logging
import socket
import json
from pathlib import Path


docs = "info-ivao"
dossier_data = "friends"
path = Path.home()

def pathData():
    return os.path.join(path, "AppData", "Roaming", docs, dossier_data)

def fiends_pilote(vid, p):
    for a in range(0, len(p)):
        if(p[a]["userId"] == vid):
            print("Callsign: " + p[a]["callsign"])

def fiends_atc(vid, x):
    for a in range(0, len(x)):
        if(x[a]["userId"] == vid):
            print("Callsign: " + x[a]["callsign"])

def get_dossier():
    if os.path.exists(pathData()):
        return True
    else:
        os.makedirs(pathData(), mode=0o777)

def opendocs():
    os.system("start "+ os.path.join(path, "AppData", "Roaming", docs))

opendocs()

# get_dossier()
# dic = {"vid": 191514, "name": "Caussades", "lasname": "Alexandre"}
# creatfile = json.dumps(dic, indent=4)
# localfile = open(pathData()+"/"+ str(dic["vid"])+".json", "w")
# localfile.write(creatfile)
# localfile.close()

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

# p1 = add_friends(191520, "thyrerryy", "qskdkqizdjq")
# print(p1.creatjson())

