# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f_usuarios.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import consultas
import sys


class Ui_usuarios(object):
    db = "dbpyme.db"

    def carga_datos(self):
        # Limpia el treeview para cargar los datos nuevos
        self.treeWidget.clear()
        querry = "SELECT * FROM usuarios"
        datos = consultas.sql_querry(self, querry)
        rows = datos.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.treeWidget.setColumnCount(2)

            self.treeWidget.setHeaderLabels(["USUARIO", "PASE"])
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0, row[1])
            item.setText(1, str(row[3]))

    def seleccion(self):
        item = self.treeWidget.currentItem()
        # print(item.text(0))
        querry = f"SELECT * FROM usuarios WHERE username='{item.text(0)}'"
        datos = consultas.sql_querry(self, querry)
        rows = datos.fetchall()
        for i in rows:
            self.lineEdit.setText(i[1])
            self.lineEdit_2.setText(i[2])

    def salir(self):
        pass

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(538, 318)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 8)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 2)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 7, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 6, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.carga_datos()

        self.treeWidget.doubleClicked.connect(self.seleccion)

        self.pushButton_4.clicked.connect(self.salir)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Usuarios"))
        self.label.setText(_translate("Form", "Nombre:"))
        self.label_2.setText(_translate("Form", "Contraseña:"))
        self.label_3.setText(_translate("Form", "Permisos:"))
        self.comboBox.setItemText(0, _translate("Form", "0"))
        self.comboBox.setItemText(1, _translate("Form", "1"))
        self.pushButton_4.setText(_translate("Form", "Cerrar"))
        self.pushButton_2.setText(_translate("Form", "Modificar"))
        self.pushButton_3.setText(_translate("Form", "Eliminar"))
        self.pushButton.setText(_translate("Form", "Agregar"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = Ui_usuarios(dialog)
    dialog.show()
    sys.exit(app.exec())
