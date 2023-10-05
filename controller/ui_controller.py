from PyQt5 import uic
from PyQt5.QtWidgets import QDialog,QMainWindow,QListWidgetItem, QTextEdit
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QAction, QMenu
from controller.data_types_controller import DataTypesDialog
from controller.functions_controller import FunctionTypesDialog
from controller.operations_controller import OperationTypesDialog
from controller.reserved_words_controller import ReservedWordsDialog
from functions.compile_code import compile_code
from functions.lexical_analysis.lexical_highlighter import LexicalHighlighter
class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        uic.loadUi("view/view.ui", self)
        self.data_types_dialog = None
        self.functions_dialog = None
        self.operations_dialog = None
        self.reserved_words_dialog = None
        self.btn_exit.clicked.connect(self.close_window)
        self.btn_compile.clicked.connect(self.execute_code)
        self.btn_new.clicked.connect(self.open_new_dialog)
        self.btn_options.clicked.connect(self.show_options_menu)
        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.highlighter = LexicalHighlighter(self.textEdit.document())
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
        elif selected_action == operations_action:
            self.generate_code_for_operations()
        elif selected_action == control_action:
            self.generate_code_for_control_syntax()
        elif selected_action == load_file_action:
            self.open_file_dialog()
        elif selected_action == data_types_action:
            self.generate_code_for_data_types()
        elif selected_action == functions_action:
            self.generate_code_for_functions()
        # ... (similarly for other actions)

    # ... (other methods)
    def generate_code_for_operations(self):
        try:
            if not self.operations_dialog:
                self.operations_dialog = OperationTypesDialog(self)
            self.operations_dialog.exec_()
        except Exception as e:
            print(f"Error in generate_code_for_operations: {e}")
    def generate_code_for_functions(self):
        try:
            if not self.functions_dialog:
                self.functions_dialog = FunctionTypesDialog(self)
            self.functions_dialog.exec_()
        except Exception as e:
            print(f"Error in generate_code_for_functions: {e}")
    def generate_code_for_data_types(self):
        try:
            if not self.data_types_dialog:
                self.data_types_dialog = DataTypesDialog(self)
            self.data_types_dialog.exec_()
        except Exception as e:
            print(f"Error in generate_code_for_data_types: {e}")
    def add_operation_to_text_edit(self, operation):
        current_text = self.textEdit.toPlainText()
        new_text = f"{current_text} {operation}"
        self.textEdit.setPlainText(new_text)
    def add_function_to_text_edit(self, function):
        current_text = self.textEdit.toPlainText()
        new_text = f"{current_text} {function}"
        self.textEdit.setPlainText(new_text)
    def add_data_type_to_text_edit(self, data_type):
        current_text = self.textEdit.toPlainText()
        new_text = f"{current_text} {data_type}"
        self.textEdit.setPlainText(new_text)
    def generate_code_for_reserved_words(self):
        try:
            if not self.reserved_words_dialog:
                self.reserved_words_dialog = ReservedWordsDialog(self)
            self.reserved_words_dialog.exec_()
        except Exception as e:
            print(f"Error in generate_code_for_reserved_words: {e}")
    def add_reserved_word_to_text_edit(self, reserved_word):
        current_text = self.textEdit.toPlainText()
        new_text = f"{current_text} {reserved_word}"
        self.textEdit.setPlainText(new_text)
    def generate_code_for_control_syntax(self):
        code = "Tu código para sintaxis de control"
        final_code = self.textEdit.toPlainText() + code
        self.textEdit.setPlainText(final_code)
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
        self.textEdit_2.setPlainText(compile_code(code))
    def open_new_dialog(self):
        text, ok = QInputDialog.getText(self, 'New File', 'Enter file name:')
        if ok and text:
            self.save_to_file(text)

    def save_to_file(self, filename):
        content = self.textEdit.toPlainText()
        with open(f'{filename}.txt', 'w') as file:
            file.write(content)