from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QListWidgetItem

class OperationTypesDialog(QDialog):
    def __init__(self, parent=None):
        super(OperationTypesDialog, self).__init__(parent)
        uic.loadUi("view/operations.ui", self)
        self.btn_select.clicked.connect(self.select_operation)
        self.initialize_operations()
    def initialize_operations(self):
        self.operations = {
            "SUMA": "\n a+b",
            "RESTA": "\n a-b",
            "MULTIPLICACION": "\n a*b",
            "DIVISION": "\n a/b",
            "AND": "\n a = b & c = d",
            "OR": "\n a = b # c = d",
            "DIFERENTE": "\n a ! b ",
            "MAYOR": "\n a>b",
            "MENOR": "\n a<b",
            "IGUAL": "\n a=b",
            "ASIGNACION": "\n a : b",
        }
        self.listWidget.addItems(self.operations.keys())
    def select_operation(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            selected_operation = selected_item.text()
            main_window = self.parent()
            main_window.add_operation_to_text_edit(self.operations.get(selected_operation, ""))
            self.close()
