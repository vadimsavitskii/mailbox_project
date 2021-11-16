import sys, settings, mail_service, database

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLineEdit

from ui.ui_service_screen_login import Ui_ServiceLoginScreen
from ui.ui_service_screen_main_menu import Ui_ServiceMainScreen
from ui.ui_service_screen_change_pin import Ui_ServiceChangePin

class ServiceMenuLogin(QMainWindow):
    def __init__(self):
        super(ServiceMenuLogin, self).__init__()
        loadUi('/home/pi/BOXIE_study_project/ui/main_screen.ui', self)
        self.ui = Ui_ServiceLoginScreen()
        self.ui.setupUi(self)
        
        self.pwd_entry = ''
        settings.box_password = database.view_all_records()[0][0]
        
        self.ui.button_1.clicked.connect(self.button_1_clicked)
        self.ui.button_2.clicked.connect(self.button_2_clicked)
        self.ui.button_3.clicked.connect(self.button_3_clicked)
        self.ui.button_4.clicked.connect(self.button_4_clicked)
        self.ui.button_5.clicked.connect(self.button_5_clicked)
        self.ui.button_6.clicked.connect(self.button_6_clicked)
        self.ui.button_7.clicked.connect(self.button_7_clicked)
        self.ui.button_8.clicked.connect(self.button_8_clicked)
        self.ui.button_9.clicked.connect(self.button_9_clicked)
        self.ui.button_0.clicked.connect(self.button_0_clicked)
        self.ui.button_ok.clicked.connect(self.button_ok_clicked)
        self.ui.button_del.clicked.connect(self.button_del_clicked)
        
    def button_del_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry = self.pwd_entry[:-1]
        self.ui.menu_pwd_field.setText(self.pwd_entry)

    def button_ok_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style) 
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
                
        self.ui.menu_pwd_field.setText(self.pwd_entry)
        if self.pwd_entry == settings.box_password:
            go_to_serv_menu = ServiceMenu()
            widget.addWidget(go_to_serv_menu)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style_wrong_pwd)
            self.pwd_entry = ''
            self.ui.menu_pwd_field.setText(self.pwd_entry)
            self.ui.menu_pwd_field.setMaxLength(14)
            self.ui.menu_pwd_field.setEchoMode(QLineEdit.Normal)
            self.ui.menu_pwd_field.setText('wrong password')


    def button_0_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '0'
        self.ui.menu_pwd_field.setText(self.pwd_entry)
        
    def button_1_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '1'
        self.ui.menu_pwd_field.setText(self.pwd_entry)
        
    def button_2_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '2'
        self.ui.menu_pwd_field.setText(self.pwd_entry)
        
    def button_3_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '3'
        self.ui.menu_pwd_field.setText(self.pwd_entry)

    def button_4_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '4'
        self.ui.menu_pwd_field.setText(self.pwd_entry)
        
    def button_5_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '5'
        self.ui.menu_pwd_field.setText(self.pwd_entry)
        
    def button_6_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '6'
        self.ui.menu_pwd_field.setText(self.pwd_entry)
      
    def button_7_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '7'
        self.ui.menu_pwd_field.setText(self.pwd_entry)

    def button_8_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '8'
        self.ui.menu_pwd_field.setText(self.pwd_entry)

    def button_9_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.pwd_entry += '9'
        self.ui.menu_pwd_field.setText(self.pwd_entry)


class ServiceMenu(QMainWindow):
    def __init__(self):
        super(ServiceMenu, self).__init__()
        loadUi('/home/pi/BOXIE_study_project/ui/main_screen.ui', self)
        self.ui = Ui_ServiceMainScreen()
        self.ui.setupUi(self)
        
        settings.box_password
        
        self.ui.box_unlocked_label.hide()
        self.ui.box_unlocked_text.hide()
        self.ui.button_ok.hide()
        
        self.ui.button_change_pin.clicked.connect(self.change_pin_button_clicked)
        self.ui.button_unlock.clicked.connect(self.unlock_button_clicked)
        self.ui.button_exit.clicked.connect(self.exit_button_clicked)
        self.ui.button_ok.clicked.connect(self.ok_button_clicked)
        
    def exit_button_clicked(self):
        go_to_login = ServiceMenuLogin()
        widget.addWidget(go_to_login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def change_pin_button_clicked(self):
        go_to_change_pin = ServiceChangePin()
        widget.addWidget(go_to_change_pin)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def unlock_button_clicked(self):
        self.ui.box_unlocked_label.show()
        self.ui.box_unlocked_text.show()
        self.ui.button_ok.show()
        self.ui.button_exit.hide()
        self.ui.button_unlock.hide()
        self.ui.button_change_pin.hide()
        mail_service.send_security_message_box_unlocked()
    
    def ok_button_clicked(self):
        self.ui.box_unlocked_label.hide()
        self.ui.box_unlocked_text.hide()
        self.ui.button_ok.hide()  
        self.ui.button_exit.show()
        self.ui.button_unlock.show()
        self.ui.button_change_pin.show()


class ServiceChangePin(QMainWindow):
    def __init__(self):
        super(ServiceChangePin, self).__init__()
        loadUi('/home/pi/BOXIE_study_project/ui/main_screen.ui', self)
        self.ui = Ui_ServiceChangePin()
        self.ui.setupUi(self)
                
        self.ui.button_1.clicked.connect(self.button_1_clicked)
        self.ui.button_2.clicked.connect(self.button_2_clicked)
        self.ui.button_3.clicked.connect(self.button_3_clicked)
        self.ui.button_4.clicked.connect(self.button_4_clicked)
        self.ui.button_5.clicked.connect(self.button_5_clicked)
        self.ui.button_6.clicked.connect(self.button_6_clicked)
        self.ui.button_7.clicked.connect(self.button_7_clicked)
        self.ui.button_8.clicked.connect(self.button_8_clicked)
        self.ui.button_9.clicked.connect(self.button_9_clicked)
        self.ui.button_0.clicked.connect(self.button_0_clicked)
        self.ui.button_ok.clicked.connect(self.button_ok_clicked)
        self.ui.button_del.clicked.connect(self.button_del_clicked)
        self.ui.backButton.clicked.connect(self.back_button_clicked)
        
        self.pwd_entry = ''
        self.new_pwd_entry = ''
        self.new_pwd_entry_again = ''

        self.ui.menu_pwd_field.setText(self.pwd_entry)

        settings.box_password = database.view_all_records()[0][0]

        print('box_pwd: ' + settings.box_password)

        print('current: ' + self.pwd_entry)
        print('new pwd: ' + self.new_pwd_entry)
        print('new pwd again: ' + self.new_pwd_entry_again)

    def back_button_clicked(self):
        self.pwd_entry = ''
        self.new_pwd_entry = ''
        self.new_pwd_entry_again = ''
        
        settings.current_psw_ok = False
        settings.new_psw_ok = False
        settings.new_psw_again_ok = False
        
        self.ui.menu_pwd_field.setText(self.pwd_entry)

        go_back = ServiceMenu()
        widget.addWidget(go_back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def button_del_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)

        if not settings.current_psw_ok:
            self.pwd_entry = self.pwd_entry[:-1]
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry = self.new_pwd_entry[:-1]
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again = self.new_pwd_entry_again[:-1]
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)

    def button_ok_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        self.ui.menu_pwd_field.setText(self.pwd_entry)
        
        print('Password is: ' + settings.box_password)
        print(self.pwd_entry)
        

        if self.pwd_entry == settings.box_password:
            settings.current_psw_ok = True
            settings.new_psw_ok = True
            print('Current Password: OK')
            self.ui.label.setStyleSheet(self.ui.label_style_ok)
            
            print('current: ' + self.pwd_entry)

            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
            print('new pwd: ' + self.new_pwd_entry)
            print('new pwd again: ' + self.new_pwd_entry_again)
            
            if len(self.new_pwd_entry) > 6:
                self.new_pwd_entry = ''
                self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style_wrong_pwd)
                self.ui.menu_pwd_field.setEchoMode(QLineEdit.Normal)
                self.ui.menu_pwd_field.setMaxLength(25)
                self.ui.menu_pwd_field.setText('Max size is 6 digits')
                
            if len(self.new_pwd_entry) < 4 and len(self.new_pwd_entry) > 0:
                self.new_pwd_entry = ''
                self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style_wrong_pwd)
                self.ui.menu_pwd_field.setEchoMode(QLineEdit.Normal)
                self.ui.menu_pwd_field.setMaxLength(25)
                self.ui.menu_pwd_field.setText('Min size is 4 digits')
            
            if len(self.new_pwd_entry) > 3 and len(self.new_pwd_entry) < 7:  
                settings.new_psw_ok = False
                settings.new_psw_again_ok = True
                self.ui.label2.setStyleSheet(self.ui.label_style_ok)
                self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
                
                if self.new_pwd_entry == self.new_pwd_entry_again:
                    self.ui.label3.setStyleSheet(self.ui.label_style_ok)
                    database.update_entry(self.pwd_entry, self.new_pwd_entry_again)
                    mail_service.send_security_message_pin_changed()

                    self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style_new_pwd_accepted)
                    self.pwd_entry = ''
                    self.new_pwd_entry = ''
                    self.new_pwd_entry_again = ''
                    
                    self.ui.button_0.hide()
                    self.ui.button_1.hide()
                    self.ui.button_2.hide()
                    self.ui.button_3.hide()
                    self.ui.button_4.hide()
                    self.ui.button_5.hide()
                    self.ui.button_6.hide()
                    self.ui.button_7.hide()
                    self.ui.button_8.hide()
                    self.ui.button_9.hide()
                    self.ui.button_ok.hide()
                    self.ui.button_del.hide()
                    
                    self.ui.menu_pwd_field.move(440,250)
                    self.ui.menu_pwd_field.resize(400,200)
                    self.ui.menu_pwd_field.setMaxLength(14)
                    self.ui.menu_pwd_field.setEchoMode(QLineEdit.Normal)
                    self.ui.menu_pwd_field.setText('PIN CHANGED')
                
                elif self.new_pwd_entry != self.new_pwd_entry_again and len(self.new_pwd_entry_again) > 0:
                    self.new_pwd_entry_again = ''
                    self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style_wrong_pwd)
                    self.ui.menu_pwd_field.setEchoMode(QLineEdit.Normal)
                    self.ui.menu_pwd_field.setMaxLength(25)
                    self.ui.menu_pwd_field.setText("New PINs don't match")
            
        else:
            self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style_wrong_pwd)
            self.pwd_entry = ''
            self.ui.menu_pwd_field.setText(self.pwd_entry)
            self.ui.menu_pwd_field.setMaxLength(14)
            self.ui.menu_pwd_field.setEchoMode(QLineEdit.Normal)
            self.ui.menu_pwd_field.setText('wrong password')


    def button_0_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '0'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '0'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '0'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)


    def button_1_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '1'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '1'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '1'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
            
    def button_2_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '2'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '2'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '2'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
            
    def button_3_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '3'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '3'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '3'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
            
    def button_4_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '4'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '4'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '4'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
        
    def button_5_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '5'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '5'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '5'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
            
    def button_6_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '6'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '6'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '6'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
      
    def button_7_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '7'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '7'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '7'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
            
    def button_8_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '8'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '8'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '8'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)
            
    def button_9_clicked(self):
        self.ui.menu_pwd_field.setStyleSheet(self.ui.pwd_field_style)
        self.ui.menu_pwd_field.setEchoMode(QLineEdit.Password)
        self.ui.menu_pwd_field.setMaxLength(6)
        if not settings.current_psw_ok:
            self.pwd_entry += '9'
            self.ui.menu_pwd_field.setText(self.pwd_entry)
        if settings.new_psw_ok:
            self.new_pwd_entry += '9'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry)
        if settings.new_psw_again_ok:
            self.new_pwd_entry_again += '9'
            self.ui.menu_pwd_field.setText(self.new_pwd_entry_again)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    
    start_window = ServiceMenuLogin()
    widget.addWidget(start_window)
    
    widget.setFixedWidth(1280)
    widget.setFixedHeight(720)
    widget.setWindowFlags(Qt.FramelessWindowHint)

    widget.show()
    
    try:
        sys.exit(app.exec())
    except Exception as e:
        print(e)
