import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QLabel, QGridLayout)

try:
    from .airport import aiport
except:
    from airport import aiport


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Metar Information")
        # Create widgets
        try:
            self.edit = QLineEdit("LFBL")
        except:
            self.edit = QLineEdit("LFBL")
        #self.edit = QLineEdit("LFBL")
        self.button = QPushButton("Show Metar")
        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.grid = QGridLayout()
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(self.layout)
        
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)
        
        

    # Greets the user
    def greetings(self):
        a = aiport(self.edit.text())
        b = a.metar()
        c = a.taf()
        r = a.runways()
               
        self.rules = QLabel(f"Rule: ")
        if b["rules"] == "VFR":
            self.rule = QLabel(f"{b[str('rules')]}")
            self.rule.setMaximumWidth(30)
            self.rule.setStyleSheet("background-color: green; color: white; font-weight: bold; margin-left: 2px;")
        else:
            self.rule = QLabel(f"{b[str('rules')]}")
            self.rule.setMaximumWidth(30)
            self.rule.setStyleSheet("background-color: red; color: white; font-weight: bold; margin-left: 2px;")
        
        self.border = QLabel("<hr>")
        self.border.setStyleSheet("border-bottom-style: solid; grey")
          
        self.io = QLabel(f"Metar : {b[str('metar')]}")
        self.iT = QLabel(f"Taf : {c[str('taf')]}")
              
        if len(r) == 1:
            self.r = QLabel("Runways " + str(r[0][0]) +"-"+ str(r[0][1]))
        elif len(r) == 2:
            self.r = QLabel("Runways " + str(r[0][0]) +"-"+ str(r[0][1]) + " / "+str(r[1][0]) +"-"+ str(r[1][1]) )
        elif len(r) == 3:
            self.r = QLabel("Runways " + str(r[0][0]) +"-"+ str(r[0][1]) + " / "+str(r[1][0]) +"-"+ str(r[1][1]) + " / "+str(r[2][0]) +"-"+ str(r[2][1]) )
        elif len(r) == 4:
            self.r = QLabel("Runways " + str(r[0][0]) +"-"+ str(r[0][1]) + " / "+str(r[1][0]) +"-"+ str(r[1][1]) + " / "+str(r[2][0]) +"-"+ str(r[2][1]) +  " / "+str(r[3][0]) +"-"+ str(r[3][1]))
        elif len(r) == 5:
            self.r = QLabel("Runways " + str(r[0][0]) +"-"+ str(r[0][1]) + " / "+str(r[1][0]) +"-"+ str(r[1][1]) + " / "+str(r[2][0]) +"-"+ str(r[2][1]) +  " / "+str(r[3][0]) +"-"+ str(r[3][1]) +  " / "+str(r[4][0]) +"-"+ str(r[4][1]))
        else:
            self.r = QLabel("No Information Runways")
        
        self.layout.addLayout(self.grid)
        #self.grid.addWidget(self.rules, 0,1,0,1)
        self.grid.addWidget(self.rule, 0,1,0,1)
        self.grid.addWidget(self.r, 0,3,0,3)
        self.layout.addWidget(self.io)
        self.layout.addWidget(self.iT)
        self.layout.addWidget(self.border)
        

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())