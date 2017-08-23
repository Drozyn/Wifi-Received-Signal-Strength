# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
# Author: Mateusz Drozynski
from PyQt4 import QtCore, QtGui
from win32wifi import Win32Wifi
import time
import sys
import datetime


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#KLASA DO OBSŁUGI GUI
class Ui_Quit(QtCore.QObject):
    def setupUi(self, Quit):
        # self.threadclass = Pomiar(1, 2)
        # self.pomiarThread=QtCore.QThread()
        # self.threadclass.moveToThread(self.pomiarThread)
        # self.pomiarThread.start()




        #DEKLARACJA ELEMENTÓW GUI
        Quit.setObjectName(_fromUtf8("Quit"))
        Quit.resize(402, 332)
        self.centralwidget = QtGui.QWidget(Quit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Zakoncz = QtGui.QPushButton(self.centralwidget)
        self.Zakoncz.setGeometry(QtCore.QRect(300, 290, 75, 23))
        self.Zakoncz.setObjectName(_fromUtf8("Zakoncz"))
        self.mierz = QtGui.QPushButton(self.centralwidget)
        self.mierz.setGeometry(QtCore.QRect(210, 290, 75, 23))
        self.mierz.setObjectName(_fromUtf8("mierz"))
        self.iteracje = QtGui.QTextEdit(self.centralwidget)
        self.iteracje.setGeometry(QtCore.QRect(260, 30, 113, 20))
        self.iteracje.setObjectName(_fromUtf8("iteracje"))
        self.stanowisko = QtGui.QTextEdit(self.centralwidget)
        self.stanowisko.setGeometry(QtCore.QRect(260, 70, 113, 20))
        self.stanowisko.setObjectName(_fromUtf8("stanowisko"))
        self.x = QtGui.QTextEdit(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(260, 140, 50, 20))
        self.x.setObjectName(_fromUtf8("x"))
        self.y = QtGui.QTextEdit(self.centralwidget)
        self.y.setGeometry(QtCore.QRect(320, 140, 50, 20))
        self.y.setObjectName(_fromUtf8("y"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 50, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 250, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_x = QtGui.QLabel(self.centralwidget)
        self.label_x.setGeometry(QtCore.QRect(275, 110, 101, 16))
        self.label_x.setObjectName(_fromUtf8("label_x"))
        self.label_y = QtGui.QLabel(self.centralwidget)
        self.label_y.setGeometry(QtCore.QRect(335, 110, 101, 16))
        self.label_y.setObjectName(_fromUtf8("label_y"))
        self.dostepne = QtGui.QScrollArea(self.centralwidget)
        self.dostepne.setGeometry(QtCore.QRect(10, 10, 231, 261))
        self.dostepne.setWidgetResizable(True)
        self.dostepne.setObjectName(_fromUtf8("dostepne"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 229, 259))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.dostepne.setWidget(self.scrollAreaWidgetContents)
        self.dostepne = QtGui.QListWidget(self.centralwidget)
        self.dostepne.setGeometry(QtCore.QRect(10, 10, 221, 251))
        self.dostepne.setObjectName(_fromUtf8("dostepne"))
        Quit.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Quit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Quit.setStatusBar(self.statusbar)
        self.retranslateUi(Quit)
        self.watekDostepne = DostepneWifi(self.dostepne)
        self.watekDostepne.start()

        #OBSŁUGA SLOTÓW PRZYCISKÓW ODPOWIEDZIALNYCH ZA ROZPOCZĘCIE POMIARU I ZAMKNIĘCIE OKNA
        QtCore.QObject.connect(self.Zakoncz, QtCore.SIGNAL(_fromUtf8("clicked()")), Quit.close)
        QtCore.QObject.connect(self.mierz, QtCore.SIGNAL(_fromUtf8("clicked()")), self.zacznij) #Przejscie do metody "zacznij"
        QtCore.QMetaObject.connectSlotsByName(Quit)





    #FUNKCJE STWORZONA PRZEZ DESIGNERA
    def retranslateUi(self, Quit):
        Quit.setWindowTitle(_translate("Quit", "MainWindow", None))
        self.Zakoncz.setText(_translate("Quit", "Zakończ", None))
        self.mierz.setText(_translate("Quit", "Pomiar", None))
        self.label.setText(_translate("Quit", "Podaj liczbę iteracji", None))
        self.label_2.setText(_translate("Quit", "Podaj numer stanowiska", None))
        self.label_3.setText(_translate("Quit", "Gotowy", None))
        self.label_x.setText(_translate("Quit", "x", None))
        self.label_y.setText(_translate("Quit", "y", None))
    def zacznij(self):
        #POBRANIE DANYCH DO ZMIENNYCH
        numer_stanowiska= int(self.stanowisko.toPlainText())
        iteracje=int(self.iteracje.toPlainText())
        x = float(self.x.toPlainText())
        y = float(self.y.toPlainText())



        #AKTUALIZACJA LABELKI O STATUSIE
        self.label_3.setText(_translate("Quit", "Wykonuje pomiar", None))


        self.klasawatku = Pomiar(numer_stanowiska,iteracje, self.label_3,x, y)
        self.klasawatku.start()



class Pomiar(QtCore.QThread):
    def __init__(self, numer_stanowiska, iteracje, label_3, x, y):
        QtCore.QThread.__init__(self)
        self.numer_stanowiska=numer_stanowiska
        self.iteracje=iteracje
        self.label_3 = label_3
        self.x = x
        self.y = y


    def run(self):
        plik = open('dane.txt', 'a')
        plik.writelines("Stanowisko nr " + str(self.numer_stanowiska)+"\n")
        plik.writelines("x:"+str(self.x)+" y:"+str(self.y)+"\n")
        for i in range(1, self.iteracje+1):
            plik.writelines(
                "Czas: " + str(datetime.datetime.today().year) + "-" + str(datetime.datetime.today().month) + "-" + str(
                    datetime.datetime.today().day) + " " + str(datetime.datetime.today().hour) + ":" + str(
                    datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second) + "\n")
            plik.writelines("Iteracja nr " + str(i) +"\n")
            ifaces = Win32Wifi.getWirelessInterfaces()
            for iface in ifaces:
                guid = iface.guid
                bsss = Win32Wifi.getWirelessNetworkBssList(iface)
                wyniki = [["None"] * 2 for i in range(len(bsss))]
                for j in range(0, len(bsss)):
                    wyniki[j][0] = bsss[j].bssid
                    wyniki[j][1] = bsss[j].link_quality
                    plik.writelines("MAC: "+str(wyniki[j][0])+"\n")
                    plik.writelines("Link Quality: " + str(wyniki[j][1]) + "\n")
                time.sleep(1)
        plik.close()
        self.label_3.setText(_translate("Quit","Gotowy", None))


class DostepneWifi(QtCore.QThread):
    def __init__(self, dostepne):
        QtCore.QThread.__init__(self)
        self.dostepne = dostepne
    def run(self):
        while True:
            self.dostepne.clear()
            ifaces = Win32Wifi.getWirelessInterfaces()
            for iface in ifaces:
                guid = iface.guid
                bsss = Win32Wifi.getWirelessNetworkBssList(iface)
                wyniki = [["None"] * 2 for i in range(len(bsss))]
                for j in range(0, len(bsss)):
                    wyniki[j][0] = bsss[j].bssid
                    wyniki[j][1] = bsss[j].link_quality
                    self.dostepne.addItem(str("MAC: " +wyniki[j][0]))
                    self.dostepne.addItem(str("Quality: " + str(bsss[j].link_quality)))
                time.sleep(1)

#KLASA TWORZONA PRZEZ DESIGNERA
class Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.ui = Ui_Quit()
        self.ui.setupUi(self)


app = QtGui.QApplication(sys.argv)
myapp = Form()
myapp.show()
sys.exit(app.exec_())
