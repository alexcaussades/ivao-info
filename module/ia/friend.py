import sqlite3 
import os
import logging
import socket
from pathlib import Path


docs = "datacliivao"

def pathData():
    return os.path.join(Path.home())

def fiends_pilote(vid, p):
    for a in range(0, len(p)):
        if(p[a]["userId"] == vid):
            print("Callsign: " + p[a]["callsign"])

def fiends_atc(vid, x):
    for a in range(0, len(x)):
        if(x[a]["userId"] == vid):
            print("Callsign: " + x[a]["callsign"])

def get_dossier():
    if(os.path.exists(pathData())):
        with open(pathData(), "r") as data:
            return data
    else:
        return os.mkdir(pathData())


#print(get_dossier())
print(pathData())
