# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocFormAutoUI_0.0.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ui_Main_Dialog(QMainWindow):

    def setupUi(self, Main_Dialog):
        Main_Dialog.setObjectName("Main_Dialog")
        Main_Dialog.resize(385, 390)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main_Dialog.sizePolicy().hasHeightForWidth())
        Main_Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("HY그래픽M")
        font.setBold(False)
        font.setWeight(50)
        Main_Dialog.setFont(font)
        self.U_LoginInfo = QtWidgets.QGroupBox(Main_Dialog)
        self.U_LoginInfo.setGeometry(QtCore.QRect(10, 10, 360, 115))
        self.U_LoginInfo.setObjectName("U_LoginInfo")
        self.G_User_PW = QtWidgets.QTextEdit(self.U_LoginInfo)
        self.G_User_PW.setGeometry(QtCore.QRect(100, 70, 245, 30))
        self.G_User_PW.setObjectName("G_User_PW")
        self.G_User_ID = QtWidgets.QTextEdit(self.U_LoginInfo)
        self.G_User_ID.setGeometry(QtCore.QRect(100, 25, 245, 30))
        self.G_User_ID.setObjectName("G_User_ID")
        self.U_ID = QtWidgets.QLabel(self.U_LoginInfo)
        self.U_ID.setGeometry(QtCore.QRect(15, 25, 70, 30))
        self.U_ID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.U_ID.setObjectName("U_ID")
        self.U_PW = QtWidgets.QLabel(self.U_LoginInfo)
        self.U_PW.setGeometry(QtCore.QRect(15, 70, 70, 30))
        self.U_PW.setObjectName("U_PW")
        self.U_SetDate = QtWidgets.QGroupBox(Main_Dialog)
        self.U_SetDate.setGeometry(QtCore.QRect(10, 140, 360, 70))
        self.U_SetDate.setObjectName("U_SetDate")
        self.G_User_SetYear = QtWidgets.QComboBox(self.U_SetDate)
        self.G_User_SetYear.setGeometry(QtCore.QRect(15, 25, 115, 30))
        self.G_User_SetYear.setEditable(False)
        self.G_User_SetYear.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.G_User_SetYear.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.G_User_SetYear.setDuplicatesEnabled(False)
        self.G_User_SetYear.setObjectName("G_User_SetYear")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetYear.addItem("")
        self.G_User_SetMonth = QtWidgets.QComboBox(self.U_SetDate)
        self.G_User_SetMonth.setGeometry(QtCore.QRect(190, 25, 115, 30))
        self.G_User_SetMonth.setObjectName("G_User_SetMonth")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.G_User_SetMonth.addItem("")
        self.U_SetYear = QtWidgets.QLabel(self.U_SetDate)
        self.U_SetYear.setGeometry(QtCore.QRect(145, 25, 25, 30))
        self.U_SetYear.setObjectName("U_SetYear")
        self.U_SetMonth = QtWidgets.QLabel(self.U_SetDate)
        self.U_SetMonth.setGeometry(QtCore.QRect(320, 25, 25, 30))
        self.U_SetMonth.setObjectName("U_SetMonth")
        self.U_SetTime = QtWidgets.QGroupBox(Main_Dialog)
        self.U_SetTime.setGeometry(QtCore.QRect(10, 225, 360, 70))
        self.U_SetTime.setObjectName("U_SetTime")
        self.U_SetHour = QtWidgets.QLabel(self.U_SetTime)
        self.U_SetHour.setGeometry(QtCore.QRect(145, 25, 25, 30))
        self.U_SetHour.setObjectName("U_SetHour")
        self.U_SetMinute = QtWidgets.QLabel(self.U_SetTime)
        self.U_SetMinute.setGeometry(QtCore.QRect(320, 25, 25, 30))
        self.U_SetMinute.setObjectName("U_SetMinute")
        self.G_User_SetHour = QtWidgets.QComboBox(self.U_SetTime)
        self.G_User_SetHour.setGeometry(QtCore.QRect(15, 25, 115, 30))
        self.G_User_SetHour.setEditable(True)
        self.G_User_SetHour.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.G_User_SetHour.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.G_User_SetHour.setDuplicatesEnabled(False)
        self.G_User_SetHour.setObjectName("G_User_SetHour")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetHour.addItem("")
        self.G_User_SetMinute = QtWidgets.QComboBox(self.U_SetTime)
        self.G_User_SetMinute.setGeometry(QtCore.QRect(190, 25, 115, 30))
        self.G_User_SetMinute.setEditable(True)
        self.G_User_SetMinute.setObjectName("G_User_SetMinute")
        self.G_User_SetMinute.addItem("")
        self.G_User_SetMinute.addItem("")
        self.G_User_SetMinute.addItem("")
        self.G_User_SetMinute.addItem("")
        self.G_User_SetMinute.addItem("")
        self.G_User_SetMinute.addItem("")
        self.U_Get_GWHR_2 = QtWidgets.QGroupBox(Main_Dialog)
        self.U_Get_GWHR_2.setGeometry(QtCore.QRect(10, 305, 360, 62))
        self.U_Get_GWHR_2.setTitle("")
        self.U_Get_GWHR_2.setObjectName("U_Get_GWHR_2")
        self.G_Get_GWHR = QtWidgets.QPushButton(self.U_Get_GWHR_2)
        self.G_Get_GWHR.setGeometry(QtCore.QRect(20, 15, 140, 32))
        self.G_Get_GWHR.setObjectName("G_Get_GWHR")
        self.G_Make_DocForm = QtWidgets.QPushButton(self.U_Get_GWHR_2)
        self.G_Make_DocForm.setGeometry(QtCore.QRect(200, 15, 140, 32))
        self.G_Make_DocForm.setObjectName("G_Make_DocForm")

        self.retranslateUi(Main_Dialog)
        self.G_User_SetHour.setCurrentIndex(17)
        QtCore.QMetaObject.connectSlotsByName(Main_Dialog)
        Main_Dialog.setTabOrder(self.G_Get_GWHR, self.G_User_PW)
        Main_Dialog.setTabOrder(self.G_User_PW, self.G_User_ID)
        Main_Dialog.setTabOrder(self.G_User_ID, self.G_User_SetYear)
        Main_Dialog.setTabOrder(self.G_User_SetYear, self.G_User_SetMonth)
        Main_Dialog.setTabOrder(self.G_User_SetMonth, self.G_User_SetHour)
        Main_Dialog.setTabOrder(self.G_User_SetHour, self.G_User_SetMinute)
        Main_Dialog.setTabOrder(self.G_User_SetMinute, self.G_Make_DocForm)

    def retranslateUi(self, Main_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Main_Dialog.setWindowTitle(_translate("Main_Dialog", "경비보고서 자동화 프로그램"))
        self.U_LoginInfo.setTitle(_translate("Main_Dialog", "로그인 정보"))
        self.G_User_PW.setHtml(_translate("Main_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY그래픽M\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Gulim\';\"><br /></p></body></html>"))
        self.U_ID.setText(_translate("Main_Dialog", "아이디"))
        self.U_PW.setText(_translate("Main_Dialog", "비밀번호"))
        self.U_SetDate.setTitle(_translate("Main_Dialog", "기간 설정하기"))

        for loopidx in range(0, 17):
            year_num = 2014 + loopidx
            year_text = str(year_num)
            self.G_User_SetYear.setItemText(loopidx, _translate("Main_Dialog", year_text))


        self.G_User_SetYear.setCurrentText(_translate("Main_Dialog", "2017"))
        for loopidx in range(0, 12):
            month_num = loopidx + 1
            month_text = str(month_num)
            self.G_User_SetMonth.setItemText(loopidx, _translate("Main_Dialog", month_text))


        self.U_SetYear.setText(_translate("Main_Dialog", "년"))
        self.U_SetMonth.setText(_translate("Main_Dialog", "월"))
        self.U_SetTime.setTitle(_translate("Main_Dialog", "퇴근 시간 설정하기"))
        self.U_SetHour.setText(_translate("Main_Dialog", "시"))
        self.U_SetMinute.setText(_translate("Main_Dialog", "분"))
        self.G_User_SetHour.setCurrentText(_translate("Main_Dialog", "18"))

        for loopidx in range(0, 25):
            hour_num = loopidx + 1
            hour_text = str(hour_num)
            self.G_User_SetHour.setItemText(loopidx, _translate("Main_Dialog", hour_text))

        self.G_User_SetMinute.setCurrentText(_translate("Main_Dialog", "0"))
        for loopidx in range(0, 6):
            min_num = loopidx * 10
            min_text = str(min_num)
            self.G_User_SetMinute.setItemText(loopidx, _translate("Main_Dialog", min_text))

        self.G_Get_GWHR.setText(_translate("Main_Dialog", "경비보고서 생성"))
        self.G_Make_DocForm.setText(_translate("Main_Dialog", "경비보고서 열기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Dialog = QtWidgets.QDialog()
    ui = Ui_Main_Dialog()
    ui.setupUi(Main_Dialog)
    Main_Dialog.show()
    sys.exit(app.exec_())

