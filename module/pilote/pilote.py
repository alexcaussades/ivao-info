

def pilote_arriver(ivaoupper, p):
    for a in range(0, len(p)):
        if(p[a]["flightPlan"]["arrivalId"] == ivaoupper):
            print("Callsign: "+ p[a]["callsign"] + " | Type: "+ p[a]["flightPlan"]["flightRules"]+ " | Status: "+ p[a]["lastTrack"]["state"]+ " | Aircraft: "+ p[a]["flightPlan"]["aircraft"]["model"])

