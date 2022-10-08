import requests



url = "https://api.ivao.aero/v2/tracker/whazzup"
update_version = "https://api.github.com/repos/alexcaussades/ivao-info/releases"

url_VAC = "https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_06_OCT_2022/Atlas-VAC/PDF_AIPparSSection/VAC/AD/AD-2.LFPO.pdf"

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
                i["frequency"] = x[a]["atcSession"]["frequency"]
                i["atis"] = x[a]["atis"]["lines"]
                i["revision"] = x[a]["atis"]["revision"]
                i['timestamp'] = x[a]["createdAt"]
                i["rating"] = x[a]["rating"]
                i["userId"] = x[a]["userId"]
                return i
