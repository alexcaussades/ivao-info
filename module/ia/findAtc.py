import fnmatch
import re
import time

def srAtc(ivao, x):
    addJocker = ivao + "*"
    d = addJocker.split("*")
    for a in range(0, len(x)):
        icaoList = [x[a]["callsign"]]
        for b in range(0, len(icaoList)):
            filtered = fnmatch.filter(icaoList, addJocker)
            filteredd = list(filter(None, filtered))
            for r in filteredd:
                if not r:
                    continue
                print(r)

