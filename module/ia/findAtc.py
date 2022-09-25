import fnmatch
import re

def srAtc(ivao, x):
    d = ivao.split("*")
    for a in range(0, len(x)):
        icaoList = [x[a]["callsign"]]
        for b in range(0, len(icaoList)):
            filtered = fnmatch.filter(icaoList, ivao)
            filteredd = list(filter(None, filtered))
            for r in filteredd:
                if not r:
                    continue
                print(r)

