import sys

from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QWidget, QLabel, QGridLayout, QTableWidget, QTableWidgetItem)

from threading import Timer
import requests

from test2 import getATC, getPilot, getPilotDepartureAirport, getPilotArrivalAirport

url = "https://api.ivao.aero/v2/tracker/whazzup"

r = requests.get(url)
atc = r.json()

x = atc["clients"]["atcs"]
p = atc["clients"]["pilots"]

class Online(QWidget):
    
        def __init__(self, vid,  parent=None):
            super(Online, self).__init__(parent)
            self.vid = vid
            self.setWindowTitle("Online Information")
            rr = getPilotDepartureAirport("LSZH")
            print(len(rr))
            # Create widgets                        
            self.layout = QWidget()
            self.vertical = QVBoxLayout()
            self.tabletEvent = QTableWidget(5, 6)
            self.setLayout(self.vertical)
            self.vertical.addWidget(QLabel(f"VID: {self.vid}"))
            self.vertical.addWidget(QLabel(f"Callsign: {rr[5]}"))
            self.vertical.addWidget(self.tabletEvent)
            self.tabletEvent.setHorizontalHeaderLabels(["Callsign", "Departure", "Alternative", "Route", "Level", "Flight Rules"])
            self.tabletEvent.setVerticalHeaderLabels(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"])
            self.tabletEvent.setItem(0, 0, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['callsign']}"))
            self.tabletEvent.setItem(0, 1, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['departureId']}"))
            self.tabletEvent.setItem(0, 2, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['alternativeId']}"))
            self.tabletEvent.setItem(0, 3, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['route']}"))
            self.tabletEvent.setItem(0, 4, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['level']}"))
            self.tabletEvent.setItem(0, 5, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['flightRules']}"))
            self.tabletEvent.setItem(1, 0, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['callsign']}"))
            self.tabletEvent.setItem(1, 1, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['departureId']}"))
            self.tabletEvent.setItem(1, 2, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['alternativeId']}"))
            self.tabletEvent.setItem(1, 3, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['route']}"))
            self.tabletEvent.setItem(1, 4, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['level']}"))
            self.tabletEvent.setItem(1, 5, QTableWidgetItem(f"{getPilotDepartureAirport('LSZH')['flightRules']}"))
            
            
        
        
        
            
            
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Online(620362)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())           
