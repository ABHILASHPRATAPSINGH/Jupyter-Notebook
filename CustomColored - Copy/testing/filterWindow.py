# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class filterWindow(QMainWindow):

    def __init__(self,Parent):
        super(filterWindow, self).__init__(Parent)
        self.setupUi()


    def setupUi(self):
        MainWindow=self
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(421, 187)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 120, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 120, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 401, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(60, 10, 71, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 10, 91, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 51, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 50, 71, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(250, 10, 51, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 10, 16, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 10, 51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.lineEdit_2.setHidden(True)
        # self.label.setHidden(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "LTP"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Change(%)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Change Price"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Vol"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Delivery Vol"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Delivery(%)"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Market Cap"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Greater Than..."))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Less Than..."))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Between..."))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Equal To..."))
        self.label_2.setText(_translate("MainWindow", "Sort by"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "LTP"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Change(%)"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Change Price"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Vol"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Delivery Vol"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Delivery(%)"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Market Cap"))
        self.label.setText(_translate("MainWindow", "To"))
        self.label_3.setText(_translate("MainWindow", "Filter by"))



