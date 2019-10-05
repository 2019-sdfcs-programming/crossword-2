#-*- coding:utf-8 -*-

import sys
#PyQt must be installed.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('aa.ui')[0]

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.B1.clicked.connect(self.b1)
        self.B2.clicked.connect(self.b2)
        self.B3.clicked.connect(self.b3)
        self.B4.clicked.connect(self.b4)
        self.B5.clicked.connect(self.b5)
        self.B6.clicked.connect(self.b6)
        self.B7.clicked.connect(self.b7)
        self.B8.clicked.connect(self.b8)
        self.B9.clicked.connect(self.b9)
        self.B10.clicked.connect(self.b10)

    
    def b1(self):
        K = self.T2.toPlainText()
        self.T1.setPlainText('ㅎㅇ')
        if K =='숭덕고등학교':
            self.A1.setPlainText('숭')
            self.A2.setPlainText('덕')
            self.A3.setPlainText('고')
            self.A4.setPlainText('등')
            self.A5.setPlainText('학')
            self.A6.setPlainText('교'')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()