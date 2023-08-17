# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_version_ui.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(537, 400)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Proj_LB = QLabel(Dialog)
        self.Proj_LB.setObjectName(u"Proj_LB")

        self.horizontalLayout_2.addWidget(self.Proj_LB)

        self.Proj_CBx = QComboBox(Dialog)
        self.Proj_CBx.setObjectName(u"Proj_CBx")

        self.horizontalLayout_2.addWidget(self.Proj_CBx)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.Ok_Cancel_BBx = QDialogButtonBox(Dialog)
        self.Ok_Cancel_BBx.setObjectName(u"Ok_Cancel_BBx")
        self.Ok_Cancel_BBx.setOrientation(Qt.Vertical)
        self.Ok_Cancel_BBx.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.Ok_Cancel_BBx.setCenterButtons(False)

        self.gridLayout.addWidget(self.Ok_Cancel_BBx, 0, 1, 2, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Shot_LB = QLabel(Dialog)
        self.Shot_LB.setObjectName(u"Shot_LB")

        self.horizontalLayout_3.addWidget(self.Shot_LB)

        self.Shot_CBx = QComboBox(Dialog)
        self.Shot_CBx.setObjectName(u"Shot_CBx")

        self.horizontalLayout_3.addWidget(self.Shot_CBx)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.task_CBx = QComboBox(Dialog)
        self.task_CBx.setObjectName(u"task_CBx")

        self.horizontalLayout_4.addWidget(self.task_CBx)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vers_LB = QLabel(Dialog)
        self.vers_LB.setObjectName(u"vers_LB")

        self.horizontalLayout.addWidget(self.vers_LB)

        self.vers_LE = QLineEdit(Dialog)
        self.vers_LE.setObjectName(u"vers_LE")

        self.horizontalLayout.addWidget(self.vers_LE)

        self.vers_TB = QToolButton(Dialog)
        self.vers_TB.setObjectName(u"vers_TB")

        self.horizontalLayout.addWidget(self.vers_TB)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Ver_name_LB = QLabel(Dialog)
        self.Ver_name_LB.setObjectName(u"Ver_name_LB")

        self.horizontalLayout_5.addWidget(self.Ver_name_LB)

        self.Ver_name_LE = QLineEdit(Dialog)
        self.Ver_name_LE.setObjectName(u"Ver_name_LE")

        self.horizontalLayout_5.addWidget(self.Ver_name_LE)


        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.desc_LB = QLabel(Dialog)
        self.desc_LB.setObjectName(u"desc_LB")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_LB.sizePolicy().hasHeightForWidth())
        self.desc_LB.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.desc_LB)

        self.desc_TE = QTextEdit(Dialog)
        self.desc_TE.setObjectName(u"desc_TE")

        self.horizontalLayout_6.addWidget(self.desc_TE)


        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.Ok_Cancel_BBx.accepted.connect(Dialog.accept)
        self.Ok_Cancel_BBx.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Proj_LB.setText(QCoreApplication.translate("Dialog", u"Project :", None))
        self.Shot_LB.setText(QCoreApplication.translate("Dialog", u"Shot : ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Task :", None))
        self.vers_LB.setText(QCoreApplication.translate("Dialog", u"Version Path :", None))
        self.vers_TB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.Ver_name_LB.setText(QCoreApplication.translate("Dialog", u"Version Name:", None))
        self.desc_LB.setText(QCoreApplication.translate("Dialog", u"Description :", None))
    # retranslateUi

