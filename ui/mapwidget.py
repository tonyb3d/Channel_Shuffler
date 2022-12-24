from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from ui.qt_ui.ui_mapwidget import Ui_MapWidget



class Map_Widget(QWidget):
    delete = Signal(int)


    def __init__(self, idw: int):
        super(Map_Widget, self).__init__()
        self.ui = Ui_MapWidget()
        self.ui.setupUi(self)
        self.my_ID = idw
        self.ui.groupBox.setTitle(str(f"Widget {idw}"))
        self.ui.pushButton.clicked.connect(self.press_del)


    @Slot()
    def press_del(self):
        self.delete.emit(self.my_ID)