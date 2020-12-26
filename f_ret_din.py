# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/f_retiro_dinero.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rdin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(342, 282)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/../imagenes/icon_qpyme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 5, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Retiro dinero"))
        self.label.setText(_translate("Form", "Motivo"))
        self.comboBox.setItemText(0, _translate("Form", "Limpieza"))
        self.comboBox.setItemText(1, _translate("Form", "Insumo"))
        self.comboBox.setItemText(2, _translate("Form", "Comida"))
        self.comboBox.setItemText(3, _translate("Form", "Pago 3ros."))
        self.comboBox.setItemText(4, _translate("Form", "Cuota"))
        self.comboBox.setItemText(5, _translate("Form", "Adelanto"))
        self.label_3.setText(_translate("Form", "Monto"))
        self.label_2.setText(_translate("Form", "Detalle"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))
        self.pushButton.setText(_translate("Form", "Aceptar"))
