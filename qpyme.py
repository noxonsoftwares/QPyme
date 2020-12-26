import sys
from f_login import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import consultas


class Ventana(Ui_Form):
    # Nombre de la base de datos
    db = 'dbpyme.db'

    def __init__(self, dialog):

        Ui_Form.__init__(self)
        self.setupUi(dialog)
        self.pushButton_2.clicked.connect(self.salir)
        self.pushButton.clicked.connect(self.conexion)
        self.pushButton.setFocus()
        

    def msjerror(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Las credenciales ingresadas son incorrectas")
        msg.addButton(QMessageBox.Ok)
        msg.exec()

    # Comprueba las credenciales
    def conexion(self):
        usuario = self.lineEdit.text()
        querry = f"SELECT * FROM usuarios WHERE username LIKE '%{usuario}%'"
        datos = consultas.sql_querry(self, querry)

        # Si no se coloca un nombre de usuario larga un aviso
        if usuario == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Debe ingresar un nombre de usuario")
            msg.addButton(QMessageBox.Ok)
            msg.exec()
        else:
            # Si las credenciales son correctas muestra el f_main
            for i in datos:  # Realiza la busqueda de los password guardados para ver coincidencia

                if self.lineEdit.text() + self.lineEdit_2.text() == i[1] + i[2]:
                    from f_main import Ui_MainWindow
                    self.f_main = QtWidgets.QMainWindow()
                    self.ui = Ui_MainWindow()
                    self.ui.setupUi(self.f_main)
                    self.f_main.show()
                    if i[3] == 0:
                        self.ui.menuAdministracion.setDisabled(True)
                    self.f_main.showMaximized()
                    # Oculta el login
                    dialog.hide()
                    break  # Corta la busqueda al haber coincidencia en los password guardados
                else:
                    self.msjerror()
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    return 0

    def salir(self):
        quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = Ventana(dialog)
    dialog.show()
    sys.exit(app.exec())
