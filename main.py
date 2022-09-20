import re
import requests
import json
import datetime
from module.version import version
from module.ia.position import position_atc

url = "https://api.ivao.aero/v2/tracker/whazzup"

version()

ivaosr = input("qu'elle est votre recherche ? ")

ivaoupper = ivaosr.upper()

r = requests.get(url)
atc = r.json()

x = atc["clients"]["atcs"]



print("{0} positions ATC ouverte, sur IVAO !".format(len(x)))
print("")

for a in range(0, len(x)):
  if (x[a]["callsign"] == ivaoupper + position_atc["APP"]):
    print("Position ATC: {0} | Freq: {1} Mhz".format(ivaoupper + position_atc["APP"], x[a]["atcSession"]["frequency"]))
    print(x[a]["atis"]["lines"][3])
    print(x[a]["atis"]["lines"][4])
    print(x[a]["atis"]["lines"][5])
    try:
      if("CONFIRM" in x[a]["atis"]["lines"][6]):
        print(x[a]["atis"]["lines"][6])
        print("")
    except(IndexError):
      print("")
    
for t in range(0, len(x)):  
  if (x[t]["callsign"] == ivaoupper + position_atc["TWR"]):
    print("Position ATC: {0} | Freq: {1} Mhz".format(ivaoupper + position_atc["TWR"], x[t]["atcSession"]["frequency"]))
    print(x[t]["atis"]["lines"][3])
    print(x[t]["atis"]["lines"][4])
    print(x[t]["atis"]["lines"][5])
    try:
      if("CONFIRM" in x[t]["atis"]["lines"][6]):
        print(x[t]["atis"]["lines"][6])
        print("")
    except(IndexError):
      print("")
    

for g in range(0, len(x)): 
  if (x[g]["callsign"] == ivaoupper + position_atc["GND"]):
    print("Position ATC: {0} | Freq: {1} Mhz".format(ivaoupper + position_atc["GND"], x[g]["atcSession"]["frequency"]))
    print(x[g]["atis"]["lines"][3])
    print(x[g]["atis"]["lines"][4])
    print(x[g]["atis"]["lines"][5])
    try:
      if("CONFIRM" in x[g]["atis"]["lines"][6]):
        print(x[g]["atis"]["lines"][6])
        print("")
    except(IndexError):
      print("")

for d in range(0, len(x)): 
  if (x[d]["callsign"] == ivaoupper + position_atc["DEL"]):
    print("Position ATC: {0} | Freq: {1} Mhz".format(ivaoupper + position_atc["DEL"], x[d]["atcSession"]["frequency"]))
    print(x[d]["atis"]["lines"][3])
    print(x[d]["atis"]["lines"][4])
    print(x[d]["atis"]["lines"][5])
    try:
      if("CONFIRM" in x[d]["atis"]["lines"][6]):
        print(x[d]["atis"]["lines"][6])
        print("")
    except(IndexError):
      print("")

for af in range(0, len(x)): 
  if (x[af]["callsign"] == ivaoupper + position_atc["AFIS"]):
    print("Position ATC: {0} | Freq: {1} Mhz".format(ivaoupper + position_atc["AFIS"], x[af]["atcSession"]["frequency"]))
    print(x[af]["atis"]["lines"][3])
    print(x[af]["atis"]["lines"][4])
    print(x[af]["atis"]["lines"][5])
    try:
      if("CONFIRM" in x[af]["atis"]["lines"][6]):
        print(x[af]["atis"]["lines"][6])
        print("")
    except(IndexError):
      print("")

for crr in range(0, len(x)): 
  if (x[crr]["callsign"] == ivaoupper + position_atc["CTR"]):
    print("Position ATC: {0} | Freq: {1} Mhz".format(ivaoupper + position_atc["CTR"], x[crr]["atcSession"]["frequency"]))
    print("")
    

for m in range(0,len(x)):
  if (not x[m]["callsign"] == ivaoupper):
    print("Aucune possition ouverte...")
    break