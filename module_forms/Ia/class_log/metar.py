import re
import requests



class metar:
    
    def __init__(self, information) -> None:
        self.url = "https://api.met.no/weatherapi/tafmetar/1.0/metar?extended=true&icao="
        self.information = information
    
    def search_metar(self):
        r = requests.get(self.url + self.express())
        t = []
        metarUrl = r.text
        infoMetar = metarUrl.split("=")
        t.append(infoMetar[0])
        return t[0]
    
    def express(self):
        try:
            a = re.search(r'(\w{4})', self.information)
            return a.group(0).upper()
        except:
            return "LFBL"

if __name__ == '__main__':
    a = metar("")
    print(a.search_metar())    
    