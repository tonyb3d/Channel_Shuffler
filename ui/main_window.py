from PySide6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem, QAbstractItemView
from PySide6.QtCore import Slot

from ui.qt_ui.ui_main_window import Ui_MainWindow
from ui.parsewidget import Parse_Widget
from ui.constructor_widget import Constructor_Widget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_tooltips()
        self.parse_widgets_dict: dict[int, QListWidgetItem] = {}
        self.cons_widgets_dict: dict[int, QListWidgetItem] = {}
        self.parsewidget_id_counter: int = 0
        self.constructorwidget_id_counter: int = 0
        self.format_list = ["jpg", "tiff", "png", "tga"]

        self.setWindowTitle("Channel_shuffler")

        self.ui.import_path_button.clicked.connect(self.set_import_path)
        self.ui.export_path_button.clicked.connect(self.set_export_path)

        self.ui.parser_add_button.clicked.connect(self.add_parsewidget)
        self.ui.parser_clear_button.clicked.connect(self.clear_parsewidget_list)

        self.ui.constructor_add_button.clicked.connect(self.add_constructorwidget)
        self.ui.constructor_clear_button.clicked.connect(self.clear_constructorwidget_list)


    def set_tooltips(self):
        self.ui.import_path_lineedit.setToolTip("Введите путь к папке или нажмите кнопку справа")
        self.ui.import_path_button.setToolTip("Нажмите для выбора папки, в которой будет производиться поиск файлов")

        self.ui.subfolder_search_checkbox.setToolTip("При включенном чекбоксе будет производиться поиск в подпапках")

        self.ui.export_path_lineedit.setToolTip("Введите путь к папке для экспорта или нажмите кнопку справа")
        self.ui.export_path_button.setToolTip("Нажмите для выбора папки для экспорта")

        self.ui.subfolder_create_checkbox.setToolTip(" При включенном чекбоксе будут создаваться подпапки для материалов. \n Иначе все созданные текстуры будут выгружены в одну папку")
        self.ui.rewrite_files_checkbox.setToolTip(" При повторной выгрузке будут перезаписаны файлы с совпадающими именами. \n Иначе к имени новых файлов будет добавлен порядковый номер")

        self.ui.parse_widget_listwidget.setToolTip('Поле для настроек поиска текстур. Для добавления виджета нажмите кнопку "Добавить"')
        self.ui.parser_add_button.setToolTip("Добавляет виджет парсера в поле выше")
        self.ui.parser_start_button.setToolTip("Запускает процесс поиска текстур")
        self.ui.parser_clear_button.setToolTip("Очищает поле выше")

        self.ui.texture_constructor_listwidget.setToolTip('Поле для настроек конструктора текстур. Для добавления виджета нажмите кнопку "Добавить"')
        self.ui.constructor_add_button.setToolTip("Добавляет виджет конструктора в поле выше")
        self.ui.constructor_start_button.setToolTip("Запускает процесс создания и экспорта текстур")
        self.ui.constructor_clear_button.setToolTip("Очищает поле выше")

        self.ui.tableView.setToolTip("Таблица для отображения результатов обработки текстур")

    def set_import_path(self):
        import_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.import_path_lineedit.setText(import_path)

    def set_export_path(self):
        export_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.ui.export_path_lineedit.setText(export_path)

    @Slot()
    def add_parsewidget(self):
        widget = Parse_Widget(self.parsewidget_id_counter)
        print(self.parsewidget_id_counter)
        my_item = QListWidgetItem(self.ui.parse_widget_listwidget)
        my_item.setSizeHint(widget.sizeHint())
        self.parse_widgets_dict[widget.my_ID] = my_item
        self.ui.parse_widget_listwidget.addItem(my_item)
        self.ui.parse_widget_listwidget.setItemWidget(my_item, widget)
        widget.delete.connect(self.delete_parsewidget)
        self.parsewidget_id_counter += 1

    @Slot()
    def clear_parsewidget_list(self):
        self.ui.parse_widget_listwidget.clear()
        self.parsewidget_id_counter = 0
        
    @Slot(int)
    def delete_parsewidget(self):
        widget = self.sender()
        my_item = self.parse_widgets_dict[widget.my_ID]
        self.ui.parse_widget_listwidget.takeItem(self.ui.parse_widget_listwidget.row(my_item))
        del self.parse_widgets_dict[widget.my_ID]

    @Slot()
    def add_constructorwidget(self):
        widget = Constructor_Widget(self.constructorwidget_id_counter, self.format_list)
        print(self.constructorwidget_id_counter)
        my_item = QListWidgetItem(self.ui.texture_constructor_listwidget)
        my_item.setSizeHint(widget.sizeHint())
        self.cons_widgets_dict[widget.my_ID] = my_item
        self.ui.texture_constructor_listwidget.addItem(my_item)
        self.ui.texture_constructor_listwidget.setItemWidget(my_item, widget)
        widget.delete.connect(self.delete_constructorwidget)
        self.constructorwidget_id_counter += 1

    @Slot()
    def clear_constructorwidget_list(self):
        self.ui.texture_constructor_listwidget.clear()
        self.constructorwidget_id_counter = 0
        
    @Slot(int)
    def delete_constructorwidget(self):
        widget = self.sender()
        my_item = self.cons_widgets_dict[widget.my_ID]
        self.ui.texture_constructor_listwidget.takeItem(self.ui.texture_constructor_listwidget.row(my_item))
        del self.cons_widgets_dict[widget.my_ID]