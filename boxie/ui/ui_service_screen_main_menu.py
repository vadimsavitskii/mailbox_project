# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


class Ui_ServiceMainScreen(object):
    def setupUi(self, MainWindow):
        
        buttons_style = """
        background-color: white;
        border-width: 3px;
        border-style: solid;
        border-radius: 25px;
        border-color: rgb(30, 205, 151);
        color: rgb(30, 205, 151);
        font-size: 30px;
        font-weight: bold;
        """
        
        unlocked_text_style = """
        background-color: transparent;
        color: rgb(30, 205, 151);
        font-size: 24px;
        font-weight: bold;
        """
                
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.bg.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.bg.setObjectName("bg")
        self.serviceMenuLabel = QtWidgets.QLabel(self.centralwidget)
        self.serviceMenuLabel.setGeometry(QtCore.QRect(529, 20, 222, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.serviceMenuLabel.setFont(font)
        self.serviceMenuLabel.setStyleSheet("color: rgb(30, 205, 151)") #color: rgb(30, 205, 151)
        self.serviceMenuLabel.setScaledContents(False)
        self.serviceMenuLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.serviceMenuLabel.setWordWrap(True)
        self.serviceMenuLabel.setObjectName("serviceMenuLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.button_change_pin = QtWidgets.QPushButton(self.centralwidget)
        self.button_change_pin.move(390, 120)
        self.button_change_pin.resize(500,75)
        self.button_change_pin.setText("Change service menu PIN")
        self.button_change_pin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_change_pin.setStyleSheet(buttons_style)
        
        self.button_unlock = QtWidgets.QPushButton(self.centralwidget)
        self.button_unlock.move(390, 220)
        self.button_unlock.resize(500,75)
        self.button_unlock.setText("Unlock box")
        self.button_unlock.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_unlock.setStyleSheet(buttons_style)
        
        self.box_unlocked_label = QtWidgets.QLabel(self.centralwidget)
        self.box_unlocked_label.setStyleSheet(buttons_style)
        self.box_unlocked_label.move(440,200)
        self.box_unlocked_label.resize(400, 230)
        
        self.box_unlocked_text = QtWidgets.QLabel(self.centralwidget)
        self.box_unlocked_text.setStyleSheet(unlocked_text_style)
        self.box_unlocked_text.move(445,260)
        self.box_unlocked_text.resize(390, 50)
        self.box_unlocked_text.setScaledContents(False)
        self.box_unlocked_text.setAlignment(QtCore.Qt.AlignHCenter)
        self.box_unlocked_text.setWordWrap(True)
        self.box_unlocked_text.setText("The box has been unlocked!")
        
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setText("ok")
        self.button_ok.move(585, 350) 
        self.button_ok.resize(110, 50) 
        self.button_ok.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_ok.setStyleSheet(buttons_style)
        
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.move(390, 320)
        self.button_exit.resize(500,75)
        self.button_exit.setText("Exit")
        self.button_exit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_exit.setStyleSheet(buttons_style)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.serviceMenuLabel.setText(_translate("MainWindow", "Service menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ServiceMainScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
