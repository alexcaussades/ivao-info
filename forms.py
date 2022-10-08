import sys
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit, QListWidget, QCheckBox, QButtonGroup, QDialog
from PySide6.QtCore import Qt
import requests
import json
import asyncio
from module_forms.Ia.atc_serach import search_ATC
from module_forms.Ia.class_log.class_pos import atc_pos

url = "https://api.ivao.aero/v2/tracker/whazzup"
update_version = "https://api.github.com/repos/alexcaussades/ivao-info/releases"

url_VAC = "https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_08_SEP_2022/Atlas-VAC/PDF_AIPparSSection/VAC/AD/AD-2.LFPO.pdf"

r = requests.get(url)
atc = r.json()

x = atc["clients"]["atcs"]
p = atc["clients"]["pilots"]


class mainWindows(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sim IVAO Info Serv")
        self.resize(400, 400)

        # Label online ATCs and Pilote
        self.atc_online = QLabel(
            "Online: {0} ATC - {1} Pilot".format(len(x), len(p)))
        self.font = self.atc_online.font()
        self.font.setPointSize(10)
        self.atc_online.setFont(self.font)

        self.version_app = QLabel("Version Alpha 0.0.1")
        self.version_app.setAlignment(Qt.AlignRight)

        self.main_w = QGridLayout(self)
        self.list_ATC = QListWidget()
        #self.list_ATC.hide()
        self.list_ATC.itemDoubleClicked.connect(self.list_sr)
        
        
        self.af = QLineEdit()
        self.af.setPlaceholderText("Search...")
        self.af.returnPressed.connect(self.search)
        
        
        self.btn_enter = QPushButton("Entrée")
        self.check_Value_ATC = QCheckBox("ATC", self)
        self.check_Value_ATC.clicked.connect(self.on_atc_click)
        
        
        self.check_Value_Pilote = QCheckBox("Pilot")
        
        self.main_w.addWidget(self.atc_online, 0, 0, 1, 4)
        self.main_w.addWidget(self.check_Value_ATC, 2, 0, 1, 1)
        self.main_w.addWidget(self.check_Value_Pilote, 2, 1, 1, 1)
        self.main_w.addWidget(self.af, 2, 2, 1, 1)
        # self.main_w.addWidget(self.btn_enter, 2, 3, 1, 1)
        self.main_w.addWidget(self.list_ATC, 3, 0, 1, 3)
        self.main_w.addWidget(self.version_app, 9, 2, 1, 1)
        
    def on_atc_click(self):
        pass
        
    def list_sr(self, item):
        IcaoAtc = item.text()
        atc = atc_pos(IcaoAtc)
        pos_dic = atc.online_atc()
        self.window = QWidget()
        gridInfoSr = QGridLayout(self.window)
        self.frequency = QLabel("Frequency : {0} Mhz".format(pos_dic["frequency"]))
        self.metar = QLabel("METAR : {0} ".format(pos_dic["atis"][3]))
        self.rwy = QLabel("RWY : {0} ".format(pos_dic["atis"][4]))
        self.revision = QLabel("Revision : {0} ".format(pos_dic["revision"]))
        self.window.setWindowTitle("Information for : {0}". format(pos_dic["atis"][1]))
        self.window.grind = gridInfoSr
        self.window.grind.addWidget(self.frequency, 0,0,1,2)
        self.window.grind.addWidget(self.revision, 0,3,1,2)
        self.window.grind.addWidget(self.metar, 1,0,1,4)
        self.window.grind.addWidget(self.rwy, 2,0,1,4)
        self.window.show()
        
                                 
    def search(self):
        self.list_ATC.show()
        self.list_ATC.clear()
        ivaoupper = self.af.text().upper()
        srs = search_ATC(ivaoupper)
        srsf = srs.finaly_atc()
        for i in range(0,len(srsf)):
            self.list_ATC.addItem(srsf[i])
                
       
        
        
    

app = QApplication()
main_windows = mainWindows()
main_windows.show()
app.exec()
