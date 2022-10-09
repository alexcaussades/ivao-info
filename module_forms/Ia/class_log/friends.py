from pathlib import Path
import json
import os
from pytz import timezone
import pytz
from uuid import uuid4
from module_forms.Ia.class_log.file import file 
from datetime import datetime
from time import time, timezone


class friend:
    
    def __init__(self, vid, uuid=None) -> None:
        super().__init__()
        self.vid = vid
        self.uuid = str(uuid4())
        
    def check_docs_friend(self):
        return file().pathData_friend()
        
    def creatdic(self):
        dic = {"vid": self.vid, "timestamp": self.timestamp()}
        return dic

    def timestamp(self):
        now = datetime.now(pytz.timezone('UTC'))
        new_now = now.replace(microsecond=0) 
        set_utc_time = new_now.replace(tzinfo=pytz.utc).timestamp()
        return set_utc_time
        
    def creat_files(self):
        creatfile = json.dumps(self.creatdic(), indent=4)
        files = open(file().pathData_friend()+"/"+ str(self.uuid)+".json", "w")
        files.write(creatfile)
        files.close()
        
        
if __name__ == '__main__':
    a = friend(191514)
    a.creat_files()
   