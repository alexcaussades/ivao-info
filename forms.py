from PySide6.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, \
    QVBoxLayout, QPushButton, QGridLayout, QLabel


class mainWindows(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sim IVAO Info Serv")
        self.setWindowOpacity(1)

        main_layout = QHBoxLayout(self)
        # button = QPushButton("t")
        # main_layout.addWidget(button)

        left_layout = QVBoxLayout()
        rigth_layout = QVBoxLayout()
        midlle_l = QHBoxLayout()
        
        btn = QPushButton("hello")
        midlle_l.addWidget(btn)
        
        
        main_layout.addLayout(left_layout)
        main_layout.addLayout(midlle_l)
        main_layout.addLayout(rigth_layout)
        
        for i in range(1, 11):
            btn = QPushButton(str(i))
            left_layout.addWidget(btn)
        
        for i in range(1, 11):
            btn = QPushButton(str(i))
            rigth_layout.addWidget(btn)
        
app = QApplication()

main_windows = mainWindows()
main_windows.show()
app.exec()
