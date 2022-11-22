# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(Form)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_selector = QHBoxLayout()
        self.horizontalLayout_selector.setObjectName(u"horizontalLayout_selector")
        self.verticalLayout_template = QVBoxLayout()
        self.verticalLayout_template.setSpacing(6)
        self.verticalLayout_template.setObjectName(u"verticalLayout_template")
        self.label_template_file = QLabel(Form)
        self.label_template_file.setObjectName(u"label_template_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_template_file.sizePolicy().hasHeightForWidth())
        self.label_template_file.setSizePolicy(sizePolicy1)

        self.verticalLayout_template.addWidget(self.label_template_file)

        self.button_template = QPushButton(Form)
        self.button_template.setObjectName(u"button_template")
        self.button_template.setAcceptDrops(True)

        self.verticalLayout_template.addWidget(self.button_template)


        self.horizontalLayout_selector.addLayout(self.verticalLayout_template)

        self.verticalLayout_invoice = QVBoxLayout()
        self.verticalLayout_invoice.setObjectName(u"verticalLayout_invoice")
        self.label_invoice_file = QLabel(Form)
        self.label_invoice_file.setObjectName(u"label_invoice_file")

        self.verticalLayout_invoice.addWidget(self.label_invoice_file)

        self.button_invoice = QPushButton(Form)
        self.button_invoice.setObjectName(u"button_invoice")
        self.button_invoice.setAcceptDrops(True)

        self.verticalLayout_invoice.addWidget(self.button_invoice)


        self.horizontalLayout_selector.addLayout(self.verticalLayout_invoice)

        self.verticalLayout_destination = QVBoxLayout()
        self.verticalLayout_destination.setObjectName(u"verticalLayout_destination")
        self.label_destination_file = QLabel(Form)
        self.label_destination_file.setObjectName(u"label_destination_file")

        self.verticalLayout_destination.addWidget(self.label_destination_file)

        self.button_destination = QPushButton(Form)
        self.button_destination.setObjectName(u"button_destination")
        self.button_destination.setAcceptDrops(True)

        self.verticalLayout_destination.addWidget(self.button_destination)


        self.horizontalLayout_selector.addLayout(self.verticalLayout_destination)


        self.verticalLayout.addLayout(self.horizontalLayout_selector)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_ready = QLabel(Form)
        self.label_ready.setObjectName(u"label_ready")
        sizePolicy1.setHeightForWidth(self.label_ready.sizePolicy().hasHeightForWidth())
        self.label_ready.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        self.label_ready.setFont(font1)
        self.label_ready.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_ready)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.button_generate = QPushButton(Form)
        self.button_generate.setObjectName(u"button_generate")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_generate.sizePolicy().hasHeightForWidth())
        self.button_generate.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.button_generate, 0, Qt.AlignRight)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("Form", u"Invoice generator", None))
        self.label_template_file.setText("")
        self.button_template.setText(QCoreApplication.translate("Form", u"Select template file", None))
        self.label_invoice_file.setText("")
        self.button_invoice.setText(QCoreApplication.translate("Form", u"Select data file", None))
        self.label_destination_file.setText("")
        self.button_destination.setText(QCoreApplication.translate("Form", u"Select destination file", None))
        self.label_ready.setText(QCoreApplication.translate("Form", u"Everything's set? Click on the \"Generate!\" button below.", None))
        self.button_generate.setText(QCoreApplication.translate("Form", u"Generate!", None))
    # retranslateUi

