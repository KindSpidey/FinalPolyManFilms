# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profilePerson.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(775, 458)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/logo3.png"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.logo)
        self.nameHead = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nameHead.setFont(font)
        self.nameHead.setFrameShape(QtWidgets.QFrame.Panel)
        self.nameHead.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.nameHead.setObjectName("nameHead")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameHead)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.moviesTable = QtWidgets.QTableWidget(self.widget)
        self.moviesTable.setObjectName("moviesTable")
        self.moviesTable.setColumnCount(2)
        self.moviesTable.setRowCount(0)
        self.header = self.moviesTable.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()
        self.moviesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.moviesTable.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.moviesTable, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.phone = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.phone.setFont(font)
        self.phone.setObjectName("phone")
        self.gridLayout_2.addWidget(self.phone, 3, 0, 1, 1)
        self.email = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.email.setFrameShadow(QtWidgets.QFrame.Plain)
        self.email.setObjectName("email")
        self.gridLayout_2.addWidget(self.email, 0, 0, 1, 1)
        self.averageSalary = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.averageSalary.setFont(font)
        self.averageSalary.setObjectName("averageSalary")
        self.gridLayout_2.addWidget(self.averageSalary, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.editButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.editButton.setFont(font)
        self.editButton.setDefault(True)
        self.editButton.setFlat(False)
        self.editButton.setObjectName("editButton")
        self.gridLayout_2.addWidget(self.editButton, 0, 1, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_8)
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nameHead.setText(_translate("Form", "Человек"))
        item = self.moviesTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Фильм"))
        item = self.moviesTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Гонорар"))
        self.label_7.setText(_translate("Form", "Фильмы"))
        self.phone.setText(_translate("Form", "Телефон"))
        self.email.setText(_translate("Form", "e-mail"))
        self.averageSalary.setText(_translate("Form", "Средняя зарплата"))
        self.editButton.setText(_translate("Form", "Редактировать"))
