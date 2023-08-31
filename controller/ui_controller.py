from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QAction, QMenu
from functions.readCode import verify_syntax
class MainView(QMainWindow):

    def __init__(self):  # this
        super(MainView, self).__init__()
        uic.loadUi("view/view.ui", self)

        self.btn_exit.clicked.connect(self.close_window)
        self.btn_execute.clicked.connect(self.execute_code)
        self.btn_new.clicked.connect(self.open_new_dialog)
        self.btn_options.clicked.connect(self.show_options_menu)
        self.btn_reserved_words.clicked.connect(self.show_reserved_words_dialog)


    def show_reserved_words_dialog(self):
        dialog = ReservedWordsDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            selected_word = dialog.get_selected_word()
            if selected_word:
                self.textEdit.append(selected_word)
    def show_options_menu(self):
        options_menu = QMenu(self)

        reserved_words_action = QAction("Palabras reservadas", self)
        syntax_menu = QMenu("Sintaxis", self)
        control_action = QAction("Control", self)
        functions_action = QAction("Funciones", self)
        operations_action = QAction("Operaciones", self)
        semantic_action = QAction("Semántica", self)
        data_types_action = QAction("Tipos de datos", self)
        load_file_action = QAction("Cargar archivo", self)
        syntax_menu.addAction(control_action)
        syntax_menu.addAction(functions_action)
        syntax_menu.addAction(operations_action)

        options_menu.addAction(reserved_words_action)
        options_menu.addMenu(syntax_menu)
        options_menu.addAction(semantic_action)
        options_menu.addAction(data_types_action)
        options_menu.addAction(load_file_action)
        selected_action = options_menu.exec_(self.btn_options.mapToGlobal(self.btn_options.rect().bottomLeft()))

        if selected_action == reserved_words_action:
            self.generate_code_for_reserved_words()
        elif selected_action == control_action:
            self.generate_code_for_control_syntax()
        elif selected_action == load_file_action:
            self.open_file_dialog()
        # ... (similarly for other actions)

    # ... (other methods)

    def generate_code_for_reserved_words(self):
        code = "Tu código para palabras reservadas\n"
        final_code = self.textEdit.toPlainText() + code
        self.textEdit.setPlainText(final_code)

    def generate_code_for_control_syntax(self):
        code = "Tu código para sintaxis de control"
        self.textEdit.setPlainText(code)
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            self.load_file(file_path)

    def load_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                self.textEdit.setPlainText(content)
        except Exception as e:
            print(f"Error loading file: {e}")

    def handle_option_1(self):
        QMessageBox.information(self, "Option 1", "Option 1 selected.")

    def handle_option_2(self):
        QMessageBox.information(self, "Option 2", "Option 2 selected.")
    def close_window(self):
        self.close()
    def execute_code(self):
        code = self.textEdit.toPlainText()
        self.textEdit_2.setPlainText(code)
        verify_syntax(code)
    def open_new_dialog(self):
        text, ok = QInputDialog.getText(self, 'New File', 'Enter file name:')
        if ok and text:
            self.save_to_file(text)

    def save_to_file(self, filename):
        content = self.textEdit.toPlainText()
        with open(f'{filename}.txt', 'w') as file:
            file.write(content)