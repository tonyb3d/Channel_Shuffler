from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Slot, Signal

from ui.qt_ui.ui_parse_widget import Ui_ParseWidget



class Parse_Widget(QWidget):
    delete = Signal(int)


    def __init__(self, idw: int):
        super(Parse_Widget, self).__init__()
        self.ui = Ui_ParseWidget()
        self.ui.setupUi(self)

        self.ui.mapName.setPlaceholderText("Название")
        self.ui.mapName.setToolTip("Введите название текстуры")

        self.ui.mapMask.setPlaceholderText("Маска")
        self.ui.mapMask.setToolTip("Ключевые слова для поиска текстуры, разделенные запятой")

        self.ui.mapPathButton.clicked.connect(self.set_path)

        self.my_ID = idw
        self.ui.groupBox.setTitle(str(f"Widget {idw}"))
        self.ui.deleteButton.clicked.connect(self.press_del)

    def set_path(self):
        import_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.mapMask.setText(import_path)


    @Slot()
    def press_del(self):
        self.delete.emit(self.my_ID)