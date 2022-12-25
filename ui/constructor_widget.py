from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from ui.qt_ui.ui_constructor_widget import Ui_ConstructorWidget

class Constructor_Widget(QWidget):
    delete = Signal(int)

    def __init__(self, idw: int):
        super(Constructor_Widget, self).__init__()
        self.ui = Ui_ConstructorWidget()
        self.ui.setupUi(self)

        # self.ui.filetype_combobox.addItems(_format_list)
        # self.ui.filetype_combobox.setCurrentIndex(1)

        self.ui.red_checkbox.setChecked(True)
        self.ui.green_checkbox.setChecked(True)
        self.ui.blue_checkbox.setChecked(True)
        self.ui.alpha_checkbox.setChecked(False)

        self.my_ID = idw
        self.ui.texture_channel_picker.setTitle(str(f"Texture {idw}"))
        self.ui.deleteButton.clicked.connect(self.press_del)

        self.ui.texture_output_mask.setPlaceholderText("Суффикс названия")
        self.ui.texture_output_mask.setToolTip("Будет добавлен к названию текстуры")
        self.ui.filetype_combobox.setToolTip("Формат файла, в который будет сохранена текстура")
        
        self.ui.red_channel_file.setToolTip("Название текстуры из левого столбца, которая будет помещена в этот канал")
        self.ui.red_channel_list.setToolTip("Канал исходной текстуры, который будет помещен в канал сгенерированной текстуры. \nЕсли он отсутствует, то канал сгенерированной текстуры будет залит черным")
        self.ui.green_channel_file.setToolTip("Название текстуры из левого столбца, которая будет помещена в этот канал")
        self.ui.green_channel_list.setToolTip("Канал исходной текстуры, который будет помещен в канал сгенерированной текстуры. \nЕсли он отсутствует, то канал сгенерированной текстуры будет залит черным")
        self.ui.blue_channel_file.setToolTip("Название текстуры из левого столбца, которая будет помещена в этот канал")
        self.ui.blue_channel_list.setToolTip("Канал исходной текстуры, который будет помещен в канал сгенерированной текстуры. \nЕсли он отсутствует, то канал сгенерированной текстуры будет залит черным")
        self.ui.alpha_channel_file.setToolTip("Название текстуры из левого столбца, которая будет помещена в этот канал")
        self.ui.alpha_channel_list.setToolTip("Канал исходной текстуры, который будет помещен в канал сгенерированной текстуры. \nЕсли он отсутствует, то канал сгенерированной текстуры будет залит черным")

        self.ui.red_checkbox.setToolTip("Заполняет канал черным при выкюченном чекбоксе")
        self.ui.green_checkbox.setToolTip("Заполняет канал черным при выкюченном чекбоксе")
        self.ui.blue_checkbox.setToolTip("Заполняет канал черным при выкюченном чекбоксе")
        self.ui.alpha_checkbox.setToolTip("Не создает канал при выключенном чекбоксе")
        self.ui.imagePreview.setToolTip("Отображает превью изображения из первого материала по списку")

    @Slot()
    def press_del(self):
        self.delete.emit(self.my_ID)