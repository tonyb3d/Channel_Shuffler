# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_window.ui'
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
    QGraphicsView, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QToolButton, QWidget)

class Ui_Main_ui(object):
    def setupUi(self, Main_ui):
        if not Main_ui.objectName():
            Main_ui.setObjectName(u"Main_ui")
        Main_ui.resize(1128, 658)
        self.groupBox = QGroupBox(Main_ui)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 541, 351))
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
        self.subfolders_check = QCheckBox(self.groupBox)
        self.subfolders_check.setObjectName(u"subfolders_check")
        self.subfolders_check.setGeometry(QRect(20, 280, 171, 17))
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 70, 521, 201))
        self.gridLayoutWidget = QWidget(self.groupBox_4)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 501, 171))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_9 = QToolButton(self.gridLayoutWidget)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setMinimumSize(QSize(32, 0))

        self.gridLayout.addWidget(self.toolButton_9, 0, 3, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.toolButton_6 = QToolButton(self.gridLayoutWidget)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setMinimumSize(QSize(32, 0))

        self.gridLayout.addWidget(self.toolButton_6, 1, 3, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.input_roughness_mask = QLineEdit(self.gridLayoutWidget)
        self.input_roughness_mask.setObjectName(u"input_roughness_mask")
        self.input_roughness_mask.setMinimumSize(QSize(350, 0))
        self.input_roughness_mask.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.input_roughness_mask, 2, 2, 1, 1)

        self.input_normal_mask = QLineEdit(self.gridLayoutWidget)
        self.input_normal_mask.setObjectName(u"input_normal_mask")
        self.input_normal_mask.setMinimumSize(QSize(350, 0))
        self.input_normal_mask.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.input_normal_mask, 4, 2, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.input_basecolor_mask = QLineEdit(self.gridLayoutWidget)
        self.input_basecolor_mask.setObjectName(u"input_basecolor_mask")
        self.input_basecolor_mask.setMinimumSize(QSize(350, 0))
        self.input_basecolor_mask.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.input_basecolor_mask, 3, 2, 1, 1)

        self.toolButton_8 = QToolButton(self.gridLayoutWidget)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setMinimumSize(QSize(32, 0))

        self.gridLayout.addWidget(self.toolButton_8, 2, 3, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.toolButton_7 = QToolButton(self.gridLayoutWidget)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setMinimumSize(QSize(32, 0))

        self.gridLayout.addWidget(self.toolButton_7, 4, 3, 1, 1)

        self.toolButton_10 = QToolButton(self.gridLayoutWidget)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setMinimumSize(QSize(32, 0))

        self.gridLayout.addWidget(self.toolButton_10, 3, 3, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.input_metalness_mask = QLineEdit(self.gridLayoutWidget)
        self.input_metalness_mask.setObjectName(u"input_metalness_mask")
        self.input_metalness_mask.setMinimumSize(QSize(350, 0))
        self.input_metalness_mask.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.input_metalness_mask, 0, 2, 1, 1)

        self.input_height_mask = QLineEdit(self.gridLayoutWidget)
        self.input_height_mask.setObjectName(u"input_height_mask")
        self.input_height_mask.setMinimumSize(QSize(350, 0))
        self.input_height_mask.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.input_height_mask, 1, 2, 1, 1)

        self.groupBox_2 = QGroupBox(Main_ui)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(560, 10, 551, 351))
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
        self.gridLayoutWidget_2.setGeometry(QRect(150, 20, 371, 171))
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

        self.alpha_enable = QCheckBox(self.gridLayoutWidget_2)
        self.alpha_enable.setObjectName(u"alpha_enable")

        self.gridLayout_2.addWidget(self.alpha_enable, 4, 0, 1, 1)

        self.alpha_channel_file = QComboBox(self.gridLayoutWidget_2)
        self.alpha_channel_file.setObjectName(u"alpha_channel_file")
        self.alpha_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.alpha_channel_file, 4, 1, 1, 1)

        self.green_channel_list = QComboBox(self.gridLayoutWidget_2)
        self.green_channel_list.setObjectName(u"green_channel_list")
        self.green_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.green_channel_list, 2, 2, 1, 1)

        self.green_enable = QCheckBox(self.gridLayoutWidget_2)
        self.green_enable.setObjectName(u"green_enable")

        self.gridLayout_2.addWidget(self.green_enable, 2, 0, 1, 1)

        self.red_channel_list = QComboBox(self.gridLayoutWidget_2)
        self.red_channel_list.setObjectName(u"red_channel_list")
        self.red_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.red_channel_list, 1, 2, 1, 1)

        self.green_channel_file = QComboBox(self.gridLayoutWidget_2)
        self.green_channel_file.setObjectName(u"green_channel_file")
        self.green_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.green_channel_file, 2, 1, 1, 1)

        self.blue_enable = QCheckBox(self.gridLayoutWidget_2)
        self.blue_enable.setObjectName(u"blue_enable")

        self.gridLayout_2.addWidget(self.blue_enable, 3, 0, 1, 1)

        self.red_enable = QCheckBox(self.gridLayoutWidget_2)
        self.red_enable.setObjectName(u"red_enable")

        self.gridLayout_2.addWidget(self.red_enable, 1, 0, 1, 1)

        self.red_channel_file = QComboBox(self.gridLayoutWidget_2)
        self.red_channel_file.setObjectName(u"red_channel_file")
        self.red_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.red_channel_file, 1, 1, 1, 1)

        self.texture_output_mask = QLineEdit(self.gridLayoutWidget_2)
        self.texture_output_mask.setObjectName(u"texture_output_mask")
        self.texture_output_mask.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.texture_output_mask, 0, 1, 1, 1)

        self.output_filetype = QComboBox(self.gridLayoutWidget_2)
        self.output_filetype.setObjectName(u"output_filetype")
        self.output_filetype.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.output_filetype, 0, 2, 1, 1)

        self.minus_button = QPushButton(self.groupBox_2)
        self.minus_button.setObjectName(u"minus_button")
        self.minus_button.setGeometry(QRect(470, 280, 61, 31))
        self.plus_button = QPushButton(self.groupBox_2)
        self.plus_button.setObjectName(u"plus_button")
        self.plus_button.setGeometry(QRect(470, 310, 61, 31))
        self.tableView = QTableView(Main_ui)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 370, 1091, 192))
        self.start_button = QPushButton(Main_ui)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(560, 590, 151, 41))
        self.scan_button = QPushButton(Main_ui)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setGeometry(QRect(400, 590, 151, 41))

        self.retranslateUi(Main_ui)

        QMetaObject.connectSlotsByName(Main_ui)
    # setupUi

    def retranslateUi(self, Main_ui):
        Main_ui.setWindowTitle(QCoreApplication.translate("Main_ui", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Main_ui", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.import_path_button.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label.setText(QCoreApplication.translate("Main_ui", u"\u041f\u0443\u0442\u044c \u0438\u043c\u043f\u043e\u0440\u0442\u0430", None))
        self.subfolders_check.setText(QCoreApplication.translate("Main_ui", u"\u041f\u043e\u0438\u0441\u043a \u0432 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u0445", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Main_ui", u"\u041c\u0430\u0441\u043a\u0438 \u0438\u043c\u0435\u043d \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.toolButton_9.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label_8.setText(QCoreApplication.translate("Main_ui", u"Roughness", None))
        self.toolButton_6.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label_9.setText(QCoreApplication.translate("Main_ui", u"Metalness", None))
        self.label_10.setText(QCoreApplication.translate("Main_ui", u"Base Color", None))
        self.toolButton_8.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label_7.setText(QCoreApplication.translate("Main_ui", u"Normal", None))
        self.toolButton_7.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.toolButton_10.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label_6.setText(QCoreApplication.translate("Main_ui", u"Height", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Main_ui", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Main_ui", u"\u041f\u0443\u0442\u044c \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.export_path_button.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.texture_channel_picker.setTitle(QCoreApplication.translate("Main_ui", u"Texture 1", None))
        self.alpha_enable.setText(QCoreApplication.translate("Main_ui", u"A", None))
        self.green_enable.setText(QCoreApplication.translate("Main_ui", u"G", None))
        self.blue_enable.setText(QCoreApplication.translate("Main_ui", u"B", None))
        self.red_enable.setText(QCoreApplication.translate("Main_ui", u"R", None))
        self.minus_button.setText(QCoreApplication.translate("Main_ui", u"-", None))
        self.plus_button.setText(QCoreApplication.translate("Main_ui", u"+", None))
        self.start_button.setText(QCoreApplication.translate("Main_ui", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.scan_button.setText(QCoreApplication.translate("Main_ui", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

