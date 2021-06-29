"""
    Formulario de ejemplo cargando un .ui 
"""
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import sys
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Formulario(QMainWindow):
    def __init__(self,path) -> None:
        super().__init__()
        uic.loadUi(path,self)
        self.btnSaludar.clicked.connect(self.saludar)
    def saludar(self):
        name = self.txtNombre.text()
        surname = self.txtApellido.text()
        #saludo = '<html><head/><body><p align="center"><span style=" font-size:14pt; color:#aa00ff;">{} {}</span></p></body></html>'.format(name,surname)
        saludo = "Bienvenido {} {}".format(name,surname)
        self.lblSaludo.setText(saludo)

if __name__ == "__main__":
    filename = 'componentes.ui'
    path = os.path.join(BASE_DIR,filename)
    print(path)
    miApp = QApplication(sys.argv)
    miVentana = Formulario(path)
    miVentana.show()
    miApp.exec_()