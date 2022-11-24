# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mapwidget.ui'
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

class Ui_MapWidget(object):
    def setupUi(self, MapWidget):
        if not MapWidget.objectName():
            MapWidget.setObjectName(u"MapWidget")
        MapWidget.resize(707, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapWidget.sizePolicy().hasHeightForWidth())
        MapWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Iosevka"])
        font.setPointSize(10)
        MapWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(MapWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(MapWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
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

        self.toolButton = QToolButton(self.groupBox)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(MapWidget)

        QMetaObject.connectSlotsByName(MapWidget)
    # setupUi

    def retranslateUi(self, MapWidget):
        MapWidget.setWindowTitle(QCoreApplication.translate("MapWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("MapWidget", u"GroupBox", None))
        self.toolButton.setText(QCoreApplication.translate("MapWidget", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MapWidget", u"Delete", None))
    # retranslateUi

