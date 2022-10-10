from uuid import uuid4

class Atc:
    def __init__(self, vid, uuid=None ):
        self.vid = vid
        self.uuid = str(uuid4())
        

if __name__ == '__main__':
    a = Atc(191514)
    print(a.uuid)
    print(a.vid)