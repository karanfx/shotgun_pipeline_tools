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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1393, 937)
        self.action_publish_version = QAction(MainWindow)
        self.action_publish_version.setObjectName(u"action_publish_version")
        self.action_publish_assets = QAction(MainWindow)
        self.action_publish_assets.setObjectName(u"action_publish_assets")
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionReport = QAction(MainWindow)
        self.actionReport.setObjectName(u"actionReport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Launch_PB = QPushButton(self.centralwidget)
        self.Launch_PB.setObjectName(u"Launch_PB")
        self.Launch_PB.setGeometry(QRect(1240, 860, 121, 31))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(180, 40, 20, 731))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(410, 40, 20, 731))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-10, 770, 1401, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1090, 820, 271, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.soft_LB = QLabel(self.layoutWidget)
        self.soft_LB.setObjectName(u"soft_LB")

        self.horizontalLayout.addWidget(self.soft_LB)

        self.soft_CB = QComboBox(self.layoutWidget)
        self.soft_CB.setObjectName(u"soft_CB")

        self.horizontalLayout.addWidget(self.soft_CB)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(200, 40, 201, 721))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.seq_LB = QLabel(self.layoutWidget1)
        self.seq_LB.setObjectName(u"seq_LB")

        self.verticalLayout_2.addWidget(self.seq_LB)

        self.seq_lW = QListWidget(self.layoutWidget1)
        QListWidgetItem(self.seq_lW)
        self.seq_lW.setObjectName(u"seq_lW")

        self.verticalLayout_2.addWidget(self.seq_lW)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 40, 161, 721))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.proj_LB = QLabel(self.layoutWidget2)
        self.proj_LB.setObjectName(u"proj_LB")

        self.verticalLayout.addWidget(self.proj_LB)

        self.proj_lW = QListWidget(self.layoutWidget2)
        QListWidgetItem(self.proj_lW)
        self.proj_lW.setObjectName(u"proj_lW")

        self.verticalLayout.addWidget(self.proj_lW)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(680, 40, 701, 721))
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
        self.sel_task_LB.setGeometry(QRect(1090, 790, 271, 21))
        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 10, 170, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.user_LB = QLabel(self.layoutWidget4)
        self.user_LB.setObjectName(u"user_LB")

        self.horizontalLayout_2.addWidget(self.user_LB)

        self.user_LE = QLineEdit(self.layoutWidget4)
        self.user_LE.setObjectName(u"user_LE")

        self.horizontalLayout_2.addWidget(self.user_LE)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(430, 40, 221, 721))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.shot_LB = QLabel(self.layoutWidget_2)
        self.shot_LB.setObjectName(u"shot_LB")

        self.verticalLayout_4.addWidget(self.shot_LB)

        self.Shot_LW = QListWidget(self.layoutWidget_2)
        QListWidgetItem(self.Shot_LW)
        self.Shot_LW.setObjectName(u"Shot_LW")

        self.verticalLayout_4.addWidget(self.Shot_LW)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(660, 40, 20, 731))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.Reload_PB = QPushButton(self.centralwidget)
        self.Reload_PB.setObjectName(u"Reload_PB")
        self.Reload_PB.setGeometry(QRect(190, 10, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1393, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMenu.addAction(self.action_publish_version)
        self.menuMenu.addAction(self.action_publish_assets)
        self.menuMenu.addAction(self.action_quit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionReport)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_publish_version.setText(QCoreApplication.translate("MainWindow", u"Publish Version", None))
        self.action_publish_assets.setText(QCoreApplication.translate("MainWindow", u"Publish Assets", None))
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionReport.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.Launch_PB.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.soft_LB.setText(QCoreApplication.translate("MainWindow", u"Software :", None))
        self.seq_LB.setText(QCoreApplication.translate("MainWindow", u"Sequences:", None))

        __sortingEnabled = self.seq_lW.isSortingEnabled()
        self.seq_lW.setSortingEnabled(False)
        ___qlistwidgetitem = self.seq_lW.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Seq_000", None));
        self.seq_lW.setSortingEnabled(__sortingEnabled)

        self.proj_LB.setText(QCoreApplication.translate("MainWindow", u"Show/Project :", None))

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
        self.shot_LB.setText(QCoreApplication.translate("MainWindow", u"Shot :", None))

        __sortingEnabled3 = self.Shot_LW.isSortingEnabled()
        self.Shot_LW.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.Shot_LW.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"001_001", None));
        self.Shot_LW.setSortingEnabled(__sortingEnabled3)

        self.Reload_PB.setText(QCoreApplication.translate("MainWindow", u"Reload Tasks", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

