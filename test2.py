import requests

url = "https://api.ivao.aero/v2/tracker/whazzup"

r = requests.get(url)
whazzup = r.json()

x = whazzup["clients"]["atcs"]
p = whazzup["clients"]["pilots"]


# crée une function qui va créer une liste de tous les atc et les comparer avec le vid

def getATC(vid):
    atcInfo = {}
    for atc in x:
        if atc["userId"] == vid:
            atcInfo["callsign"] = atc["callsign"]
            atcInfo["rating"] = atc["rating"]
            atcInfo["vid"] = atc["userId"]
            atcInfo["revision"] = atc["atis"]["revision"]
            return atcInfo


def getPilot(vid):
    pilotInfo = {}
    for pilot in p:
        if pilot["userId"] == vid:
            pilotInfo["callsign"] = pilot["callsign"]
            pilotInfo["rating"] = pilot["rating"]
            pilotInfo["vid"] = pilot["userId"]
            pilotInfo["departureId"] = pilot["flightPlan"]["departureId"]
            pilotInfo["arrivalId"] = pilot["flightPlan"]["arrivalId"]
            pilotInfo["alternativeId"] = pilot["flightPlan"]["alternativeId"]
            pilotInfo["route"] = pilot["flightPlan"]["route"]
            pilotInfo["level"] = pilot["flightPlan"]["level"]
            pilotInfo["flightRules"] = pilot["flightPlan"]["flightRules"]
            return pilotInfo


def getPilotDepartureAirport(plateforme):
    pilotInfodepartureId = {}
    i = 0
    while True:
        pilotInfodepartureId[i] = getPilot(plateforme)["departureId"]
        i = i+1
        return pilotInfodepartureId
          
            
                
               


if __name__ == "__main__":
    # print(getATC(698934))
    # print(getPilot(698934))
    print(getPilotDepartureAirport("LFPO"))
    # print(getPilotArrivalAirport("LSZH"))
