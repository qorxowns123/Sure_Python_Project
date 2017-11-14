import sys
from PyQt5.QtWidgets import *
import Search_Hanbiro
import Create_ExcelFile
import os

class MyWindow(QMainWindow):

    # 년, 월, 시간, 분
    set_day_info = []

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 385, 390)

        self.setWindowTitle('경비보고서 자동생성')

        #Loginfo group box
        self.U_LoginInfo = QGroupBox(self)
        self.U_LoginInfo.move(10, 10)
        self.U_LoginInfo.resize(360, 115)
        self.U_LoginInfo.setTitle('로그인 정보')

        #Loginfo ID text box
        #self.G_User_ID = QTextEdit(self.U_LoginInfo)
        self.G_User_ID = QLineEdit(self.U_LoginInfo)
        self.G_User_ID.move(100, 25)
        self.G_User_ID.resize(245, 30)
        self.G_User_ID.textChanged.connect(self.Id_Key_press)
        self.G_User_ID.setFocus()

        #Loginfo PW text box
        #self.G_User_PW = QTextEdit(self.U_LoginInfo)
        self.G_User_PW = QLineEdit(self.U_LoginInfo)
        self.G_User_PW.move(100, 70)
        self.G_User_PW.resize(245, 30)
        self.G_User_PW.textChanged.connect(self.Pw_Key_press)
        
        #Loginfo ID label
        self.U_ID = QLabel(self.U_LoginInfo)
        self.U_ID.move(15, 25)
        self.U_ID.resize(70, 30)
        self.U_ID.setText('아이디')
        
        #Loginfo PW label
        self.U_PW = QLabel(self.U_LoginInfo)
        self.U_PW.move(15, 70)
        self.U_PW.resize(70, 30)
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
        
        for loopidx in range(0, 12):
            month_num = loopidx + 1
            if loopidx < 9:
                month_text = '0' + str(month_num)
            else:
                month_text = str(month_num)
            self.G_User_SetMonth.addItem(month_text)

        #Date year label
        self.U_SetYear = QLabel(self.U_SetDate)
        self.U_SetYear.move(145, 25)
        self.U_SetYear.resize(25, 30)
        self.U_SetYear.setText('년')
        
        #Date month label
        self.U_SetMonth = QLabel(self.U_SetDate)
        self.U_SetMonth.move(320, 25)
        self.U_SetMonth.resize(25, 30)
        self.U_SetMonth.setText('월')
        
        #Time groupbox
        self.U_SetTime = QGroupBox(self)
        self.U_SetTime.move(10, 225)
        self.U_SetTime.resize(360, 70)
        self.U_SetTime.setTitle('퇴근 시간 설정하기')   
        
        #Time hour label
        self.U_SetHour = QLabel(self.U_SetTime)
        self.U_SetHour.move(145, 25)
        self.U_SetHour.resize(25, 30)
        self.U_SetHour.setText('시')
        
        #Time minute label
        self.U_SetMinute = QLabel(self.U_SetTime)
        self.U_SetMinute.move(320, 25)
        self.U_SetMinute.resize(25, 30)
        self.U_SetMinute.setText('분')
        
        #Time set hour combobox
        self.G_User_SetHour = QComboBox(self.U_SetTime)
        self.G_User_SetHour.move(15, 25)
        self.G_User_SetHour.resize(115, 30)
        self.G_User_SetHour.setInsertPolicy(QComboBox.InsertAtBottom)
        self.G_User_SetHour.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.G_User_SetHour.setDuplicatesEnabled(False)

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
        #get active button
        self.G_Make_DocForm = QPushButton(self.U_Get_GWHR_2)
        self.G_Make_DocForm.move(20, 15)
        self.G_Make_DocForm.resize(140, 32)
        self.G_Make_DocForm.setText('경비보고서 생성')
        self.G_Make_DocForm.clicked.connect(self.clicked_make_btn)
        
        #make activ button
        self.G_Open_DocForm = QPushButton(self.U_Get_GWHR_2)
        self.G_Open_DocForm.move(200, 15)
        self.G_Open_DocForm.resize(140, 32)
        self.G_Open_DocForm.setText('경비보고서 열기')
        self.G_Open_DocForm.clicked.connect(self.clicked_open_btn)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Ready')

    def Window_Key_press(self):
        print('Any key pressed')
        pass


    def Id_Key_press(self):
        pass
        '''
        print('ID text changed')
        print(self.G_User_ID.toPlainText())
        if '\t' in self.G_User_ID.toPlainText():
            print('탭 발견!!')
        '''

    def Pw_Key_press(self):
        #print('PW text changed')
        pass

    def clicked_make_btn(self):
        #print('경비보고서 생성 버튼 클릭')
        self.statusBar.showMessage('한비로에 로그인 시도 중...')
        '''
        self.G_User_ID.toPlainText() # 아이디
        self.G_User_PW.toPlainText() # 비밀번호
        
        self.G_User_SetYear.currentText() # 년
        self.G_User_SetMonth.currentText() # 월
        self.G_User_SetHour.currentText() # 시간
        self.G_User_SetMinute.currentText() # 분
        '''
        # 년
        self.set_day_info.append(self.G_User_SetYear.currentText())
        # 월
        self.set_day_info.append(self.G_User_SetMonth.currentText())
        # 시간
        self.set_day_info.append(self.G_User_SetHour.currentText())
        # 분
        self.set_day_info.append(self.G_User_SetMinute.currentText())
        #print(self.Info)

        if not self.G_User_ID.toPlainText():
            self.statusBar.showMessage('아이디를 입력해주세요')
            return
        elif not self.G_User_PW.toPlainText():
            self.statusBar.showMessage('패스워드를 입력해주세요')
            return
        else:
            class_hanbiro = Search_Hanbiro.SearchHanbiro()
            class_xlsx = Create_ExcelFile.CreateExcelFile()

            [check_login, driver, errorflag] = class_hanbiro.search_hanbiro_main(self.G_User_ID.toPlainText(), self.G_User_PW.toPlainText())
            if errorflag == 2:
                self.statusBar.showMessage('phantomjs.exe 파일이 실행파일과 같은 폴더에 위치해야만 합니다')
                return
            else:
                pass

            if check_login != False:
                # 캘린더 로그인
                [store_over_work_day, store_over_work_time, store_over_work_money] = class_hanbiro.enter_calendar(driver, self.set_day_info)
                if not store_over_work_day:
                    self.statusBar.showMessage('프로그램 종료 - 야근한 날이 없습니다')
                else:
                    self.statusBar.showMessage('로그인 성공 - 엑셀 파일을 생성 중입니다...')
                    class_xlsx.create_xlsx(store_over_work_day, store_over_work_time, store_over_work_money)
                    self.statusBar.showMessage('프로그램 종료 - 경비보고서가 성공적으로 생성 되었습니다')
                    
            else:
                self.statusBar.showMessage('로그인 실패 - 아이디와 비밀번호를 다시 확인 바랍니다')

    def clicked_open_btn(self):
        #print('경비보고서 열기 버튼 클릭')
        self.statusBar.showMessage('경비보고서.xlsx 파일을 실행합니다')
        filepath = ".\\경비보고서.xlsx"
        os.popen(filepath)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
