from module.ia.position import position_atc


def position_app(ivaoupper, x):
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

def position_twr(ivaoupper, x):
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

def position_gnd(ivaoupper, x):
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

def position_del(ivaoupper, x):
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

def position_afis(ivaoupper, x):
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

def position_crr(ivaoupper, x):
  for crr in range(0, len(x)): 
    if (x[crr]["callsign"] == ivaoupper + position_atc["CTR"]):
      print("Position ATC: {0} | Freq: {1} Mhz".format(ivaoupper + position_atc["CTR"], x[crr]["atcSession"]["frequency"]))
      print("")

def position_close(ivaoupper, x):
  for m in range(0,len(x)):
    if (not x[m]["callsign"] == ivaoupper):
      print("Aucune possition ouverte...")
      break


def position_gen(ivaoupper, x):
  position_app(ivaoupper, x)
  position_twr(ivaoupper, x)
  position_gnd(ivaoupper, x)
  position_afis(ivaoupper, x)
  position_crr(ivaoupper, x)
  #position_close(ivaoupper, x)