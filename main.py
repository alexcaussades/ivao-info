#!/usr/bin/python3
import re
import requests
import json
import time
import os
import asyncio
import fnmatch
from datetime import datetime
from module.version import version
from module.ia.position import position_atc
from module.atc.atc import position_gen
from module.pilote.pilote import pilote_arriver
from module.ia.time import timestamp_atc
from module.ia.findAtc import srAtc
from module.help import help
from module.ia.friend import add_friends as addFriends
from module.ia.friend import creat_dic_verify_friends
from module.ia.pilote_list import pilote_list
from module.ia.atc_list import atc_list
import pyttsx3
from pathlib import Path

engine = pyttsx3.init()

url = "https://api.ivao.aero/v2/tracker/whazzup"

version()

r = requests.get(url)
atc = r.json()



x = atc["clients"]["atcs"]
p = atc["clients"]["pilots"]

print("{0} positions ATC ouverte, sur IVAO !".format(len(x)))
print("{0} Pilots en ligne, sur IVAO !".format(len(p)))
print("")

#engine.say("Bonsoir maxime je suis ton inteligence artificiel personelle pour IVAO. Que veux tu faire ? ")
#engine.runAndWait()

docs = "info-ivao"
dossier_data = "friends"
path = Path.home()

def pathData():
    return os.path.join(path, "AppData", "Roaming", docs, dossier_data)

def creat_dic_verify_friends():
    dic_friends = []
    arr = os.listdir(pathData())
    i = 0 
    while i <= len(arr):
        for r in range(0, len(arr)):
            txt = arr[r].split(".")
            dic_friends.append(int(txt[0]))
            i = i +1
        break
    return dic_friends

try:
  
  ivaosr = input("Qu'elle est votre recherche ? ")
  ivaoupper = ivaosr.upper()

  if(ivaosr == "-h"):
      help()
  
  if(ivaosr == "addfriends"):
    vid = input("Quelle est son vid ? :")
    name = input("Quelle est son nom ? :")
    lastname = input("Quelle est son prénon ? :")
    add = addFriends(vid=vid, name=name, lastname=lastname)
    add.creatjson()

  if(ivaosr == "online"):
    list_ivao_atc = atc_list(x)
    list_ivao_pilot = pilote_list(p)
    list_pc = creat_dic_verify_friends()
    list_gen = list_ivao_atc + list_ivao_pilot
    for i in list_gen:
      for j in list_pc:
          if(i==j):
              print(i)
              break
    


  try:
    args = ivaosr.split()
    ivaoupperArgs = ivaoupper.split()

    if(ivaoupper and args[1]):
      if(args[1] == "-a"):
        pilote_arriver(ivaoupperArgs[0], p)
        

      if(args[1] == "-f"):
        if(len(ivaoupperArgs[0]) <= 3):
          srAtc(ivaoupperArgs[0], x)
          

  except:
    tt = 'Vous pouvez pour utiliser des arguments taper "-h" pour en savoir plus !'
    print(tt)
  
  
  position_gen(ivaoupper, x)

  


except(KeyboardInterrupt):
  
  print(" Fermeture du logiciel")