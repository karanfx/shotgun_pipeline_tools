# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1168, 937)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Launch_PB = QPushButton(self.centralwidget)
        self.Launch_PB.setObjectName(u"Launch_PB")
        self.Launch_PB.setGeometry(QRect(1030, 850, 121, 31))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(230, 40, 20, 731))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(500, 40, 20, 731))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-10, 770, 1181, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(900, 810, 251, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.soft_CB = QComboBox(self.layoutWidget)
        self.soft_CB.setObjectName(u"soft_CB")

        self.horizontalLayout.addWidget(self.soft_CB)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(250, 40, 251, 721))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.seq_lW = QListWidget(self.layoutWidget1)
        QListWidgetItem(self.seq_lW)
        self.seq_lW.setObjectName(u"seq_lW")

        self.verticalLayout_2.addWidget(self.seq_lW)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 40, 221, 721))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.proj_lW = QListWidget(self.layoutWidget2)
        QListWidgetItem(self.proj_lW)
        self.proj_lW.setObjectName(u"proj_lW")

        self.verticalLayout.addWidget(self.proj_lW)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(520, 40, 631, 721))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.task_treeWid = QTreeWidget(self.layoutWidget3)
        QTreeWidgetItem(self.task_treeWid)
        self.task_treeWid.setObjectName(u"task_treeWid")

        self.verticalLayout_3.addWidget(self.task_treeWid)

        self.sel_task_LB = QLabel(self.centralwidget)
        self.sel_task_LB.setObjectName(u"sel_task_LB")
        self.sel_task_LB.setGeometry(QRect(890, 790, 271, 21))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 170, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.user_LB = QLabel(self.widget)
        self.user_LB.setObjectName(u"user_LB")

        self.horizontalLayout_2.addWidget(self.user_LB)

        self.user_LE = QLineEdit(self.widget)
        self.user_LE.setObjectName(u"user_LE")

        self.horizontalLayout_2.addWidget(self.user_LE)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1168, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Launch_PB.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Software :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sequences:", None))

        __sortingEnabled = self.seq_lW.isSortingEnabled()
        self.seq_lW.setSortingEnabled(False)
        ___qlistwidgetitem = self.seq_lW.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Seq_000", None));
        self.seq_lW.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Show/Project :", None))

        __sortingEnabled1 = self.proj_lW.isSortingEnabled()
        self.proj_lW.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.proj_lW.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Show_01", None));
        self.proj_lW.setSortingEnabled(__sortingEnabled1)

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tasks :", None))
        ___qtreewidgetitem = self.task_treeWid.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Due Date", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Start Date", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Shot", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Tasks", None));

        __sortingEnabled2 = self.task_treeWid.isSortingEnabled()
        self.task_treeWid.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.task_treeWid.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Reload_Tasks", None));
        self.task_treeWid.setSortingEnabled(__sortingEnabled2)

        self.sel_task_LB.setText(QCoreApplication.translate("MainWindow", u"Selected Task :", None))
        self.user_LB.setText(QCoreApplication.translate("MainWindow", u"User :", None))
        self.user_LE.setText(QCoreApplication.translate("MainWindow", u"test", None))
    # retranslateUi

