from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
class MainView(QMainWindow):

    def __init__(self):  # this
        super(MainView, self).__init__()  # Inicializa la clase -> Initialize
        uic.loadUi("view/view.ui", self)

    # Conectar la señal clicked del botón "Exit" a la función que cierra la ventana
        self.btn_exit.clicked.connect(self.close_window)
        self.btn_execute.clicked.connect(self.execute_code)
        self.btn_new.clicked.connect(self.open_new_dialog)
        self.btn_options.clicked.connect(self.open_options_dialog)

    def open_options_dialog(self):
        options = ["Load File", "Option 1", "Option 2"]
        choice, _ = QInputDialog.getItem(self, "Options", "Select an option:", options, editable=False)

        if choice == "Load File":
            self.open_file_dialog()
        elif choice == "Option 1":
            self.handle_option_1()
        elif choice == "Option 2":
            self.handle_option_2()

    # ... (otros métodos relacionados con las opciones)

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
    def open_new_dialog(self):
        text, ok = QInputDialog.getText(self, 'New File', 'Enter file name:')
        if ok and text:
            self.save_to_file(text)

    def save_to_file(self, filename):
        content = self.textEdit.toPlainText()
        with open(f'{filename}.txt', 'w') as file:
            file.write(content)