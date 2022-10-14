import requests



url = "https://api.ivao.aero/v2/tracker/whazzup"
r = requests.get(url)
atc = r.json()
x = atc["clients"]["atcs"]

class atc_pos():
    
    def __init__(self, callsingAtc) -> None:
        self.callsing = callsingAtc
        
    def online_atc(self):
        i = {}
        for a in range(0, len(x)):
            if (x[a]["callsign"] == str(self.callsing)):
                i["callsign"] = x[a]["callsign"]
                i["frequency"] = x[a]["atcSession"]["frequency"]
                try:
                    i["atis"] = x[a]["atis"]["lines"]
                except:
                    i["atis"] = None
                try:
                    i["revision"] = x[a]["atis"]["revision"]
                except:
                    i["revision"] = None
                i['timestamp'] = x[a]["createdAt"]
                i["rating"] = x[a]["rating"]
                i["userId"] = x[a]["userId"]
                i["timestamp"]= x[a]["time"]
                return i

if __name__ == '__main__':
    a = atc_pos("LFLL_APP")
    print(a.online_atc())  