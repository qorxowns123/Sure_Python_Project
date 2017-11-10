import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 385, 390)


        self.setWindowTitle('경비보고서 자동화 프로그램')

        #Loginfo group box
        self.U_LoginInfo = QGroupBox(self)
        self.U_LoginInfo.move(10, 10)
        self.U_LoginInfo.resize(360, 115)
        self.U_LoginInfo.setTitle('로그인 정보')

        #Loginfo PW text box
        self.G_User_PW = QTextEdit(self.U_LoginInfo)
        self.G_User_PW.move(100, 70)
        self.G_User_PW.resize(245, 30)
        self.G_User_PW.setObjectName("G_User_PW")
        
        #Loginfo ID text box
        self.G_User_ID = QTextEdit(self.U_LoginInfo)
        self.G_User_ID.move(100, 25)
        self.G_User_ID.resize(245, 30)
        self.G_User_ID.setObjectName("G_User_ID")
        
        #Loginfo ID label
        self.U_ID = QLabel(self.U_LoginInfo)
        self.U_ID.move(15, 25)
        self.U_ID.resize(70, 30)        
        self.U_ID.setObjectName("U_ID")
        self.U_ID.setText('아이디')
        
        #Loginfo PW label
        self.U_PW = QLabel(self.U_LoginInfo)
        self.U_PW.move(15, 70)
        self.U_PW.resize(70, 30)
        self.U_PW.setObjectName("U_PW")
        self.U_PW.setText('비밀번호')
        
        #DateInfo Group box
        self.U_SetDate = QGroupBox(self)
        self.U_SetDate.move(10, 140)
        self.U_SetDate.resize(360, 70)
        self.U_SetDate.setTitle('기간 설정하기')
        
        #DateInfo year
        self.G_User_SetYear = QComboBox(self.U_SetDate)
        self.G_User_SetYear.move(15, 25)
        self.G_User_SetYear.resize(115, 30)
        self.G_User_SetYear.setEditable(False)
        self.G_User_SetYear.setInsertPolicy(QComboBox.InsertAtBottom)
        self.G_User_SetYear.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.G_User_SetYear.setDuplicatesEnabled(False)
        self.G_User_SetYear.setObjectName("G_User_SetYear")

        for loopidx in range(0, 17):
            year_num = 2014 + loopidx
            year_text = str(year_num)
            self.G_User_SetYear.addItem(year_text)

        self.G_User_SetYear.setCurrentText("2017")

        #DateInfo month
        self.G_User_SetMonth = QComboBox(self.U_SetDate)
        self.G_User_SetMonth.move(190, 25)
        self.G_User_SetMonth.resize(115, 30)
        self.G_User_SetMonth.setInsertPolicy(QComboBox.InsertAtBottom)
        self.G_User_SetMonth.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.G_User_SetMonth.setDuplicatesEnabled(False)
        self.G_User_SetMonth.setObjectName("G_User_SetMonth")

        for loopidx in range(0, 12):
            month_num = loopidx + 1
            month_text = str(month_num)
            self.G_User_SetMonth.addItem(month_text)

        #Date year label
        self.U_SetYear = QLabel(self.U_SetDate)
        self.U_SetYear.move(145, 25)
        self.U_SetYear.resize(25, 30)
        self.U_SetYear.setText('년')
        self.U_SetYear.setObjectName("U_SetYear")
        
        #Date month label
        self.U_SetMonth = QLabel(self.U_SetDate)
        self.U_SetMonth.move(320, 25)
        self.U_SetMonth.resize(25, 30)
        self.U_SetMonth.setText('월')
        self.U_SetMonth.setObjectName("U_SetMonth")
        
        #Time groupbox
        self.U_SetTime = QGroupBox(self)
        self.U_SetTime.move(10, 225)
        self.U_SetTime.resize(360, 70)
        self.U_SetTime.setObjectName("U_SetTime")
        self.U_SetTime.setTitle('퇴근 시간 설정하기')   
        
        #Time hour label
        self.U_SetHour = QLabel(self.U_SetTime)
        self.U_SetHour.move(145, 25)
        self.U_SetHour.resize(25, 30)
        self.U_SetHour.setText('시')
        self.U_SetHour.setObjectName("U_SetHour")
        
        #Time minute label
        self.U_SetMinute = QLabel(self.U_SetTime)
        self.U_SetMinute.move(320, 25)
        self.U_SetMinute.resize(25, 30)
        self.U_SetMinute.setText('분')
        self.U_SetMinute.setObjectName("U_SetMinute")
        
        #Time set hour combobox
        self.G_User_SetHour = QComboBox(self.U_SetTime)
        self.G_User_SetHour.move(15, 25)
        self.G_User_SetHour.resize(115, 30)
        self.G_User_SetHour.setInsertPolicy(QComboBox.InsertAtBottom)
        self.G_User_SetHour.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.G_User_SetHour.setDuplicatesEnabled(False)
        self.G_User_SetHour.setObjectName("G_User_SetHour")

        for loopidx in range(0, 25):
            hour_num = loopidx + 1
            hour_text = str(hour_num)
            self.G_User_SetHour.addItem(hour_text)

        self.G_User_SetHour.setCurrentText("18")

        #Time set minute combobox
        self.G_User_SetMinute = QComboBox(self.U_SetTime)
        self.G_User_SetMinute.move(190, 25)
        self.G_User_SetMinute.resize(115, 30)
        self.G_User_SetMinute.setInsertPolicy(QComboBox.InsertAtBottom)
        self.G_User_SetMinute.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.G_User_SetMinute.setDuplicatesEnabled(False)
        self.G_User_SetMinute.setObjectName("G_User_SetMinute")

        for loopidx in range(0, 6):
            min_num = loopidx * 10
            min_text = str(min_num)
            self.G_User_SetMinute.addItem(min_text)

        self.G_User_SetMinute.setCurrentText("0")

        #button group box
        self.U_Get_GWHR_2 = QGroupBox(self)
        self.U_Get_GWHR_2.move(10, 305)
        self.U_Get_GWHR_2.resize(360, 62)
        self.U_Get_GWHR_2.setTitle("")
        self.U_Get_GWHR_2.setObjectName("U_Get_GWHR_2")

        #get active button
        self.G_Get_GWHR = QPushButton(self.U_Get_GWHR_2)
        self.G_Get_GWHR.move(20, 15)
        self.G_Get_GWHR.resize(140, 32)
        self.G_Get_GWHR.setText('경비보고서 생성')
        self.G_Get_GWHR.setObjectName("G_Get_GWHR")
        
        #make activ button
        self.G_Make_DocForm = QPushButton(self.U_Get_GWHR_2)
        self.G_Make_DocForm.move(200, 15)
        self.G_Make_DocForm.resize(140, 32)
        self.G_Make_DocForm.setText('경비보고서 열기')
        self.G_Make_DocForm.setObjectName("G_Make_DocForm")

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
