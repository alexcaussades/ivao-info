from pathlib import Path
import json
import os
from turtle import width
from pytz import timezone
import pytz
from uuid import uuid4
from module_forms.Ia.class_log.file import file 
from datetime import datetime
from module_forms.Ia.class_log.time_log import timeLog
# from time_log import timeLog
# from file import file 


class friend(timeLog):
    
    def __init__(self, vid=None, uuid=None) -> None:
        super().__init__()
        self.vid = vid
        self.uuid = str(uuid4())
        
    def check_docs_friend(self):
        return file().pathData_friend()
        
    def creatdic(self):
        dic = {"vid": self.vid, "timestamp": self.set_Timestamp()}
        return dic
        
    def creat_files(self):
        creatfile = json.dumps(self.creatdic(), indent=4)
        files = open(file().pathData_friend()+"/"+ str(self.uuid)+".json", "w")
        files.write(creatfile)
        files.close()
    
    def creatDicFriend(self):
        dic_friends = []
        dic_vid = []
        arr = os.listdir(file().pathData_friend())
        i = 0
        while i <= len(arr):
            for r in range(0, len(arr)):
                dic_friends.append(arr[r])
                i = i +1
            break
        for o in range(0, len(dic_friends)):
            data = open(file().pathData_friend()+"/"+ dic_friends[o], "r")
            with data:
                datavid = json.load(data)
                dic_vid.append(datavid["vid"])
                continue  
        return dic_vid
    
    def verif_friend(self):
       return self.creatDicFriend()
        
if __name__ == '__main__':
    a = friend(191514)
    print(a.verif_friend())
   