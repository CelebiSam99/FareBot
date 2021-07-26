import pyautogui
from PyQt5 import QtWidgets
import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon
import time

class MainFrom(QMainWindow):
    def __init__(self):
        super(MainFrom, self).__init__()

        self.setWindowTitle("Fare Botu")
        self.setWindowIcon(QIcon("un.png"))
        self.setGeometry(100,100,250,200)
        self.initUI()

    def initUI(self):

        self.btn_topla=QtWidgets.QPushButton(self)
        self.btn_topla.setText("Botu Başlat")
        self.btn_topla.move(50,50)
        self.btn_topla.clicked.connect(self.bot)

        self.btn_cıkar=QtWidgets.QPushButton(self)
        self.btn_cıkar.setText("Botu Durdur")
        self.btn_cıkar.move(50,100)
        self.btn_cıkar.clicked.connect(self.bot)


    def bot(self):
        sender =self.sender().text()
        result = 0  
        if sender == "Botu Başlat":
            while True:
                pyautogui.moveRel(0,50,duration=1)
                pyautogui.moveRel(0,-50,duration=0)

        elif sender == "Botu Durdur":
                  sys.exit(app.exec_())
            

def app():
    app = QApplication(sys.argv)
    win = MainFrom()
    win.show()
    sys.exit(app.exec_())

app()

