from itertools import count
import requests
import logging
import re


class aiport:

    def __init__(self, ident) -> None:
        self.barerToken = "x_LveP6GNrgdVJ9BxlmIUAJMOlfCMzTxNcnJC8zLgW0"
        self.urlBaseApi = "https://avwx.rest/api/"
        self.ident = ident

    def station(self):
        station = {}
        param = {"Accept": "*/*",
                 "Authorization": "Bearer Token "+self.barerToken}
        url = self.urlBaseApi+"station/"+self.ident
        getUrl = requests.get(url, headers=param)
        station = getUrl.json()
        return station

    def metar(self):
        metar = {}
        param = {"Accept": "*/*",
                 "Authorization": "Bearer Token "+self.barerToken}
        url = self.urlBaseApi+"metar/"+self.ident
        getUrl = requests.get(url, headers=param)
        returnmetar = getUrl.json()
        metar = {
            "metar": returnmetar["sanitized"],
            "rules": returnmetar["flight_rules"],
            "timestamp": returnmetar["time"]["dt"]
        }
        return metar

    def taf(self):
        metar = {}
        param = {"Accept": "*/*",
                 "Authorization": "Bearer Token "+self.barerToken}
        url = self.urlBaseApi+"taf/"+self.ident
        getUrl = requests.get(url, headers=param)
        returnmetar = getUrl.json()
        metar = {
            "taf": returnmetar["sanitized"],
            "timestamp": returnmetar["time"]["dt"]
        }
        return metar
    
    def runways(self):
        d = {}
        f = self.station()
        r = f["runways"]
        #lenR = len(f["runways"])
        for a in range(0, len(r)):
            print(a)
            d[a] = r[a]["ident1"], r[a]["ident2"]
        return d
        
            
if __name__ == '__main__':
    a = aiport("LFbl").runways()
    print(a)
