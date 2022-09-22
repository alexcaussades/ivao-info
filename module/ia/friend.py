
def fiends_pilote(vid, p):
    for a in range(0, len(p)):
        if(p[a]["userId"] == vid):
            print("Callsign: " + p[a]["callsign"])

def fiends_atc(vid, x):
    for a in range(0, len(x)):
        if(x[a]["userId"] == vid):
            print("Callsign: " + x[a]["callsign"])
