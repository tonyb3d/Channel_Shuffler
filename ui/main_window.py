from PySide6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem, QAbstractItemView
from PySide6.QtCore import Slot

from ui.qt_ui.ui_main_window import Ui_Main_ui
from ui.mapwidget import Map_Widget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_ui()
        self.ui.setupUi(self)
        self.my_widgets_dict: dict[int, QListWidgetItem] = {}
        self.map_id_counter: int = 0
        _format_list = ["jpg", "tiff", "png", "tga"]

        self.setWindowTitle("Channel_shuffler")

        self.ui.filetype_combobox.addItems(_format_list)
        self.ui.filetype_combobox.setCurrentIndex(1)

        self.ui.red_checkbox.setChecked(True)
        self.ui.green_checkbox.setChecked(True)
        self.ui.blue_checkbox.setChecked(True)

        self.ui.import_path_button.clicked.connect(self.set_import_path)
        self.ui.export_path_button.clicked.connect(self.set_export_path)

        self.ui.texture_output_mask.setPlaceholderText("Суффикс")

        self.ui.add_pushbutton.clicked.connect(self.add_mapwidget)
        self.ui.clear_pushbutton.clicked.connect(self.clear_mapwidgets_list)
        
    def set_import_path(self):
        import_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.import_path.setText(import_path)

    def set_export_path(self):
        export_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.export_path.setText(export_path)

    @Slot()
    def add_mapwidget(self):
        widget = Map_Widget(self.map_id_counter)
        print(self.map_id_counter)
        my_item = QListWidgetItem(self.ui.mapwidget_listwidget)
        my_item.setSizeHint(widget.sizeHint())
        self.my_widgets_dict[widget.my_ID] = my_item
        self.ui.mapwidget_listwidget.addItem(my_item)
        self.ui.mapwidget_listwidget.setItemWidget(my_item, widget)
        widget.delete.connect(self.delete_mapwidget)

        self.map_id_counter += 1


    @Slot()
    def clear_mapwidgets_list(self):
        self.ui.mapwidget_listwidget.clear()
        self.map_id_counter = 0
        
    @Slot(int)
    def delete_mapwidget(self):
        widget = self.sender()
        my_item = self.my_widgets_dict[widget.my_ID]
        self.ui.mapwidget_listwidget.takeItem(self.ui.mapwidget_listwidget.row(my_item))
        del self.my_widgets_dict[widget.my_ID]