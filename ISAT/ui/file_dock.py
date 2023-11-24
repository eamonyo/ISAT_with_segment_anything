# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/disk2/PycharmProjects/ISAT_with_segment_anything/ISAT/ui/file_dock.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(264, 341)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.widget_state = QtWidgets.QWidget(Form)
        self.widget_state.setObjectName("widget_state")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_state)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_prev_state = QtWidgets.QLabel(self.widget_state)
        self.label_prev_state.setMaximumSize(QtCore.QSize(16777215, 3))
        self.label_prev_state.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.label_prev_state.setText("")
        self.label_prev_state.setObjectName("label_prev_state")
        self.horizontalLayout_2.addWidget(self.label_prev_state)
        self.label_current_state = QtWidgets.QLabel(self.widget_state)
        self.label_current_state.setMaximumSize(QtCore.QSize(16777215, 3))
        self.label_current_state.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.label_current_state.setText("")
        self.label_current_state.setObjectName("label_current_state")
        self.horizontalLayout_2.addWidget(self.label_current_state)
        self.label_next_state = QtWidgets.QLabel(self.widget_state)
        self.label_next_state.setMinimumSize(QtCore.QSize(50, 0))
        self.label_next_state.setMaximumSize(QtCore.QSize(16777215, 3))
        self.label_next_state.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.label_next_state.setText("")
        self.label_next_state.setObjectName("label_next_state")
        self.horizontalLayout_2.addWidget(self.label_next_state)
        self.verticalLayout.addWidget(self.widget_state)
        self.widget_num = QtWidgets.QWidget(Form)
        self.widget_num.setObjectName("widget_num")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_num)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_jump = QtWidgets.QLineEdit(self.widget_num)
        self.lineEdit_jump.setObjectName("lineEdit_jump")
        self.horizontalLayout.addWidget(self.lineEdit_jump)
        self.label_current = QtWidgets.QLabel(self.widget_num)
        self.label_current.setText("")
        self.label_current.setObjectName("label_current")
        self.horizontalLayout.addWidget(self.label_current)
        self.label = QtWidgets.QLabel(self.widget_num)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_all = QtWidgets.QLabel(self.widget_num)
        self.label_all.setText("")
        self.label_all.setObjectName("label_all")
        self.horizontalLayout.addWidget(self.label_all)
        self.verticalLayout.addWidget(self.widget_num)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_prev_state.setStatusTip(_translate("Form", "Prev image SAM state"))
        self.label_prev_state.setWhatsThis(_translate("Form", "Prev image SAM state."))
        self.label_current_state.setStatusTip(_translate("Form", "Current image SAM state"))
        self.label_current_state.setWhatsThis(_translate("Form", "Current image SAM state."))
        self.label_next_state.setStatusTip(_translate("Form", "Next image SAM state"))
        self.label_next_state.setWhatsThis(_translate("Form", "Next image SAM state."))
        self.lineEdit_jump.setToolTip(_translate("Form", "Jump to the image. Input name or index."))
        self.lineEdit_jump.setPlaceholderText(_translate("Form", "Jump to the image."))
        self.label.setText(_translate("Form", "/"))
