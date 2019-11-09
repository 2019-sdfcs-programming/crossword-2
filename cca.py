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
        self.B2.clicked.connect(self.b2)
        self.B7.clicked.connect(self.b7)
        self.B3.clicked.connect(self.b3)
        self.B8.clicked.connect(self.b8)
        self.B4.clicked.connect(self.b4)
        self.B9.clicked.connect(self.b9)
        self.B5.clicked.connect(self.b5)
        self.B10.clicked.connect(self.b10)
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
        elif K =='등차중항' and self.now == 2:
            self.A4.setPlainText('등')
            self.A8.setPlainText('차')
            self.A10.setPlainText('중')
            self.A12.setPlainText('항')
        elif K =='항상성과호르몬' and self.now == 3:
            self.A12.setPlainText('항')
            self.A13.setPlainText('상')
            self.A14.setPlainText('성')
            self.A15.setPlainText('과')
            self.A16.setPlainText('호')
            self.A17.setPlainText('르')
            self.A18.setPlainText('몬')
        elif K =='성관계' and self.now == 4:
            self.A14.setPlainText('성')
            self.A19.setPlainText('관')
            self.A25.setPlainText('계')

        elif K =='관성좌표계' and self.now == 5:
            self.A21.setPlainText('관')
            self.A22.setPlainText('성')
            self.A23.setPlainText('좌')
            self.A24.setPlainText('표')
            self.A25.setPlainText('계')

        elif K =='표창장' and self.now == 6:
            self.A24.setPlainText('표')
            self.A27.setPlainText('창')
            self.A29.setPlainText('장')

        elif K =='장지연' and self.now == 7:
            self.A29.setPlainText('장')
            self.A30.setPlainText('지')
            self.A31.setPlainText('연')

        elif K =='르네상스' and self.now == 8:
            self.A17.setPlainText('르')
            self.A20.setPlainText('네')
            self.A26.setPlainText('상')
            self.A28.setPlainText('스')

        elif K =='스누피' and self.now == 9:
            self.A28.setPlainText('스')
            self.A33.setPlainText('누')
            self.A34.setPlainText('피')

        elif K =='성호르몬' and self.now == 10:
            self.A7.setPlainText('성')
            self.A9.setPlainText('호')
            self.A11.setPlainText('르')
            self.A18.setPlainText('몬')

    def b1(self):
        self.now = 1
        self.initDisplay()
        self.T1.setPlainText('우리학교이름은?')

    def b6(self):
        self.now = 2
        self.initDisplay()
        self.T1.setPlainText('연속한 세 항 중에서 가운데 항, 두 수의 평균에 해당하는 값')

    def b2(self):
        self.now = 3
        self.initDisplay()
        self.T1.setPlainText('생명과학 : ㅎㅅㅅㄱ ㅎㄹㅁ')

    def b7(self):
        self.now = 4
        self.initDisplay()
        self.T1.setPlainText('sex')

    def b3(self):
        self.now = 5
        self.initDisplay()
        self.T1.setPlainText('고전 역학에서 뉴턴의 운동법칙 중 제1법칙이 성립하는 좌표계')

    def b8(self):
        self.now = 6
        self.initDisplay()
        self.T1.setPlainText('특정 성과나 행실에 대해 상을 수여하는 내용의 문서')

    def b4(self):
        self.now = 7
        self.initDisplay()
        self.T1.setPlainText('김건모 아내의 이름은?')

    def b9(self):
        self.now = 8
        self.initDisplay()
        self.T1.setPlainText('14∼16세기에 서유럽 문명사에 나타난 문화운동')

    def b5(self):
        self.now = 9
        self.initDisplay()
        self.T1.setPlainText('만화가 찰스 슐츠가의 만화. 주인공인 찰리 브라운의 애완동물이다.')

    def b10(self):
        self.now = 10
        self.initDisplay()
        self.T1.setPlainText('XX, XY')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()