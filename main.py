from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThread,pyqtSignal
import sys, cv2
import numpy as np

#7mc1Jeza^moufmev

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        ui = uic.loadUi('sesionLogin.ui',self)
        self.show()
        self.setWindowTitle('MyCounts')
        #Llamadas a los Widgets
        self.usuarioLogin = self.findChild(QtWidgets.QLineEdit, 'leUsuarioLogin')
        self.passwordLogin = self.findChild(QtWidgets.QLineEdit, 'lePasswordLogin')
        self.usuarioRegistrar = self.findChild(QtWidgets.QLineEdit, 'leUsuarioReg')
        self.passwordRegistrar = self.findChild(QtWidgets.QLineEdit, 'lePasswordRe')
        self.login = self.findChild(QtWidgets.QPushButton, 'pbLogin')
        self.registrar = self.findChild(QtWidgets.QPushButton, 'pbRegistrar')
        self.login.clicked.connect(self.ingresar)
        self.registrar.clicked.connect(self.registrarse)

    def ingresar(self):
        self.usuarioLogin = self.findChild(QtWidgets.QLineEdit, 'leUsuarioLogin')
        self.passwordLogin = self.findChild(QtWidgets.QLineEdit, 'lePasswordLogin')
        print('funciona si')
        #mandamos la informacion a revision con la BD
        #si no existe el usuario mandamos mensaje de que no se ah registrado ese usuario

        #si existe inicia sesion, crea un objeto de tipo Usuario y carga todos sus datos
        #lo logea



    def registrarse(self):
        self.usuarioRegistrar = self.findChild(QtWidgets.QLineEdit, 'leUsuarioReg')
        self.passwordRegistrar = self.findChild(QtWidgets.QLineEdit, 'lePasswordRe')
        print('funciona si dos')
        #revisamos si el usuario no existe

        #si no existe creamos uno
        #en caso contrario regresar un mensaje de que ya esta registrado


app = QtWidgets.QApplication(sys.argv)
windows = Ui()
app.exec_()

