from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from ui.qt_ui.ui_mapwidget import Ui_MapWidget



class MapWidget(QWidget):
    delete = Signal(int)


    def __init__(self, id_widget: int, parent=None):
        super(MapWidget, self).__init__(parent)
        self.ui = Ui_MapWidget()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.groupBox.setTitle(str(id_widget))
        self.ui.pushButton.clicked.connect(self.press_del)


    @Slot()
    def press_del(self):
        self.delete.emit(self.id_widget)