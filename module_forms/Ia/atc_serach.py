
import sys
import requests

sys.setrecursionlimit(150)

url = "https://api.ivao.aero/v2/tracker/whazzup"
update_version = "https://api.github.com/repos/alexcaussades/ivao-info/releases"

url_VAC = "https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_08_SEP_2022/Atlas-VAC/PDF_AIPparSSection/VAC/AD/AD-2.LFPO.pdf"

r = requests.get(url)
atc = r.json()

x = atc["clients"]["atcs"]

class search_ATC:
    """Classe sur la recheche des ATC en ligne sur IVAO 
    """    
    
    def __init__(self, ivao):
        self.ivao = ivao
    
    def srAtc2(self):
        """ Recheche des ATC en ligne sur IVAO et filte par la recherche des données envoyer par l'utilisateur dans la class !
        
        Keyword arguments:
            - ``ivao`` = ``information utilisteur``
            - ``x ``=``list de ivao en format JSON``
            
        Returns:
            - ``res``: ``List(string)``
        """
        addJocker = self.ivao 
        icaoList = []
        for a in range(0, len(x)):
            icaoList.append(x[a]["callsign"])
        if icaoList :
            res = [x for x in icaoList if x.startswith(addJocker)]
            return res
    
    def finaly_atc(self):
        """ Class Final du filtrage des ATCs\n
        Function :
            ``srAtc2 -> list``
        """        
        r = self.srAtc2()
        return r                 
        
                   
# if __name__ == '__main__':
#     a = search_ATC("LF")
#     print(a.finaly_atc())    
    