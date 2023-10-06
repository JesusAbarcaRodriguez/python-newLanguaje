from math import exp
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller.ui_controller import MainView
# =======================
# Main
# =======================
main = None
if __name__ == '__main__': 
    app = QApplication(sys.argv)
    main = MainView()
    main.show()
    sys.exit(app.exec_())

def write_variables(variable_text):
    main.write_variables(main,variable_text)

