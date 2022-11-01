import re
import requests
from module_forms.Ia.class_log.airac import airac
#from airac import airac

class chart_vac(airac):
    
    def __init__(self, icao) -> None:
        super().__init__()
        self.icao = icao
        self.urlStart = "https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_"
        self.airac = airac().get_date()
        self.urlend = "/Atlas-VAC/PDF_AIPparSSection/VAC/AD/AD-2."
        self.extention = ".pdf"
        
    def express(self):
        try:
            a = re.search(r'(\w{4})', self.icao)
            return a.group(0).upper()
        except:
            return ""
        
    def creatUrlShema(self):
        url = self.urlStart + str(self.airac) + self.urlend + self.express() + self.extention
        return str(url)
       
    
if __name__ == '__main__':
    a = chart_vac("LFBE_APP").creatUrlShema()
    print(a)