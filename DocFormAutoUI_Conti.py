# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocFormAutoUI_Conti.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    Ui_data = ['ID', 'PW', 2000, 1, 0, 0]
    UI_password = ['Init_PW']

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 664)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.U_LoginInfo = QtWidgets.QGroupBox(Dialog)
        self.U_LoginInfo.setGeometry(QtCore.QRect(10, 10, 381, 111))
        self.U_LoginInfo.setObjectName("U_LoginInfo")
        self.G_User_PW = QtWidgets.QTextEdit(self.U_LoginInfo)
        self.G_User_PW.setGeometry(QtCore.QRect(110, 70, 251, 31))
        self.G_User_PW.setObjectName("G_User_PW")
        self.G_User_ID = QtWidgets.QTextEdit(self.U_LoginInfo)
        self.G_User_ID.setGeometry(QtCore.QRect(110, 20, 251, 31))
        self.G_User_ID.setObjectName("G_User_ID")
        self.label = QtWidgets.QLabel(self.U_LoginInfo)
        self.label.setGeometry(QtCore.QRect(40, 30, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.U_LoginInfo)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 56, 12))
        self.label_2.setObjectName("label_2")
        self.U_SetDate = QtWidgets.QGroupBox(Dialog)
        self.U_SetDate.setGeometry(QtCore.QRect(10, 137, 381, 71))
        self.U_SetDate.setObjectName("U_SetDate")
        self.G_User_SetYear = QtWidgets.QComboBox(self.U_SetDate)
        self.G_User_SetYear.setGeometry(QtCore.QRect(10, 23, 111, 31))
        self.G_User_SetYear.setObjectName("G_User_SetYear")
        self.G_User_SetMonth = QtWidgets.QComboBox(self.U_SetDate)
        self.G_User_SetMonth.setGeometry(QtCore.QRect(200, 22, 111, 31))
        self.G_User_SetMonth.setObjectName("G_User_SetMonth")
        self.label_3 = QtWidgets.QLabel(self.U_SetDate)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 56, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.U_SetDate)
        self.label_4.setGeometry(QtCore.QRect(320, 30, 61, 16))
        self.label_4.setObjectName("label_4")
        self.U_SetTime = QtWidgets.QGroupBox(Dialog)
        self.U_SetTime.setGeometry(QtCore.QRect(10, 220, 381, 71))
        self.U_SetTime.setObjectName("U_SetTime")
        self.label_5 = QtWidgets.QLabel(self.U_SetTime)
        self.label_5.setGeometry(QtCore.QRect(130, 40, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.U_SetTime)
        self.label_6.setGeometry(QtCore.QRect(320, 40, 56, 12))
        self.label_6.setObjectName("label_6")
        self.G_User_SetHour = QtWidgets.QComboBox(self.U_SetTime)
        self.G_User_SetHour.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.G_User_SetHour.setObjectName("G_User_SetHour")
        self.G_User_SetMinute = QtWidgets.QComboBox(self.U_SetTime)
        self.G_User_SetMinute.setGeometry(QtCore.QRect(200, 30, 111, 31))
        self.G_User_SetMinute.setObjectName("G_User_SetMinute")
        self.U_Print_OTTable = QtWidgets.QTableView(Dialog)
        self.U_Print_OTTable.setGeometry(QtCore.QRect(10, 380, 381, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.U_Print_OTTable.sizePolicy().hasHeightForWidth())
        self.U_Print_OTTable.setSizePolicy(sizePolicy)
        self.U_Print_OTTable.setMinimumSize(QtCore.QSize(0, 0))
        self.U_Print_OTTable.setSizeIncrement(QtCore.QSize(0, 0))
        self.U_Print_OTTable.setBaseSize(QtCore.QSize(0, 0))
        self.U_Print_OTTable.setObjectName("U_Print_OTTable")
        self.U_Get_GWHR = QtWidgets.QFrame(Dialog)
        self.U_Get_GWHR.setGeometry(QtCore.QRect(10, 310, 381, 51))
        self.U_Get_GWHR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.U_Get_GWHR.setFrameShadow(QtWidgets.QFrame.Raised)
        self.U_Get_GWHR.setObjectName("U_Get_GWHR")
        self.U_Get_GWHR_Proc = QtWidgets.QProgressBar(self.U_Get_GWHR)
        self.U_Get_GWHR_Proc.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.U_Get_GWHR_Proc.setProperty("value", 24)
        self.U_Get_GWHR_Proc.setObjectName("U_Get_GWHR_Proc")
        self.G_Get_GWHR = QtWidgets.QPushButton(self.U_Get_GWHR)
        self.G_Get_GWHR.setGeometry(QtCore.QRect(270, 10, 93, 31))
        self.G_Get_GWHR.setObjectName("G_Get_GWHR")
        self.U_Make_DocForm = QtWidgets.QFrame(Dialog)
        self.U_Make_DocForm.setGeometry(QtCore.QRect(10, 601, 381, 51))
        self.U_Make_DocForm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.U_Make_DocForm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.U_Make_DocForm.setObjectName("U_Make_DocForm")
        self.G_Make_DocForm_Proc = QtWidgets.QProgressBar(self.U_Make_DocForm)
        self.G_Make_DocForm_Proc.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.G_Make_DocForm_Proc.setProperty("value", 99)
        self.G_Make_DocForm_Proc.setObjectName("G_Make_DocForm_Proc")
        self.G_Make_DocForm = QtWidgets.QPushButton(self.U_Make_DocForm)
        self.G_Make_DocForm.setGeometry(QtCore.QRect(270, 10, 93, 31))
        self.G_Make_DocForm.setObjectName("G_Make_DocForm")

        self.G_Get_GWHR.clicked.connect(self.Get_GWHR_bnt_clicked)
        self.G_Make_DocForm.clicked.connect(self.Make_DocForm_bnt_clicked)
        self.G_User_PW.textChanged.connect(self.User_PW_key_pushed)

        self.Set_Items() 

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.U_LoginInfo.setTitle(_translate("Dialog", "로그인 정보"))
        self.label.setText(_translate("Dialog", "아이디"))
        self.label_2.setText(_translate("Dialog", "패스워드"))
        self.U_SetDate.setTitle(_translate("Dialog", "기간 설정하기"))
        self.label_3.setText(_translate("Dialog", "년"))
        self.label_4.setText(_translate("Dialog", "월"))
        self.U_SetTime.setTitle(_translate("Dialog", "퇴근 시간 설정하기"))
        self.label_5.setText(_translate("Dialog", "시"))
        self.label_6.setText(_translate("Dialog", "분"))
        self.G_Get_GWHR.setText(_translate("Dialog", "가져오기"))
        self.G_Make_DocForm.setText(_translate("Dialog", "내보내기"))

    def Set_Items(self):
        
        Items_year = ['2014', '2015', '2016', '2017']
        self.G_User_SetYear.addItems(Items_year)

        Items_month = ['1','2','3','4','5','6','7','8','9','10','11','12']
        self.G_User_SetMonth.addItems(Items_month)

        Items_hour = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
        self.G_User_SetHour.addItems(Items_hour)

        Items_minute = ['0', '10','20','30','40','50']
        self.G_User_SetMinute.addItems(Items_minute)



    def Get_GWHR_bnt_clicked(self):
        print('가져오기 눌림')
        ID_txt = self.G_User_ID.toPlainText()
        PW_txt = self.G_User_PW.toPlainText()
        Year_Num = self.G_User_SetYear.currentText()
        Month_Num = self.G_User_SetMonth.currentText()
        Hour_Num = self.G_User_SetHour.currentText()
        Minute_Num = self.G_User_SetMinute.currentText()


        if ID_txt != None:     
            self.Ui_data[0] = ID_txt

        if PW_txt != None:
            self.Ui_data[1] = PW_txt

        if Year_Num != None:
            self.Ui_data[2] = Year_Num

        if Month_Num != None:
            self.Ui_data[3] = Month_Num

        if Hour_Num != None:
            self.Ui_data[4] = Hour_Num

        if Minute_Num != None:
            self.Ui_data[5] = Minute_Num

        print(self.Ui_data)

    def Make_DocForm_bnt_clicked(self):
        print('내보내기 눌림')
        PW_txt = self.G_User_PW.toPlainText()
        print(PW_txt)

    def User_PW_key_pushed(self):
        print('키 입력')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

