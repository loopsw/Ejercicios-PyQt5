"""
    Programa de ejemplo para cargar un .ui de QT Designer
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
        self.lblSaludo.setText("Hola mundo!")

if __name__ == "__main__":
    filename = 'formulario.ui'
    path = os.path.join(BASE_DIR,filename)
    print(path)
    miApp = QApplication(sys.argv)
    miVentana = Formulario(path)
    miVentana.show()
    miApp.exec_()