# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_request.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Create_request(object):
    def setupUi(self, Create_request):
        if not Create_request.objectName():
            Create_request.setObjectName(u"Create_request")
        Create_request.resize(538, 345)
        self.verticalLayout = QVBoxLayout(Create_request)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu_btn = QPushButton(Create_request)
        self.menu_btn.setObjectName(u"menu_btn")

        self.horizontalLayout_3.addWidget(self.menu_btn)

        self.save_btn = QPushButton(Create_request)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_3.addWidget(self.save_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Create_request)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setMargin(10)

        self.horizontalLayout.addWidget(self.label)

        self.description_text = QTextEdit(Create_request)
        self.description_text.setObjectName(u"description_text")

        self.horizontalLayout.addWidget(self.description_text)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_nomenclature_btn = QPushButton(Create_request)
        self.add_nomenclature_btn.setObjectName(u"add_nomenclature_btn")

        self.horizontalLayout_2.addWidget(self.add_nomenclature_btn)

        self.delete_nomenclature_btn = QPushButton(Create_request)
        self.delete_nomenclature_btn.setObjectName(u"delete_nomenclature_btn")

        self.horizontalLayout_2.addWidget(self.delete_nomenclature_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(Create_request)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Create_request)

        QMetaObject.connectSlotsByName(Create_request)
    # setupUi

    def retranslateUi(self, Create_request):
        Create_request.setWindowTitle(QCoreApplication.translate("Create_request", u"Form", None))
        self.menu_btn.setText(QCoreApplication.translate("Create_request", u"\u041c\u0435\u043d\u044e", None))
        self.save_btn.setText(QCoreApplication.translate("Create_request", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Create_request", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.description_text.setPlaceholderText(QCoreApplication.translate("Create_request", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438...", None))
        self.add_nomenclature_btn.setText(QCoreApplication.translate("Create_request", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_nomenclature_btn.setText(QCoreApplication.translate("Create_request", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Create_request", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Create_request", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Create_request", u"\u0415\u0434. \u0438\u0437\u043c.", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Create_request", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
    # retranslateUi
