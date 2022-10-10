import json
import os
from module_forms.Ia.class_log.time_log import timeLog

class airac(timeLog):
    
    def __init__(self) -> None:
        timeLog.__init__(self)  
        
    def airac_data(self):
        data = open(os.path.join("module_forms/ia/class_log/data-airac.json"))
        with data:
            airacdata = json.load(data)
            #print(airacdata["2022"]["10"])
            return airacdata
    
    def get_airac(self):
        airacData = self.airac_data()
        dateSr = self.datenow()
        year = dateSr.year
        month = dateSr.month
        return airacData[str(year)][str(month)]
        
    def get_date(self):
        airacData = self.get_airac()
        dateDay = self.datenow()
        if int(dateDay.day) > int(airacData["day"]):
            airacDataSet = str(airacData["day"])+"_"+str(airacData["month"])+"_"+str(dateDay.year)
            return airacDataSet
        
        
if __name__ == '__main__':
    a = airac().get_date()
    print(a)
    