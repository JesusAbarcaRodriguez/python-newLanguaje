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
from functions.execute_code import execute_code
from functions.lexical_analysis.lexical_highlighter import LexicalHighlighter
class MainView(QMainWindow):
    comand_text = None
    def __init__(self):
        super(MainView, self).__init__()
        uic.loadUi("view/view.ui", self)
        # Agregar un QLineEdit para la línea de comandos
        self.command_line = QLineEdit(self)
        self.command_line.setStyleSheet("font: 11pt 'Cascadia Code' color:rgb(255,255,255);")
        self.command_line.returnPressed.connect(self.execute_command)
        self.command_line.setEnabled(False)
        # Configurar diseño de la interfaz
        self.verticalLayout_4.addWidget(self.command_line)
        self.data_types_dialog = None
        self.functions_dialog = None
        self.operations_dialog = None
        self.reserved_words_dialog = None
        self.btn_exit.clicked.connect(self.close_window)
        self.btn_compile.clicked.connect(self.compile_codeUi)
        self.btn_new.clicked.connect(self.open_new_dialog)
        self.btn_options.clicked.connect(self.show_options_menu)
        self.btn_execute.clicked.connect(self.execute_codeUi)

        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.highlighter = LexicalHighlighter(self.textEdit.document())
    def on_comand_line(self):
        self.command_line.setEnabled(True)
        self.command_line.setStyleSheet("background-color: lightblue;")
    def off_comand_line(self):
        self.command_line.setEnabled(False)
        self.command_line.setStyleSheet("background-color: transparent;")
        self.command_text = None
    def execute_command(self):
        command = self.command_line.text()
        self.command_line.clear()
        current_text = self.textEdit_2.toPlainText()
        new_text = f"{current_text} >>{command} \n"
        self.textEdit_2.setPlainText(new_text)
        self.comand_text = command
        self.command_line.setStyleSheet("font: 11pt 'Cascadia Code' color:rgb(255,255,255);")
        self.command_line.setEnabled(False)
    def write_variables(self, variable_text):
        current_text = self.textEdit_2.toPlainText()
        # Reemplazar "##" por un salto de línea
        variable_text = variable_text.replace("//", "\n")
        new_text = f"{current_text}{variable_text}"
        self.textEdit_2.setPlainText(new_text)

    def execute_custom_command(self, command):
        # Implementa la lógica para ejecutar un comando personalizado aquí.
        # Retorna la salida del comando como una cadena.
        # Este es solo un ejemplo, debes reemplazarlo con tu propia lógica.
        return f"{command}"
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
    def execute_codeUi(self):
        code = self.textEdit.toPlainText()
        current_text = self.textEdit_2.toPlainText()
        new_text = f"{current_text} {execute_code(self, code)}"
        self.textEdit_2.setPlainText(new_text)
    def compile_codeUi(self):
        code = self.textEdit.toPlainText()
        current_text = self.textEdit_2.toPlainText()
        new_text = f"{current_text} {compile_code(code)}"
        self.textEdit_2.setPlainText(new_text)
        #compile_code(self, code)
    def open_new_dialog(self):
        text, ok = QInputDialog.getText(self, 'New File', 'Enter file name:')
        if ok and text:
            self.save_to_file(text)

    def save_to_file(self, filename):
        content = self.textEdit.toPlainText()
        with open(f'{filename}.txt', 'w') as file:
            file.write(content)