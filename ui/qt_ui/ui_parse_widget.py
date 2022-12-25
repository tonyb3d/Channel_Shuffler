# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_parse_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_ParseWidget(object):
    def setupUi(self, ParseWidget):
        if not ParseWidget.objectName():
            ParseWidget.setObjectName(u"ParseWidget")
        ParseWidget.resize(519, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ParseWidget.sizePolicy().hasHeightForWidth())
        ParseWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Iosevka"])
        font.setPointSize(10)
        ParseWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(ParseWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(ParseWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mapName = QLineEdit(self.groupBox)
        self.mapName.setObjectName(u"mapName")
        sizePolicy.setHeightForWidth(self.mapName.sizePolicy().hasHeightForWidth())
        self.mapName.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.mapName)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.mapMask = QLineEdit(self.groupBox)
        self.mapMask.setObjectName(u"mapMask")

        self.horizontalLayout.addWidget(self.mapMask)

        self.mapPathButton = QToolButton(self.groupBox)
        self.mapPathButton.setObjectName(u"mapPathButton")

        self.horizontalLayout.addWidget(self.mapPathButton)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.deleteButton = QPushButton(self.groupBox)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(ParseWidget)

        QMetaObject.connectSlotsByName(ParseWidget)
    # setupUi

    def retranslateUi(self, ParseWidget):
        ParseWidget.setWindowTitle(QCoreApplication.translate("ParseWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("ParseWidget", u"GroupBox", None))
        self.mapPathButton.setText(QCoreApplication.translate("ParseWidget", u"...", None))
        self.deleteButton.setText(QCoreApplication.translate("ParseWidget", u"Delete", None))
    # retranslateUi

