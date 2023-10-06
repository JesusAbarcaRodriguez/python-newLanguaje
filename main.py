
import sys
from PyQt5.QtWidgets import QApplication
from controller.ui_controller import MainView
# =======================
# Main
# =======================

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    main = MainView()
    main.show()
    sys.exit(app.exec_())


