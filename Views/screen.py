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
        font1 = QFont()
        font1.setPointSize(11)
        self.label_template_file.setFont(font1)
        self.label_template_file.setAlignment(Qt.AlignCenter)

        self.verticalLayout_template.addWidget(self.label_template_file)

        self.button_template = QPushButton(Form)
        self.button_template.setObjectName(u"button_template")
        self.button_template.setAcceptDrops(True)

        self.verticalLayout_template.addWidget(self.button_template)


        self.horizontalLayout_selector.addLayout(self.verticalLayout_template)

        self.verticalLayout_data = QVBoxLayout()
        self.verticalLayout_data.setObjectName(u"verticalLayout_data")
        self.label_data_file = QLabel(Form)
        self.label_data_file.setObjectName(u"label_data_file")
        self.label_data_file.setFont(font1)
        self.label_data_file.setAlignment(Qt.AlignCenter)

        self.verticalLayout_data.addWidget(self.label_data_file)

        self.button_data = QPushButton(Form)
        self.button_data.setObjectName(u"button_data")
        self.button_data.setAcceptDrops(True)

        self.verticalLayout_data.addWidget(self.button_data)


        self.horizontalLayout_selector.addLayout(self.verticalLayout_data)

        self.verticalLayout_destination = QVBoxLayout()
        self.verticalLayout_destination.setObjectName(u"verticalLayout_destination")
        self.label_destination_file = QLabel(Form)
        self.label_destination_file.setObjectName(u"label_destination_file")
        self.label_destination_file.setFont(font1)
        self.label_destination_file.setAlignment(Qt.AlignCenter)

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
        font2 = QFont()
        font2.setPointSize(12)
        self.label_ready.setFont(font2)
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
        self.label_data_file.setText("")
        self.button_data.setText(QCoreApplication.translate("Form", u"Select data file", None))
        self.label_destination_file.setText("")
        self.button_destination.setText(QCoreApplication.translate("Form", u"Select destination file", None))
        self.label_ready.setText(QCoreApplication.translate("Form", u"Everything's set? Click on the \"Generate!\" button below.", None))
        self.button_generate.setText(QCoreApplication.translate("Form", u"Generate!", None))
    # retranslateUi

