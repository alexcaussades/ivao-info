import os
from pathlib import Path


docs = "info-ivao"
dossier_friend = "friends"
dossier_pref = "preference"
path = Path.home()

class file:
    
    def __init__(self) -> None:
        self.path = path
        self.friend = dossier_friend
        self.pref = dossier_pref
        self.docs = docs
    
    def pathData_gen(self):   
        return os.path.join(self.path, "AppData", "Roaming", self.docs)
        
    def pathData_friend(self):
        return os.path.join(self.path, "AppData", "Roaming", self.docs, self.friend)
    
    def pathData_pref(self):
        return os.path.join(self.path, "AppData", "Roaming", self.docs, self.pref)
    
    def get_dossier_gen(self):
        if os.path.exists(self.pathData_gen()):
            return True
        else:
            os.makedirs(self.pathData_gen(), mode=0o777)
    
    def get_dossier_friend(self):
        if os.path.exists(self.pathData_friend()):
            return True
        else:
            os.makedirs(self.pathData_friend(), mode=0o777)
            
    def get_dossier_pref(self):
        if os.path.exists(self.pathData_pref()):
            return True
        else:
            os.makedirs(self.pathData_pref(), mode=0o777)
            
    def creat_arborecence(self):
        self.get_dossier_gen()
        self.get_dossier_friend()
        self.get_dossier_pref()
        
    
    def openfiles(self):
        os.system("start "+ self.pathData_gen())

if __name__ == '__main__':
    a = file()
    a.creat_arborecence()
    print(a.openfiles())
    