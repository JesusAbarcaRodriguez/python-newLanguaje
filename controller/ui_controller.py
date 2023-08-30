from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
class MainView(QMainWindow):

    def __init__(self):  # this
        super(MainView, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("view/view.ui", self)

    # Conectar la señal clicked del botón "Exit" a la función que cierra la ventana
        self.btn_exit.clicked.connect(self.close_window)
        self.btn_execute.clicked.connect(self.execute_code)

    def close_window(self):
        self.close()

    def execute_code(self):
        code = self.textEdit.toPlainText()
        self.textEdit_2.setPlainText(code)