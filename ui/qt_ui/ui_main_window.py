# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Main_ui(object):
    def setupUi(self, Main_ui):
        if not Main_ui.objectName():
            Main_ui.setObjectName(u"Main_ui")
        Main_ui.resize(1207, 769)
        font = QFont()
        font.setBold(False)
        Main_ui.setFont(font)
        self.groupBox = QGroupBox(Main_ui)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 621, 721))
        self.groupBox.setMinimumSize(QSize(541, 0))
        self.groupBox.setMaximumSize(QSize(1024, 16777215))
        self.import_path_button = QToolButton(self.groupBox)
        self.import_path_button.setObjectName(u"import_path_button")
        self.import_path_button.setGeometry(QRect(480, 40, 32, 19))
        self.import_path_button.setMinimumSize(QSize(32, 0))
        self.import_path = QLineEdit(self.groupBox)
        self.import_path.setObjectName(u"import_path")
        self.import_path.setGeometry(QRect(141, 40, 341, 20))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(21, 40, 91, 16))
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 70, 601, 651))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.groupBox_4)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 579, 616))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mapwidget_gridLayout = QGridLayout()
        self.mapwidget_gridLayout.setObjectName(u"mapwidget_gridLayout")

        self.verticalLayout_2.addLayout(self.mapwidget_gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.subfolders_check = QCheckBox(self.groupBox)
        self.subfolders_check.setObjectName(u"subfolders_check")
        self.subfolders_check.setGeometry(QRect(20, 20, 171, 17))
        self.groupBox_2 = QGroupBox(Main_ui)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(640, 10, 551, 351))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 91, 16))
        self.export_path_button = QToolButton(self.groupBox_2)
        self.export_path_button.setObjectName(u"export_path_button")
        self.export_path_button.setGeometry(QRect(500, 40, 31, 20))
        self.export_path = QLineEdit(self.groupBox_2)
        self.export_path.setObjectName(u"export_path")
        self.export_path.setGeometry(QRect(162, 40, 341, 20))
        self.texture_channel_picker = QGroupBox(self.groupBox_2)
        self.texture_channel_picker.setObjectName(u"texture_channel_picker")
        self.texture_channel_picker.setGeometry(QRect(10, 70, 531, 201))
        self.image_preview = QGraphicsView(self.texture_channel_picker)
        self.image_preview.setObjectName(u"image_preview")
        self.image_preview.setGeometry(QRect(10, 50, 128, 128))
        self.image_preview.setMinimumSize(QSize(128, 128))
        self.image_preview.setMaximumSize(QSize(128, 128))
        self.gridLayoutWidget_2 = QWidget(self.texture_channel_picker)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(150, 20, 371, 181))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.blue_channel_file = QComboBox(self.gridLayoutWidget_2)
        self.blue_channel_file.setObjectName(u"blue_channel_file")
        self.blue_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.blue_channel_file, 3, 1, 1, 1)

        self.alpha_channel_list = QComboBox(self.gridLayoutWidget_2)
        self.alpha_channel_list.setObjectName(u"alpha_channel_list")
        self.alpha_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.alpha_channel_list, 4, 2, 1, 1)

        self.blue_channel_list = QComboBox(self.gridLayoutWidget_2)
        self.blue_channel_list.setObjectName(u"blue_channel_list")
        self.blue_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.blue_channel_list, 3, 2, 1, 1)

        self.alpha_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.alpha_checkbox.setObjectName(u"alpha_checkbox")

        self.gridLayout_2.addWidget(self.alpha_checkbox, 4, 0, 1, 1)

        self.alpha_channel_file = QComboBox(self.gridLayoutWidget_2)
        self.alpha_channel_file.setObjectName(u"alpha_channel_file")
        self.alpha_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.alpha_channel_file, 4, 1, 1, 1)

        self.green_channel_list = QComboBox(self.gridLayoutWidget_2)
        self.green_channel_list.setObjectName(u"green_channel_list")
        self.green_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.green_channel_list, 2, 2, 1, 1)

        self.green_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.green_checkbox.setObjectName(u"green_checkbox")

        self.gridLayout_2.addWidget(self.green_checkbox, 2, 0, 1, 1)

        self.red_channel_list = QComboBox(self.gridLayoutWidget_2)
        self.red_channel_list.setObjectName(u"red_channel_list")
        self.red_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.red_channel_list, 1, 2, 1, 1)

        self.green_channel_file = QComboBox(self.gridLayoutWidget_2)
        self.green_channel_file.setObjectName(u"green_channel_file")
        self.green_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.green_channel_file, 2, 1, 1, 1)

        self.blue_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.blue_checkbox.setObjectName(u"blue_checkbox")

        self.gridLayout_2.addWidget(self.blue_checkbox, 3, 0, 1, 1)

        self.red_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.red_checkbox.setObjectName(u"red_checkbox")

        self.gridLayout_2.addWidget(self.red_checkbox, 1, 0, 1, 1)

        self.red_channel_file = QComboBox(self.gridLayoutWidget_2)
        self.red_channel_file.setObjectName(u"red_channel_file")
        self.red_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.red_channel_file, 1, 1, 1, 1)

        self.texture_output_mask = QLineEdit(self.gridLayoutWidget_2)
        self.texture_output_mask.setObjectName(u"texture_output_mask")
        self.texture_output_mask.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.texture_output_mask, 0, 1, 1, 1)

        self.filetype_combobox = QComboBox(self.gridLayoutWidget_2)
        self.filetype_combobox.setObjectName(u"filetype_combobox")
        self.filetype_combobox.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.filetype_combobox, 0, 2, 1, 1)

        self.minus_button = QPushButton(self.groupBox_2)
        self.minus_button.setObjectName(u"minus_button")
        self.minus_button.setGeometry(QRect(470, 280, 61, 31))
        self.plus_button = QPushButton(self.groupBox_2)
        self.plus_button.setObjectName(u"plus_button")
        self.plus_button.setGeometry(QRect(470, 310, 61, 31))
        self.start_button = QPushButton(Main_ui)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(850, 700, 151, 41))
        self.scan_button = QPushButton(Main_ui)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setGeometry(QRect(690, 700, 151, 41))
        self.add_pushbutton = QPushButton(Main_ui)
        self.add_pushbutton.setObjectName(u"add_pushbutton")
        self.add_pushbutton.setGeometry(QRect(40, 730, 75, 23))
        self.clear_pushbutton = QPushButton(Main_ui)
        self.clear_pushbutton.setObjectName(u"clear_pushbutton")
        self.clear_pushbutton.setGeometry(QRect(530, 730, 75, 23))

        self.retranslateUi(Main_ui)

        QMetaObject.connectSlotsByName(Main_ui)
    # setupUi

    def retranslateUi(self, Main_ui):
        Main_ui.setWindowTitle(QCoreApplication.translate("Main_ui", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Main_ui", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.import_path_button.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label.setText(QCoreApplication.translate("Main_ui", u"\u041f\u0443\u0442\u044c \u0438\u043c\u043f\u043e\u0440\u0442\u0430", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Main_ui", u"\u041c\u0430\u0441\u043a\u0438 \u0438\u043c\u0435\u043d \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.subfolders_check.setText(QCoreApplication.translate("Main_ui", u"\u041f\u043e\u0438\u0441\u043a \u0432 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u0445", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Main_ui", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Main_ui", u"\u041f\u0443\u0442\u044c \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.export_path_button.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.texture_channel_picker.setTitle(QCoreApplication.translate("Main_ui", u"Texture 1", None))
        self.alpha_checkbox.setText(QCoreApplication.translate("Main_ui", u"A", None))
        self.green_checkbox.setText(QCoreApplication.translate("Main_ui", u"G", None))
        self.blue_checkbox.setText(QCoreApplication.translate("Main_ui", u"B", None))
        self.red_checkbox.setText(QCoreApplication.translate("Main_ui", u"R", None))
        self.minus_button.setText(QCoreApplication.translate("Main_ui", u"-", None))
        self.plus_button.setText(QCoreApplication.translate("Main_ui", u"+", None))
        self.start_button.setText(QCoreApplication.translate("Main_ui", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.scan_button.setText(QCoreApplication.translate("Main_ui", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.add_pushbutton.setText(QCoreApplication.translate("Main_ui", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.clear_pushbutton.setText(QCoreApplication.translate("Main_ui", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

