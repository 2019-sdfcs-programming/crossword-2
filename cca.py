#-*- coding:utf-8 -*-

import sys
#PyQt must be installed.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('qq.ui')[0]

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.B1.clicked.connect(self.b1)
        self.B6.clicked.connect(self.b6)
        self.P.clicked.connect(self.b11)
        now = 0

    def initDisplay(self):
        self.T2.setPlainText('')

    def b11(self):
        K = self.T2.toPlainText()
        if K =='숭덕고등학교' and self.now == 1:
            self.A1.setPlainText('숭')
            self.A2.setPlainText('덕')
            self.A3.setPlainText('고')
            self.A4.setPlainText('등')
            self.A5.setPlainText('학')
            self.A6.setPlainText('교')
        elif K =='등차수열' and self.now == 2:
            self.A4.setPlainText('등')
            self.A8.setPlainText('차')
            self.A10.setPlainText('수')
            self.A12.setPlainText('열')

    def b1(self):
        self.now = 1
        self.initDisplay()
        self.T1.setPlainText('우리학교이름은?')

    def b6(self):
        self.now = 2
        self.initDisplay()
        self.T1.setPlainText('등차수열')    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()