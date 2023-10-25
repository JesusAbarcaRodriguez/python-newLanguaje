from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QListWidgetItem

class FunctionTypesDialog(QDialog):
    def __init__(self, parent=None):
        super(FunctionTypesDialog, self).__init__(parent)
        uic.loadUi("view/functions.ui", self)
        self.btn_select.clicked.connect(self.select_function_type)
        self.initialize_function_types()

    def initialize_function_types(self):
        self.function_types = {
            "FUNCION": "\n ENTERO FUNCION suma(ENTERO a, ENTERO b) \n INICIO \n a:a+b \n RETORNA a \n FIN",
            "PROCEDIMIENTO": "\n PROCEDIMIENTO imprimir(ENTERO a) \n INICIO \n ESCRIBIR(a) \n FIN",
        }
        self.listWidget.addItems(self.function_types.keys())

    def select_function_type(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            selected_type = selected_item.text()
            main_window = self.parent()
            main_window.add_function_to_text_edit(self.function_types.get(selected_type, ""))
            self.close()
