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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 900)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.save_preset = QAction(MainWindow)
        self.save_preset.setObjectName(u"save_preset")
        self.load_preset = QAction(MainWindow)
        self.load_preset.setObjectName(u"load_preset")
        self.reset_preset = QAction(MainWindow)
        self.reset_preset.setObjectName(u"reset_preset")
        self.help = QAction(MainWindow)
        self.help.setObjectName(u"help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.import_path_lineedit = QLineEdit(self.groupBox_2)
        self.import_path_lineedit.setObjectName(u"import_path_lineedit")

        self.horizontalLayout_3.addWidget(self.import_path_lineedit)

        self.import_path_button = QToolButton(self.groupBox_2)
        self.import_path_button.setObjectName(u"import_path_button")

        self.horizontalLayout_3.addWidget(self.import_path_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.subfolder_search_checkbox = QCheckBox(self.groupBox_2)
        self.subfolder_search_checkbox.setObjectName(u"subfolder_search_checkbox")

        self.verticalLayout.addWidget(self.subfolder_search_checkbox)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.scrollArea = QScrollArea(self.groupBox_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 685, 522))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.parse_widget_listwidget = QListWidget(self.scrollAreaWidgetContents)
        self.parse_widget_listwidget.setObjectName(u"parse_widget_listwidget")

        self.verticalLayout_5.addWidget(self.parse_widget_listwidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.parser_add_button = QPushButton(self.groupBox_2)
        self.parser_add_button.setObjectName(u"parser_add_button")

        self.horizontalLayout_2.addWidget(self.parser_add_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.parser_start_button = QPushButton(self.groupBox_2)
        self.parser_start_button.setObjectName(u"parser_start_button")

        self.horizontalLayout_2.addWidget(self.parser_start_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.parser_clear_button = QPushButton(self.groupBox_2)
        self.parser_clear_button.setObjectName(u"parser_clear_button")

        self.horizontalLayout_2.addWidget(self.parser_clear_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.export_path_lineedit = QLineEdit(self.groupBox)
        self.export_path_lineedit.setObjectName(u"export_path_lineedit")

        self.horizontalLayout_4.addWidget(self.export_path_lineedit)

        self.export_path_button = QToolButton(self.groupBox)
        self.export_path_button.setObjectName(u"export_path_button")

        self.horizontalLayout_4.addWidget(self.export_path_button)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.subfolder_create_checkbox = QCheckBox(self.groupBox)
        self.subfolder_create_checkbox.setObjectName(u"subfolder_create_checkbox")

        self.horizontalLayout_10.addWidget(self.subfolder_create_checkbox)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_10.addWidget(self.checkBox)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.scrollArea_2 = QScrollArea(self.groupBox)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 685, 520))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.texture_constructor_listwidget = QListWidget(self.scrollAreaWidgetContents_2)
        self.texture_constructor_listwidget.setObjectName(u"texture_constructor_listwidget")

        self.verticalLayout_9.addWidget(self.texture_constructor_listwidget)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.constructor_add_button = QPushButton(self.groupBox)
        self.constructor_add_button.setObjectName(u"constructor_add_button")

        self.horizontalLayout_5.addWidget(self.constructor_add_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.constructor_start_button = QPushButton(self.groupBox)
        self.constructor_start_button.setObjectName(u"constructor_start_button")

        self.horizontalLayout_5.addWidget(self.constructor_start_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.constructor_clear_button = QPushButton(self.groupBox)
        self.constructor_clear_button.setObjectName(u"constructor_clear_button")

        self.horizontalLayout_5.addWidget(self.constructor_clear_button)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        self.tableView.setMinimumSize(QSize(0, 100))

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 21))
        self.Main_menu = QMenu(self.menubar)
        self.Main_menu.setObjectName(u"Main_menu")
        self.Presets_menu = QMenu(self.menubar)
        self.Presets_menu.setObjectName(u"Presets_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.Main_menu.menuAction())
        self.menubar.addAction(self.Presets_menu.menuAction())
        self.Main_menu.addAction(self.help)
        self.Presets_menu.addAction(self.save_preset)
        self.Presets_menu.addAction(self.load_preset)
        self.Presets_menu.addAction(self.reset_preset)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0440\u0435\u0441\u0435\u0442", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u0440\u0435\u0441\u0435\u0442", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.save_preset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0440\u0435\u0441\u0435\u0442", None))
        self.load_preset.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u0440\u0435\u0441\u0435\u0442", None))
        self.reset_preset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u0438\u043c\u043f\u043e\u0440\u0442\u0430", None))
        self.import_path_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.subfolder_search_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0432 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u0445", None))
        self.parser_add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.parser_start_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0441\u0438\u043d\u0433", None))
        self.parser_clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.export_path_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.subfolder_create_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0432\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.constructor_add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.constructor_start_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.constructor_clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.Main_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.Presets_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0441\u0435\u0442\u044b", None))
    # retranslateUi

