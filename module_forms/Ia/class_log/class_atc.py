from uuid import uuid4

class Atc:
    def __init__(self, callsign, uuid=None ):
        self.callsing = callsign
        self.uuid = str(uuid4())
        

if __name__ == '__main__':
    a = Atc("POS015F")
    print(a.uuid)
    print(a.callsing)