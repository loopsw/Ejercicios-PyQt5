"""
    Ejemplo de visualización de una lista en QT
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
        #self.hiButton.clicked.connect(self.saludar)
        self.btnSalir.clicked.connect(self.salir)
        self.btnVisualizar.clicked.connect(self.visualizar)

    def cerrarWidget(self):
        self.dockWidget.close()

    def salir(self):
        self.close()
    def visualizar(self):
        self.listWidget.addItem("Python")
        self.listWidget.insertItem(1, "Java")
        self.listWidget.insertItem(2, "C++")
        self.listWidget.insertItem(3, "C#")
        self.listWidget.insertItem(4, "Ruby")
        self.listWidget.insertItem(5, "Kotlin")

if __name__ == "__main__":
    filename = 'cerrarVentana.ui'
    path = os.path.join(BASE_DIR,filename)
    print(path)
    miApp = QApplication(sys.argv)
    miVentana = Formulario(path)
    miVentana.show()
    miApp.exec_()