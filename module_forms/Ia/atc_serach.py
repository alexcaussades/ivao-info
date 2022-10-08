
import sys
import requests

sys.setrecursionlimit(150)

url = "https://api.ivao.aero/v2/tracker/whazzup"
update_version = "https://api.github.com/repos/alexcaussades/ivao-info/releases"

url_VAC = "https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_08_SEP_2022/Atlas-VAC/PDF_AIPparSSection/VAC/AD/AD-2.LFPO.pdf"

r = requests.get(url)
atc = r.json()

x = atc["clients"]["atcs"]

class search_ATC:
    
    def __init__(self, ivao):
        self.ivao = ivao
    
    def srAtc2(self):
        addJocker = self.ivao 
        icaoList = []
        for a in range(0, len(x)):
            icaoList.append(x[a]["callsign"])
        if icaoList :
            res = [x for x in icaoList if x.startswith(addJocker)]
            return res
    
    def finaly_atc(self):
        r = self.srAtc2()
        return r                 
        
                   
if __name__ == '__main__':
    a = search_ATC("LF")
    print(a.finaly_atc())    
    