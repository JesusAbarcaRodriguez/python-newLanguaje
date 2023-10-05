from PyQt5 import uic
from PyQt5.QtWidgets import QDialog,QMainWindow,QListWidgetItem, QTextEdit
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QAction, QMenu

class DataTypesDialog(QDialog):
    def __init__(self, parent=None):
        super(DataTypesDialog, self).__init__(parent)
        uic.loadUi("view/dataType.ui", self)

        self.btn_select.clicked.connect(self.select_data_type)

        self.initialize_data_types()

    def initialize_data_types(self):
        data_types = ["\n ENTERO", "\n FLOTANTE", "\n CADENA", "\n CARACTER", "\n NULO"]
        for data_type in data_types:
            item = QListWidgetItem(data_type)
            self.listWidget.addItem(item)

    def select_data_type(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            selected_data_type = selected_item.text()
            main_window = self.parent()
            main_window.add_data_type_to_text_edit(selected_data_type)
            self.close()