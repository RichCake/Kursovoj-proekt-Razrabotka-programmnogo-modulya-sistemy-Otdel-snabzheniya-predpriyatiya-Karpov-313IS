# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_request.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Request(object):
    def setupUi(self, Request):
        if not Request.objectName():
            Request.setObjectName(u"Request")
        Request.resize(807, 564)
        self.verticalLayout = QVBoxLayout(Request)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.save_btn = QPushButton(Request)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_3.addWidget(self.save_btn)

        self.delete_btn = QPushButton(Request)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout_3.addWidget(self.delete_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.close_btn = QPushButton(Request)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Request)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.date_lbl = QLabel(Request)
        self.date_lbl.setObjectName(u"date_lbl")

        self.horizontalLayout_4.addWidget(self.date_lbl)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Request)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.status_lbl = QLabel(Request)
        self.status_lbl.setObjectName(u"status_lbl")

        self.horizontalLayout_5.addWidget(self.status_lbl)

        self.send_btn = QPushButton(Request)
        self.send_btn.setObjectName(u"send_btn")

        self.horizontalLayout_5.addWidget(self.send_btn)

        self.accept_viewer_btn = QPushButton(Request)
        self.accept_viewer_btn.setObjectName(u"accept_viewer_btn")

        self.horizontalLayout_5.addWidget(self.accept_viewer_btn)

        self.label_4 = QLabel(Request)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.category_combobox = QComboBox(Request)
        self.category_combobox.setObjectName(u"category_combobox")

        self.horizontalLayout_5.addWidget(self.category_combobox)

        self.category_dialog_btn = QPushButton(Request)
        self.category_dialog_btn.setObjectName(u"category_dialog_btn")

        self.horizontalLayout_5.addWidget(self.category_dialog_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Request)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setMargin(10)

        self.horizontalLayout.addWidget(self.label)

        self.description_text = QTextEdit(Request)
        self.description_text.setObjectName(u"description_text")

        self.horizontalLayout.addWidget(self.description_text)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_nomenclature_btn = QPushButton(Request)
        self.add_nomenclature_btn.setObjectName(u"add_nomenclature_btn")

        self.horizontalLayout_2.addWidget(self.add_nomenclature_btn)

        self.delete_nomenclature_btn = QPushButton(Request)
        self.delete_nomenclature_btn.setObjectName(u"delete_nomenclature_btn")
        self.delete_nomenclature_btn.setCheckable(False)
        self.delete_nomenclature_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.delete_nomenclature_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(Request)
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

        self.mark_done_btn = QPushButton(Request)
        self.mark_done_btn.setObjectName(u"mark_done_btn")

        self.verticalLayout.addWidget(self.mark_done_btn)


        self.retranslateUi(Request)

        QMetaObject.connectSlotsByName(Request)
    # setupUi

    def retranslateUi(self, Request):
        Request.setWindowTitle(QCoreApplication.translate("Request", u"Form", None))
        self.save_btn.setText(QCoreApplication.translate("Request", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.delete_btn.setText(QCoreApplication.translate("Request", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("Request", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Request", u"\u0421\u043e\u0437\u0434\u0430\u043d\u043e:", None))
        self.date_lbl.setText("")
        self.label_3.setText(QCoreApplication.translate("Request", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.status_lbl.setText("")
        self.send_btn.setText(QCoreApplication.translate("Request", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c...", None))
        self.accept_viewer_btn.setText(QCoreApplication.translate("Request", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.label_4.setText(QCoreApplication.translate("Request", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.category_dialog_btn.setText(QCoreApplication.translate("Request", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.label.setText(QCoreApplication.translate("Request", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.description_text.setPlaceholderText(QCoreApplication.translate("Request", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438...", None))
        self.add_nomenclature_btn.setText(QCoreApplication.translate("Request", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_nomenclature_btn.setText(QCoreApplication.translate("Request", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Request", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Request", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Request", u"\u0415\u0434. \u0438\u0437\u043c.", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Request", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
        self.mark_done_btn.setText(QCoreApplication.translate("Request", u"\u041f\u043e\u043c\u0435\u0442\u0438\u0442\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u043c", None))
    # retranslateUi

