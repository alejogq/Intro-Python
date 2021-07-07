# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:11:32 2021

@author: alejo
"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import sys
from ventana import *


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("ventana.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()



# class miventana(QtWidgets.QMainWindow):
    
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.ui=Ui_MainWindow()
#         self.ui.setupUi(self)     
        
#         ## Se conecta el boton a una señal para cuando se le dé un click
#         ## y se le asigna el método a realizar.
#         self.ui.pushButton_2.clicked.connect(self.mostrarMensaje)
        
#     def mostrarMensaje(self):
#         ## textEdit recibe un texto enriquecido, entonces es necesario ponerle 
#         ##el tipo de conversión. En este caso texto plano.
#         hola=self.ui.textEdit.toPlainText()
      
#         # hola="holaas"
#         self.ui.label.setText(hola)

# if __name__=="__main__":
#     aplicacion=QApplication([])
#     miaplicacion=miventana()
#     miaplicacion.show()
#     sys.exit(aplicacion.exec())