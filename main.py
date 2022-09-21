import re
import requests
import json
import time
import asyncio
from datetime import datetime
from module.version import version
from module.ia.position import position_atc
from module.atc.atc import position_gen
from module.pilote.pilote import pilote_arriver

url = "https://api.ivao.aero/v2/tracker/whazzup"

version()

r = requests.get(url)
atc = r.json()

x = atc["clients"]["atcs"]
p = atc["clients"]["pilots"]

print("{0} positions ATC ouverte, sur IVAO !".format(len(x)))
print("{0} Pilots en ligne, sur IVAO !".format(len(p)))
print("")

try:
  
  ivaosr = input("qu'elle est votre recherche ? ")
  ivaoupper = ivaosr.upper()
  try:
    args = ivaosr.split()
    ivaoupperArgs = ivaoupper.split()

    if(ivaoupper and args[1]):
      if(args[1] == "-a"):
        pilote_arriver(ivaoupperArgs[0], p)

  except:
    tt = 'Vous pouvez pour utiliser des arguments taper "-h" pour en savoir plus !'
    print(tt)
  
  
  position_gen(ivaoupper, x)

except(KeyboardInterrupt):
   print(" Fermeture du logiciel")