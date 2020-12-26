# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f_ventas.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import consultas


class Ui_ventas(object):
    db = "dbpyme.db"

    def busqueda(self):
        text = self.lineEdit.text()
        item = self.treeWidget.findItems(text, QtCore.Qt.MatchContains, 0)

    def carga_productos(self):

        # Limpia el treeview para cargar los datos nuevos
        self.treeWidget.clear()
        querry = "SELECT * FROM productos"
        datos = consultas.sql_querry(self, querry)
        rows = datos.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.treeWidget.setColumnCount(3)
            self.treeWidget.setHeaderLabels(["PRODUCTO", "PRECIO", "STOCK"])
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0, row[2])
            item.setText(1, str(row[3]))
            item.setText(2, str(row[4]))



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(641, 406)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/icons8-brief-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setText("")

        self.pushButton.clicked.connect(self.carga_productos)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagenes/icons8-reset-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagenes/icons8-add-property-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagenes/icons8-delete-document-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imagenes/icons8-edit-property-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 5, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 6)
        self.treeWidget_2 = QtWidgets.QTreeWidget(Form)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget_2, 2, 0, 1, 6)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Inconsolata Expanded Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.carga_productos()
        self.lineEdit.textChanged.connect(self.busqueda)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventas"))
        self.label.setText(_translate("Form", "Producto:"))
        self.label_2.setText(_translate("Form", "1000,43"))
