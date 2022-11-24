from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Slot

from ui.qt_ui.ui_main_window import Ui_Main_ui
from ui.mapwidget import MapWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_ui()
        self.ui.setupUi(self)
        self.map_id_counter: int = 0
        self.init_ui()


    def init_ui(self):
        _format_list = ["jpg", "tiff", "png", "tga"]

        self.setWindowTitle("Channel_shuffler")

        self.ui.add_pushbutton.clicked.connect(self.add_mapwidget)
        self.ui.clear_pushbutton.clicked.connect(self.clear_mapwidgets_area)

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

    @Slot()
    def add_mapwidget(self):
        self.map_id_counter += 1
        map_widget = MapWidget(self.map_id_counter)
        self.ui.mapwidget_layout.addWidget(map_widget)
        map_widget.delete.connect(self.delete_mapwidget)

    @Slot()
    def clear_mapwidgets_area(self):
        while self.ui.mapwidget_layout.count() > 0:
            item = self.ui.mapwidget_layout.takeAt(0)
            item.widget().deleteLater()
            self.map_id_counter = 0
    
    @Slot(int)
    def delete_mapwidget(self, wid: int):
        print(f"Id удаляемого виджета: {wid}")
        item = self.sender()
        # self.ui.mapwidget_layout.removeWidget(widget)
        # widget.deleteLater()
        # item = self.ui.mapwidget_layout.takeAt(wid)
        self.ui.mapwidget_layout.removeWidget(item)
        item.widget().deleteLater()


    def set_import_path(self):
        import_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.import_path.setText(import_path)

    def set_export_path(self):
        export_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.export_path.setText(export_path)
