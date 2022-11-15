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
    QFormLayout, QGraphicsView, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Main_ui(object):
    def setupUi(self, Main_ui):
        if not Main_ui.objectName():
            Main_ui.setObjectName(u"Main_ui")
        Main_ui.resize(1125, 754)
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
        self.import_path.setGeometry(QRect(131, 40, 341, 20))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(21, 40, 91, 16))
        self.subfolders_check = QCheckBox(self.groupBox)
        self.subfolders_check.setObjectName(u"subfolders_check")
        self.subfolders_check.setGeometry(QRect(20, 250, 171, 17))
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 70, 521, 171))
        self.formLayout_2 = QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.input_metalness_mask = QLineEdit(self.groupBox_4)
        self.input_metalness_mask.setObjectName(u"input_metalness_mask")
        self.input_metalness_mask.setMinimumSize(QSize(350, 0))

        self.horizontalLayout_4.addWidget(self.input_metalness_mask)

        self.toolButton_9 = QToolButton(self.groupBox_4)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setMinimumSize(QSize(32, 0))

        self.horizontalLayout_4.addWidget(self.toolButton_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.input_height_mask = QLineEdit(self.groupBox_4)
        self.input_height_mask.setObjectName(u"input_height_mask")
        self.input_height_mask.setMinimumSize(QSize(350, 0))
        self.input_height_mask.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_2.addWidget(self.input_height_mask)

        self.toolButton_6 = QToolButton(self.groupBox_4)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setMinimumSize(QSize(32, 0))

        self.horizontalLayout_2.addWidget(self.toolButton_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.input_roughness_mask = QLineEdit(self.groupBox_4)
        self.input_roughness_mask.setObjectName(u"input_roughness_mask")
        self.input_roughness_mask.setMinimumSize(QSize(350, 0))
        self.input_roughness_mask.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_3.addWidget(self.input_roughness_mask)

        self.toolButton_8 = QToolButton(self.groupBox_4)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setMinimumSize(QSize(32, 0))

        self.horizontalLayout_3.addWidget(self.toolButton_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.input_basecolor_mask = QLineEdit(self.groupBox_4)
        self.input_basecolor_mask.setObjectName(u"input_basecolor_mask")
        self.input_basecolor_mask.setMinimumSize(QSize(350, 0))
        self.input_basecolor_mask.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_5.addWidget(self.input_basecolor_mask)

        self.toolButton_10 = QToolButton(self.groupBox_4)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setMinimumSize(QSize(32, 0))

        self.horizontalLayout_5.addWidget(self.toolButton_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.input_normal_mask = QLineEdit(self.groupBox_4)
        self.input_normal_mask.setObjectName(u"input_normal_mask")
        self.input_normal_mask.setMinimumSize(QSize(350, 0))
        self.input_normal_mask.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout.addWidget(self.input_normal_mask)

        self.toolButton_7 = QToolButton(self.groupBox_4)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setMinimumSize(QSize(32, 0))

        self.horizontalLayout.addWidget(self.toolButton_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

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
        self.texture_channel_picker.setGeometry(QRect(10, 70, 531, 169))
        self.formLayout = QFormLayout(self.texture_channel_picker)
        self.formLayout.setObjectName(u"formLayout")
        self.image_preview = QGraphicsView(self.texture_channel_picker)
        self.image_preview.setObjectName(u"image_preview")
        self.image_preview.setMinimumSize(QSize(128, 128))
        self.image_preview.setMaximumSize(QSize(128, 128))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.image_preview)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.texture_output_mask = QLineEdit(self.texture_channel_picker)
        self.texture_output_mask.setObjectName(u"texture_output_mask")
        self.texture_output_mask.setMinimumSize(QSize(256, 0))

        self.horizontalLayout_10.addWidget(self.texture_output_mask)

        self.comboBox = QComboBox(self.texture_channel_picker)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_10.addWidget(self.comboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.red_enable = QCheckBox(self.texture_channel_picker)
        self.red_enable.setObjectName(u"red_enable")

        self.horizontalLayout_6.addWidget(self.red_enable)

        self.label_3 = QLabel(self.texture_channel_picker)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.red_channel_file = QComboBox(self.texture_channel_picker)
        self.red_channel_file.setObjectName(u"red_channel_file")
        self.red_channel_file.setMinimumSize(QSize(256, 0))

        self.horizontalLayout_6.addWidget(self.red_channel_file)

        self.red_channel_list = QComboBox(self.texture_channel_picker)
        self.red_channel_list.setObjectName(u"red_channel_list")
        self.red_channel_list.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_6.addWidget(self.red_channel_list)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.green_enable = QCheckBox(self.texture_channel_picker)
        self.green_enable.setObjectName(u"green_enable")

        self.horizontalLayout_7.addWidget(self.green_enable)

        self.label_4 = QLabel(self.texture_channel_picker)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.green_channel_file = QComboBox(self.texture_channel_picker)
        self.green_channel_file.setObjectName(u"green_channel_file")
        self.green_channel_file.setMinimumSize(QSize(256, 0))

        self.horizontalLayout_7.addWidget(self.green_channel_file)

        self.green_channel_list = QComboBox(self.texture_channel_picker)
        self.green_channel_list.setObjectName(u"green_channel_list")
        self.green_channel_list.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_7.addWidget(self.green_channel_list)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.blue_enable = QCheckBox(self.texture_channel_picker)
        self.blue_enable.setObjectName(u"blue_enable")

        self.horizontalLayout_8.addWidget(self.blue_enable)

        self.label_5 = QLabel(self.texture_channel_picker)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.blue_channel_file = QComboBox(self.texture_channel_picker)
        self.blue_channel_file.setObjectName(u"blue_channel_file")
        self.blue_channel_file.setMinimumSize(QSize(256, 0))

        self.horizontalLayout_8.addWidget(self.blue_channel_file)

        self.blue_channel_list = QComboBox(self.texture_channel_picker)
        self.blue_channel_list.setObjectName(u"blue_channel_list")
        self.blue_channel_list.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_8.addWidget(self.blue_channel_list)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.alpha_enable = QCheckBox(self.texture_channel_picker)
        self.alpha_enable.setObjectName(u"alpha_enable")

        self.horizontalLayout_9.addWidget(self.alpha_enable)

        self.label_11 = QLabel(self.texture_channel_picker)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.alpha_channel_file = QComboBox(self.texture_channel_picker)
        self.alpha_channel_file.setObjectName(u"alpha_channel_file")
        self.alpha_channel_file.setMinimumSize(QSize(256, 0))

        self.horizontalLayout_9.addWidget(self.alpha_channel_file)

        self.alpha_channel_list = QComboBox(self.texture_channel_picker)
        self.alpha_channel_list.setObjectName(u"alpha_channel_list")
        self.alpha_channel_list.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_9.addWidget(self.alpha_channel_list)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_3)

        self.minus_button = QPushButton(self.groupBox_2)
        self.minus_button.setObjectName(u"minus_button")
        self.minus_button.setGeometry(QRect(470, 260, 61, 31))
        self.plus_button = QPushButton(self.groupBox_2)
        self.plus_button.setObjectName(u"plus_button")
        self.plus_button.setGeometry(QRect(470, 300, 61, 31))
        self.tableView = QTableView(Main_ui)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 380, 1091, 192))
        self.scan_button = QPushButton(Main_ui)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setGeometry(QRect(20, 640, 321, 71))
        self.start_button = QPushButton(Main_ui)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(660, 650, 451, 71))

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
        self.label_9.setText(QCoreApplication.translate("Main_ui", u"Metalness", None))
        self.toolButton_9.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label_6.setText(QCoreApplication.translate("Main_ui", u"Height", None))
        self.toolButton_6.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label_8.setText(QCoreApplication.translate("Main_ui", u"Roughness", None))
        self.toolButton_8.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label_10.setText(QCoreApplication.translate("Main_ui", u"Base Color", None))
        self.toolButton_10.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.label_7.setText(QCoreApplication.translate("Main_ui", u"Normal", None))
        self.toolButton_7.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Main_ui", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Main_ui", u"\u041f\u0443\u0442\u044c \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.export_path_button.setText(QCoreApplication.translate("Main_ui", u"...", None))
        self.texture_channel_picker.setTitle(QCoreApplication.translate("Main_ui", u"Texture 1", None))
        self.red_enable.setText("")
        self.label_3.setText(QCoreApplication.translate("Main_ui", u"R", None))
        self.green_enable.setText("")
        self.label_4.setText(QCoreApplication.translate("Main_ui", u"G", None))
        self.blue_enable.setText("")
        self.label_5.setText(QCoreApplication.translate("Main_ui", u"B", None))
        self.alpha_enable.setText("")
        self.label_11.setText(QCoreApplication.translate("Main_ui", u"A", None))
        self.minus_button.setText(QCoreApplication.translate("Main_ui", u"-", None))
        self.plus_button.setText(QCoreApplication.translate("Main_ui", u"+", None))
        self.scan_button.setText(QCoreApplication.translate("Main_ui", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.start_button.setText(QCoreApplication.translate("Main_ui", u"\u0421\u0442\u0430\u0440\u0442", None))
    # retranslateUi

