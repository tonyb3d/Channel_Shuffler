import os
import sys

import PIL
import yaml
from loguru import logger
from PySide6.QtWidgets import *

from GUI.Main_ui import Ui_Main_ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main_ui()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        _format_list = ["jpg", "tiff", "png", "tga"]

        self.setWindowTitle("Channel_shuffler")

        self.ui.filetype_combobox.addItems(_format_list)
        self.ui.filetype_combobox.setCurrentIndex(1)

        self.ui.input_metalness_mask.setPlaceholderText("Ключевые слова, через запятую.")
        self.ui.input_metalness_mask.setText("metalness, metallic")

        self.ui.input_height_mask.setPlaceholderText("Ключевые слова, через запятую.")
        self.ui.input_height_mask.setText("height, displacement")

        self.ui.input_roughness_mask.setPlaceholderText("Ключевые слова, через запятую.")
        self.ui.input_roughness_mask.setText("roughness, smoothness")

        self.ui.input_basecolor_mask.setPlaceholderText("Ключевые слова, через запятую.")
        self.ui.input_basecolor_mask.setText("base_color, color, albedo, diffuse")

        self.ui.input_normal_mask.setPlaceholderText("Ключевые слова, через запятую.")
        self.ui.input_normal_mask.setText("normal, tangent") 

        self.ui.input_ao_mask.setPlaceholderText("Ключевые слова, через запятую.")
        self.ui.input_ao_mask.setText("ao, ambient_occlusion")


        self.ui.red_checkbox.setChecked(True)
        self.ui.green_checkbox.setChecked(True)
        self.ui.blue_checkbox.setChecked(True)

        self.ui.import_path_button.clicked.connect(self.set_import_path)
        self.ui.export_path_button.clicked.connect(self.set_export_path)

        self.ui.texture_output_mask.setPlaceholderText("Суффикс")


    def set_import_path(self):
        import_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.import_path.setText(import_path)

    def set_export_path(self):
        export_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.export_path.setText(export_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())