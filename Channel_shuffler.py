import os
import PIL
import yaml
import sys
from PySide6.QtWidgets import *
from loguru import logger
from GUI.Main_ui import Ui_Main_ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main_ui()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Channel_shuffler")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())