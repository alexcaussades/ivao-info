# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QSystemTrayIcon, QFrame, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit, QListWidget, QCheckBox, QButtonGroup, QDialog, QMenu, QToolBar
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QShortcut, QShortcutEvent, QAction
import requests
import webbrowser
import time
from module_forms.Ia.class_log.atc_serach import search_ATC
from module_forms.Ia.class_log.class_pos import atc_pos
from module_forms.Ia.class_log.file import file
from module_forms.Ia.class_log.friends import friend
from module_forms.Ia.class_log.time_log import timeLog
from module_forms.Ia.class_log.vac import chart_vac
from module_forms.Ia.preference.pref import pref
from module_forms.Ia.class_log.airac import airac
from module_forms.Ia.class_log.version import version

url = "https://api.ivao.aero/v2/tracker/whazzup"

update_version = "https://api.github.com/repos/alexcaussades/ivao-info/releases"

r = requests.get(url)
atc = r.json()

x = atc["clients"]["atcs"]
p = atc["clients"]["pilots"]

data = pref().get_pref()
class mainWindows(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sim IVAO Info Serv")
        self.resize(600, 600)
        self.setWindowIcon(QIcon("./module_forms/icons/airplane.png"))
        self.url_profile = "https://ivao.aero/Login.aspx?r=Member.aspx?Id="
        
        self.btn_friend = QPushButton("Friends")
        self.btn_friend.clicked.connect(self.btn_friends)
                                
        # Label online ATCs and Pilote
        self.atc_online = QLabel(
            "Online: {0} ATC - {1} Pilot".format(len(x), len(p)))
        self.font = self.atc_online.font()
        self.font.setPointSize(10)
        self.atc_online.setFont(self.font)

        self.version_app = QLabel("Version "+ version("0.5.1","alpha").getVersion())
        self.version_app.setAlignment(Qt.AlignRight)

        self.main_w = QGridLayout(self)
        self.list_ATC = QListWidget()
        self.list_ATC.itemDoubleClicked.connect(self.list_sr)
        
        self.af = QLineEdit()
        self.af.setPlaceholderText("Search...")
        self.af.returnPressed.connect(self.search)
                
        self.reload = QPushButton("Reload")
        self.reload.setIcon(QIcon(QIcon("./module_forms/icons/synchronize.png")))
        self.reload.clicked.connect(self.update_enter)
        
        self.check_Value_ATC = QCheckBox("ATC", self)
        self.check_Value_ATC.setCheckable(True)
        self.check_Value_ATC.clicked.connect(self.on_atc_click)
        
        self.check_Value_Pilote = QCheckBox("Pilot")
        self.check_Value_Pilote.setCheckable(True)
        self.check_Value_Pilote.clicked.connect(self.on_pilote_click)
        
        self.main_w.addWidget(self.btn_friend, 0,0,1,1)
        self.main_w.addWidget(self.reload, 0,1,1,1)
        self.main_w.addWidget(self.atc_online, 1, 0, 1, 4)
        self.main_w.addWidget(self.check_Value_ATC, 2, 0, 1, 1)
        self.main_w.addWidget(self.check_Value_Pilote, 2, 1, 1, 1)
        self.main_w.addWidget(self.af, 2, 2, 1, 1)
        self.main_w.addWidget(self.list_ATC, 3, 0, 1, 3)
        self.main_w.addWidget(self.version_app, 9, 2, 1, 1)  
    
    def update_json_atc(self):
        url = "https://api.ivao.aero/v2/tracker/whazzup"
        r = requests.get(url)
        atc = r.json()
        x = atc["clients"]["atcs"]
        self.atc_online.hide()
        return x
    
    def update_json_pilot(self):
        url = "https://api.ivao.aero/v2/tracker/whazzup"
        r = requests.get(url)
        atc = r.json()
        p = atc["clients"]["pilots"]
        self.atc_online.hide()
        return p
        
    def update_enter(self):
        x = self.update_json_atc()
        p = self.update_json_pilot()
        self.atc_online = QLabel(
            f"Online: {len(x)} ATC - {len(p)} Pilot")
        self.font = self.atc_online.font()
        self.font.setPointSize(10)
        self.atc_online.setFont(self.font)
        self.main_w.addWidget(self.atc_online, 1, 0, 1, 4)
        
    def btn_friends(self):
        self.windowFriend = QWidget()
        gridInfoSr = QGridLayout(self.windowFriend)
        vidsList = friend().verif_friend()
        self.ghj = QLabel("Friends Online : ")
        list_ivao_atc = friend(list=x).atc_list()
        list_pc = vidsList
        list_gen = list_ivao_atc
        for i in list_gen:
            for j in list_pc:
                if(i==j):
                    i = i
                    break
        
        self.returnVid = QLabel("Fonctionnalité en cour de devs")             
        self.windowFriend.grind = gridInfoSr
        self.windowFriend.setWindowTitle("Friends")
        self.windowFriend.grind.addWidget(self.ghj, 0,0,1,2)
        self.windowFriend.grind.addWidget(self.returnVid, 0,2,1,2)
        self.windowFriend.show()
        
    def on_atc_click(self, check):
        if check:
            print("je suis la")
        else:
            print("je ne suis pas là ")   
        
    def on_pilote_click(self, check):
        if True:
            print(check)
    
    def chart(self):   
        url = "https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_06_OCT_2022/Atlas-VAC/PDF_AIPparSSection/VAC/AD/AD-2."+self.plateforme+".pdf"
        webbrowser.open(url)
    
    def profil_web(self):
        url = self.url_profile + str(self.vidAdd)
        webbrowser.open(url)
    
    def list_sr(self, item):
       
        IcaoAtc = item.text() if item else ""
        atc = atc_pos(IcaoAtc)
        pos_dic = atc.online_atc()
        self.window = QWidget()
        self.window.setWindowIcon(QIcon("./module_forms/icons/lock.png"))
        gridInfoSr = QGridLayout(self.window)
        
        self.plateforme = chart_vac(IcaoAtc).express()
        self.vac = QPushButton("VAC")
        self.vac.setIcon(QIcon(QIcon("./module_forms/icons/pdf.png")))
        self.vac.clicked.connect(self.chart)
        
        self.vidAdd = pos_dic["userId"]
        
        self.addfriend = QPushButton("Add Friends")
        self.addfriend.setIcon(QIcon(QIcon("./module_forms/icons/user--plus.png")))
        self.addfriend.clicked.connect(self.addFriend)
        
        self.profil_users = QPushButton("Account Users")
        self.profil_users.setIcon(QIcon(QIcon("./module_forms/icons/user-green.png")))
        self.profil_users.clicked.connect(self.profil_web)
        
        if(self.vidAdd in friend().verif_friend()):
            self.addfriend = QPushButton("Your Friends")
        
        self.frequency = QLabel("Frequency : {0} Mhz".format(pos_dic["frequency"]))
        self.frequency.setStyleSheet("color: red; font-weight: bold;")
        
        
        
        try:
            self.metar = QLabel("METAR : {0} ".format(pos_dic["atis"][3]))
        except:
            self.metar = QLabel("METAR : No METAR ")
        try:
            self.rwy = QLabel("RWY : {0} ".format(pos_dic["atis"][4]))
        except:
             self.rwy = QLabel("")
        
        try:
            self.revision = QLabel("{0}".format(pos_dic["atis"][2]))
        except:
            self.revision = QLabel("")
        
        
        
        self.timestamp = QLabel("Online: {0}".format(timeLog(pos_dic["timestamp"]).get_TimesTamp()))
        self.window.setWindowTitle("Information for : {0}". format(pos_dic["atis"][1]))
        self.window.grind = gridInfoSr
        self.window.grind.addWidget(self.frequency, 0,0,1,2)
        self.window.grind.addWidget(self.revision, 0,2,1,1)
        self.window.grind.addWidget(self.metar, 1,0,1,4)
        self.window.grind.addWidget(self.rwy, 2,0,1,4)
        self.window.grind.addWidget(self.timestamp, 3,0,1,3)
        self.window.grind.addWidget(self.vac, 4,0,1,1)
        self.window.grind.addWidget(self.profil_users, 4,1,1,1)
        self.window.grind.addWidget(self.addfriend, 4,4,1,1)
        self.window.show()
    
    # revoir la function !                                    
    def search(self):
        self.list_ATC.show()
        self.list_ATC.clear()
        ivaoupper = self.af.text().upper()
        srs = search_ATC(ivaoupper)
        srsf = srs.finaly_atc()
        liste = []
        liste.append(friend().verif_friend())
        vid = []        
        for i in range(0,len(srsf)):    
            pos = atc_pos(srsf[i]).online_atc()
            #vid.append(pos["userId"])
            self.list_ATC.addItem(str(pos["callsign"]))
            #self.list_ATC.setStyleSheet("color: green; font-weight: bold;")
            #self.list_ATC.addItem(str(pos["callsign"]))
                    
                            
                
    def addFriend(self):
        self.vid = self.vidAdd
        a = friend(self.vid)
        a.creat_files()
        self.addfriend.setText("You Friend") 
        
        
    
file().creat_arborecence()
#file().openfiles()
app = QApplication()
main_windows = mainWindows()
main_windows.show()
app.exec()


