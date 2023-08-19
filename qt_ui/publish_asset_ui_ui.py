# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'publish_asset_ui.ui'
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
        self.Asset_LB = QLabel(Dialog)
        self.Asset_LB.setObjectName(u"Asset_LB")

        self.horizontalLayout_3.addWidget(self.Asset_LB)

        self.Asset_CBx = QComboBox(Dialog)
        self.Asset_CBx.setObjectName(u"Asset_CBx")

        self.horizontalLayout_3.addWidget(self.Asset_CBx)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.asset_type = QLabel(Dialog)
        self.asset_type.setObjectName(u"asset_type")

        self.horizontalLayout_4.addWidget(self.asset_type)

        self.asset_type_CBx = QComboBox(Dialog)
        self.asset_type_CBx.setObjectName(u"asset_type_CBx")

        self.horizontalLayout_4.addWidget(self.asset_type_CBx)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.asset_path_LB = QLabel(Dialog)
        self.asset_path_LB.setObjectName(u"asset_path_LB")

        self.horizontalLayout.addWidget(self.asset_path_LB)

        self.asset_path_LE = QLineEdit(Dialog)
        self.asset_path_LE.setObjectName(u"asset_path_LE")

        self.horizontalLayout.addWidget(self.asset_path_LE)

        self.asset_path_TB = QToolButton(Dialog)
        self.asset_path_TB.setObjectName(u"asset_path_TB")

        self.horizontalLayout.addWidget(self.asset_path_TB)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.asset_name_LB = QLabel(Dialog)
        self.asset_name_LB.setObjectName(u"asset_name_LB")

        self.horizontalLayout_5.addWidget(self.asset_name_LB)

        self.asset_name_LE = QLineEdit(Dialog)
        self.asset_name_LE.setObjectName(u"asset_name_LE")

        self.horizontalLayout_5.addWidget(self.asset_name_LE)


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
        self.Asset_LB.setText(QCoreApplication.translate("Dialog", u"Asset :", None))
        self.asset_type.setText(QCoreApplication.translate("Dialog", u"Type :", None))
        self.asset_path_LB.setText(QCoreApplication.translate("Dialog", u"Asset Path :", None))
        self.asset_path_TB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.asset_name_LB.setText(QCoreApplication.translate("Dialog", u"Asset Name:", None))
        self.desc_LB.setText(QCoreApplication.translate("Dialog", u"Description :", None))
    # retranslateUi

