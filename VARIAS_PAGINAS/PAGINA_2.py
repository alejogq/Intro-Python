# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PAGINA_2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

"""
Algunos elementos fueront tomados de:
https://learndataanalysis.org/embed-matplotlib-graph-in-a-pyqt5-application/
https://www.delftstack.com/es/tutorial/pyqt5/pyqt-grid-layout/

"""


from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Canvas(FigureCanvas):
    
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(3, 2), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)
        
        self.ax.plot(t, s)

        self.ax.set(xlabel='Tiempo (s)', ylabel='voltaje (mV)',
               title='GRAFICO FIGURA DE MAT-PLOT')
        self.ax.grid()




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(272, 219)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 201, 121))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout.SetMinimumSize(10)
        
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton.clicked.connect(lambda: Form.close())
        
        dibujo = Canvas(Form)
        # self.gridLayout.addWidget(dibujo, 0, 1, 1, 1)
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PAGINA 2"))
        self.pushButton.setText(_translate("Form", "CERRAR"))

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Form=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())