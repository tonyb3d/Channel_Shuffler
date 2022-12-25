# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_constructor_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGraphicsView,
    QGridLayout, QGroupBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_ConstructorWidget(object):
    def setupUi(self, ConstructorWidget):
        if not ConstructorWidget.objectName():
            ConstructorWidget.setObjectName(u"ConstructorWidget")
        ConstructorWidget.resize(617, 179)
        self.horizontalLayout_2 = QHBoxLayout(ConstructorWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.texture_channel_picker = QGroupBox(ConstructorWidget)
        self.texture_channel_picker.setObjectName(u"texture_channel_picker")
        self.horizontalLayout = QHBoxLayout(self.texture_channel_picker)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imagePreview = QGraphicsView(self.texture_channel_picker)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setMinimumSize(QSize(128, 128))
        self.imagePreview.setMaximumSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.imagePreview)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.blue_channel_file = QComboBox(self.texture_channel_picker)
        self.blue_channel_file.setObjectName(u"blue_channel_file")
        self.blue_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.blue_channel_file, 3, 1, 1, 1)

        self.alpha_channel_list = QComboBox(self.texture_channel_picker)
        self.alpha_channel_list.setObjectName(u"alpha_channel_list")
        self.alpha_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.alpha_channel_list, 4, 2, 1, 1)

        self.blue_channel_list = QComboBox(self.texture_channel_picker)
        self.blue_channel_list.setObjectName(u"blue_channel_list")
        self.blue_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.blue_channel_list, 3, 2, 1, 1)

        self.alpha_checkbox = QCheckBox(self.texture_channel_picker)
        self.alpha_checkbox.setObjectName(u"alpha_checkbox")

        self.gridLayout_2.addWidget(self.alpha_checkbox, 4, 0, 1, 1)

        self.alpha_channel_file = QComboBox(self.texture_channel_picker)
        self.alpha_channel_file.setObjectName(u"alpha_channel_file")
        self.alpha_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.alpha_channel_file, 4, 1, 1, 1)

        self.green_channel_list = QComboBox(self.texture_channel_picker)
        self.green_channel_list.setObjectName(u"green_channel_list")
        self.green_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.green_channel_list, 2, 2, 1, 1)

        self.green_checkbox = QCheckBox(self.texture_channel_picker)
        self.green_checkbox.setObjectName(u"green_checkbox")

        self.gridLayout_2.addWidget(self.green_checkbox, 2, 0, 1, 1)

        self.red_channel_list = QComboBox(self.texture_channel_picker)
        self.red_channel_list.setObjectName(u"red_channel_list")
        self.red_channel_list.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.red_channel_list, 1, 2, 1, 1)

        self.green_channel_file = QComboBox(self.texture_channel_picker)
        self.green_channel_file.setObjectName(u"green_channel_file")
        self.green_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.green_channel_file, 2, 1, 1, 1)

        self.blue_checkbox = QCheckBox(self.texture_channel_picker)
        self.blue_checkbox.setObjectName(u"blue_checkbox")

        self.gridLayout_2.addWidget(self.blue_checkbox, 3, 0, 1, 1)

        self.red_checkbox = QCheckBox(self.texture_channel_picker)
        self.red_checkbox.setObjectName(u"red_checkbox")

        self.gridLayout_2.addWidget(self.red_checkbox, 1, 0, 1, 1)

        self.red_channel_file = QComboBox(self.texture_channel_picker)
        self.red_channel_file.setObjectName(u"red_channel_file")
        self.red_channel_file.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.red_channel_file, 1, 1, 1, 1)

        self.texture_output_mask = QLineEdit(self.texture_channel_picker)
        self.texture_output_mask.setObjectName(u"texture_output_mask")
        self.texture_output_mask.setMinimumSize(QSize(256, 0))

        self.gridLayout_2.addWidget(self.texture_output_mask, 0, 1, 1, 1)

        self.filetype_combobox = QComboBox(self.texture_channel_picker)
        self.filetype_combobox.setObjectName(u"filetype_combobox")
        self.filetype_combobox.setMinimumSize(QSize(64, 0))

        self.gridLayout_2.addWidget(self.filetype_combobox, 0, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.deleteButton = QPushButton(self.texture_channel_picker)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QSize(0, 0))
        self.deleteButton.setFlat(False)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.horizontalLayout_2.addWidget(self.texture_channel_picker)


        self.retranslateUi(ConstructorWidget)

        self.deleteButton.setDefault(False)


        QMetaObject.connectSlotsByName(ConstructorWidget)
    # setupUi

    def retranslateUi(self, ConstructorWidget):
        ConstructorWidget.setWindowTitle(QCoreApplication.translate("ConstructorWidget", u"Form", None))
        self.texture_channel_picker.setTitle(QCoreApplication.translate("ConstructorWidget", u"Texture 1", None))
        self.alpha_checkbox.setText(QCoreApplication.translate("ConstructorWidget", u"A", None))
        self.green_checkbox.setText(QCoreApplication.translate("ConstructorWidget", u"G", None))
        self.blue_checkbox.setText(QCoreApplication.translate("ConstructorWidget", u"B", None))
        self.red_checkbox.setText(QCoreApplication.translate("ConstructorWidget", u"R", None))
        self.deleteButton.setText(QCoreApplication.translate("ConstructorWidget", u"Delete", None))
    # retranslateUi

