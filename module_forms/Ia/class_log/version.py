class version:
    
    def __init__(self, numero, typeOfVersion ) -> None:
        self.numero = numero
        self.typeOfVersion = typeOfVersion
    
    def getVersion(self):
        return self.numero+"-"+self.typeOfVersion