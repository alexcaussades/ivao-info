import sys
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit, QListWidget
from PySide6.QtCore import Qt
import requests
import json

url = "https://api.ivao.aero/v2/tracker/whazzup"
update_version = "https://api.github.com/repos/alexcaussades/ivao-info/releases"

r = requests.get(url)
atc = r.json()

x = atc["clients"]["atcs"]
p = atc["clients"]["pilots"]

class mainWindows(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sim IVAO Info Serv")
        self.resize(400, 400)
        
        #Label online ATCs and Pilote
        self.atc_online = QLabel("ATCs : {0} Online - Pilots : {1} Online".format(len(x), len(p)))
        self.font = self.atc_online.font()
        self.font.setPointSize(10)
        self.atc_online.setFont(self.font)
        
        self.version_app = QLabel("Version Alpha 0.0.1")
        self.version_app.setAlignment(Qt.AlignRight)
        
        self.main_w = QGridLayout(self)
        self.list_ATC = QListWidget()
        self.af = QLineEdit()
        self.af.setPlaceholderText("ATCs Online")
        self.btn_enter = QPushButton("Entrée")
        self.btn_atc = QPushButton("text")

        
        self.main_w.addWidget(self.atc_online, 0, 0, 1, 4)
        self.main_w.addWidget(self.list_ATC, 1, 0, 1, 3)
        
        self.main_w.addWidget(self.af, 2,0,1,1)
        self.main_w.addWidget(self.btn_enter, 2,2,1,1)
        self.main_w.addWidget(self.btn_atc, 3, 0, 1, 4)
        self.main_w.addWidget(self.version_app, 4,2,1,1)

app = QApplication()
main_windows = mainWindows()
main_windows.show()
app.exec()
