
from module_forms.Ia.class_log.file import file
import json
import os

class pref:
    
    def __init__(self) -> None:
        pass
    
    def creatdic(self):
        dic = {"devs": False, "friend": False}
        return dic
    
    def get_pref(self):
        if file().get_dossier_pref():
            try:
                data = open(file().pathData_pref()+"/preference.json")
                with data:
                    datajson = json.load(data)
                    return datajson
            except:
                self.creat_files()
        else:
            self.creat_files()
    
    def creat_files(self):
        creatfile = json.dumps(self.creatdic(), indent=4)
        files = open(file().pathData_pref()+"/preference.json", "w")
        files.write(creatfile)
        files.close()
    