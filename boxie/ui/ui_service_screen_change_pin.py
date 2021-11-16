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


class Ui_ServiceChangePin(object):
    def setupUi(self, MainWindow):
        
        buttons_style = """
        background-color: white;
        border-width: 3px;
        border-style: solid;
        border-radius: 50px;
        border-color: rgb(30, 205, 151);
        color: rgb(30, 205, 151);
        font-size: 30px;
        font-weight: bold;
        """
        
        blue_frame_label = """
        background-color: white;
        border-width: 3px;
        border-style: solid;
        border-radius: 25px;
        border-color: rgb(30, 205, 151);
        color: yellow;
        font-size: 30px;
        font-weight: bold;
        """
        
        self.label_style_not_ok = """
        font-weight: bold;
        color: rgb(30, 205, 151);
        """

        self.label_style_ok = """
        font-weight: bold;
        color: rgb(27, 177, 130);
        """        
        
        back_button_style = """
        background-color: white;
        border-width: 3px;
        border-style: solid;
        border-radius: 25px;
        border-color: rgb(30, 205, 151);
        color: rgb(30, 205, 151);
        font-size: 30px;
        font-weight: bold;
        """
        
        self.pwd_field_style = """
        background-color: white;
        border-width: 0px;
        border-style: none;
        color: rgb(30, 205, 151);
        font-size: 30px;
        font-weight: bold;
        """

        self.pwd_field_style_wrong_pwd = """
        background-color: white;
        border-width: 0px;
        border-style: none;
        color: red;
        font-size: 30px;
        font-weight: bold;
        """

        self.pwd_field_style_new_pwd_accepted = """
        background-color: transparent;
        border-width: 3px;
        border-style: solid;
        border-radius: 25px;
        border-color: rgb(30, 205, 151);
        color: rgb(30, 205, 151);
        font-size: 30px;
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
        self.changePinLabel = QtWidgets.QLabel(self.centralwidget)
        self.changePinLabel.setGeometry(QtCore.QRect(529, 20, 222, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.changePinLabel.setFont(font)
        self.changePinLabel.setStyleSheet("color: rgb(30, 205, 151)") 
        self.changePinLabel.setScaledContents(False)
        self.changePinLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.changePinLabel.setWordWrap(True)
        self.changePinLabel.setObjectName("changePinLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menu_pwd_field = QtWidgets.QLineEdit(self.centralwidget)
        self.menu_pwd_field.setGeometry(QtCore.QRect(440, 60, 400, 100))
        self.menu_pwd_field.setMaxLength(6)
        self.menu_pwd_field.setAlignment(Qt.AlignCenter)
        self.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.menu_pwd_field.setEnabled(False)
        self.menu_pwd_field.setStyleSheet(self.pwd_field_style)

        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.move(450, 170)
        self.button_1.resize(100,100)
        self.button_1.setText("1")
        self.button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_1.setStyleSheet(buttons_style) 

        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.move(590, 170)
        self.button_2.resize(100,100)
        self.button_2.setText("2")
        self.button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_2.setStyleSheet(buttons_style)        

        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.move(730, 170)
        self.button_3.resize(100,100)
        self.button_3.setText("3")
        self.button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_3.setStyleSheet(buttons_style)
        
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.move(450, 310)
        self.button_4.resize(100,100)
        self.button_4.setText("4")
        self.button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_4.setStyleSheet(buttons_style) 

        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.move(590, 310)
        self.button_5.resize(100,100)
        self.button_5.setText("5")
        self.button_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_5.setStyleSheet(buttons_style)        

        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.move(730, 310)
        self.button_6.resize(100,100)
        self.button_6.setText("6")
        self.button_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_6.setStyleSheet(buttons_style)
        
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.move(450, 450)
        self.button_7.resize(100,100)
        self.button_7.setText("7")
        self.button_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_7.setStyleSheet(buttons_style) 

        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.move(590, 450)
        self.button_8.resize(100,100)
        self.button_8.setText("8")
        self.button_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_8.setStyleSheet(buttons_style)        

        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.move(730, 450)
        self.button_9.resize(100,100)
        self.button_9.setText("9")
        self.button_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_9.setStyleSheet(buttons_style)

        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.move(590, 590)
        self.button_0.resize(100,100)
        self.button_0.setText("0")
        self.button_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_0.setStyleSheet(buttons_style)
        
        self.button_del = QtWidgets.QPushButton(self.centralwidget)
        self.button_del.move(450, 590)
        self.button_del.resize(100,100)
        self.button_del.setText("del")
        self.button_del.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_del.setStyleSheet(buttons_style)
        
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.move(730, 590)
        self.button_ok.resize(100,100)
        self.button_ok.setText("ok")
        self.button_ok.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_ok.setStyleSheet(buttons_style) 

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setText("< Back")
        self.backButton.move(50, 50) 
        self.backButton.resize(200, 60) 
        self.backButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backButton.setStyleSheet(back_button_style)

        self.wframe = QtWidgets.QLabel(self.centralwidget)
        self.wframe.setStyleSheet(blue_frame_label)
        self.wframe.move(50,150)
        self.wframe.resize(300,142)

        self.fontSize = 18
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText('1. Enter current PIN')
        self.label.setStyleSheet(self.label_style_not_ok)
        self.label.move(75,160)
        self.label.resize(350,40)
        self.label.setFont(QtGui.QFont("Arial", self.fontSize))
        
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setText('2. Enter new PIN')
        self.label2.setStyleSheet(self.label_style_not_ok)
        self.label2.move(75,200)
        self.label2.resize(350,40)
        self.label2.setFont(QtGui.QFont("Arial", self.fontSize))
        
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setText('3. Enter new PIN again')
        self.label3.setStyleSheet(self.label_style_not_ok)
        self.label3.move(75,240)
        self.label3.resize(350,40)
        self.label3.setFont(QtGui.QFont("Arial", self.fontSize))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.changePinLabel.setText(_translate("MainWindow", "CHANGE PIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ServiceChangePin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
