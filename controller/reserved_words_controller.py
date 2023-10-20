from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
class ReservedWordsDialog(QDialog):
    def __init__(self, parent=None):
        super(ReservedWordsDialog, self).__init__(parent)
        uic.loadUi("view/reservedWord.ui", self)
        self.btn_select.clicked.connect(self.select_reserved_word)
        self.initialize_reserved_words()
    def initialize_reserved_words(self):
        self.reserved_words = {
            "MIENTRAS": "\n MIENTRAS i<10 INICIO \n … i : i + 1; \n FIN",
            "DE": "\n DE i=0…variable INICIO \n … $Acá se va a ejecutar el bucle de 0 hasta el valor de la variable$ \n FIN",
            "CUANDO": "\n CUANDO i<10 INICIO \n … i : i + 1; \n FIN \n  SINO INICIO \n … i : i + 1; \n FIN",
        }
        self.listWidget.addItems(self.reserved_words.keys())
    def select_reserved_word(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            selected_word = selected_item.text()
            main_window = self.parent()
            main_window.add_reserved_word_to_text_edit(self.reserved_words.get(selected_word, ""))  # Llamada a un método en MainView
            self.close()

