import requests
import os
from pathlib import Path
import zipfile
import wget
from PySide6.QtWidgets import QApplication, QWidget, QProgressBar, QMessageBox, QSystemTrayIcon, QFrame, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit, QListWidget, QCheckBox, QButtonGroup, QDialog, QMenu, QToolBar
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QShortcut, QShortcutEvent, QAction

class version:
       
    def __init__(self, numero, typeOfVersion ) -> None:
        self.numero = numero
        self.typeOfVersion = typeOfVersion
        self.url = "https://api.github.com/repos/alexcaussades/ivao-info/releases/latest"
    
    def getVersion(self):
        return self.numero+"-"+self.typeOfVersion
    
    def getUrlReleasesGithub(self):
        r = requests.get(self.url)
        res = r.json()
        releases = {"name": res["name"], "urlFiles": res["assets"][0]["browser_download_url"], "body": res["body"], "urlGithub": res["url"], "size": res["assets"][0]["size"], "download_count": res["assets"][0]["download_count"], "created_at": res["assets"][0]["created_at"], "nameFiles": res["assets"][0]["name"] }
        return releases
    
    def verrify_version(self):
        nameFiles = self.getUrlReleasesGithub()['nameFiles'].split(".")
        if "V"+ self.getVersion() != self.getUrlReleasesGithub()['name']:
           newVersion =  requests.get(self.getUrlReleasesGithub()["urlFiles"])
           with open(os.path.join(Path.home(), "Downloads", self.getUrlReleasesGithub()['nameFiles'] ), "wb") as f:
               f.write(newVersion.content)
               with zipfile.ZipFile(os.path.join(Path.home(), "Downloads", self.getUrlReleasesGithub()['nameFiles']), 'r') as zip_ref:
                zip_ref.extractall(os.path.join(Path.home(), "Downloads", self.getUrlReleasesGithub()['name']))
                os.system("start "+ os.path.join(Path.home(), "Downloads", self.getUrlReleasesGithub()['name'], nameFiles[0]))
                
    def check_version(self):
        filename = wget.download(self.getUrlReleasesGithub()["urlFiles"])
        filename
        
    def windows_bar_progress(self):
        self.progress = QProgressBar(self)
        self.progress.setRange(0, 100)
        self.btn = QPushButton("Download",self)
        self.btn.clicked.connect(self.download)
    
    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed) 