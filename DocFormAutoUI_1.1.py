import sys
from PyQt5.QtWidgets import *
from PyQt5 import Qt, QtCore, QtGui
import Search_Hanbiro
import Create_ExcelFile
import os
import subprocess
from datetime import date

class MyWindow(QMainWindow):

    # 년, 월, 시간, 분
    set_day_info = ['1111', '11', '11', '11']

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 385, 390)
        self.setWindowTitle('야근없는그날까지')
        
        # 도움말 열기
        bar = self.menuBar()
        helpOption = bar.addMenu('Help')
        helpOpen = QAction("도움말열기", self)
        helpOption.addAction(helpOpen)
        helpOption.triggered.connect(self.helpTrigger)

        # GUI 아이콘 변경
        sciptDir = os.path.dirname(os.path.realpath(__file__))
        iconPath = sciptDir + os.path.sep + 'Report\\NoYagn.ico'
        self.setWindowIcon(QtGui.QIcon(iconPath))

        #Loginfo group box
        self.U_LoginInfo = QGroupBox(self)
        self.U_LoginInfo.move(10, 30)
        self.U_LoginInfo.resize(360, 115)
        self.U_LoginInfo.setTitle('로그인 정보')

        #Loginfo ID text box
        self.G_User_ID = QLineEdit(self.U_LoginInfo)
        self.G_User_ID.move(100, 25)
        self.G_User_ID.resize(245, 30)
        self.G_User_ID.setFocus()

        #Loginfo PW text box
        self.G_User_PW = QLineEdit(self.U_LoginInfo)
        self.G_User_PW.move(100, 70)
        self.G_User_PW.resize(245, 30)
        self.G_User_PW.setEchoMode(QLineEdit.Password)

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
        self.U_SetDate.move(10, 150)
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

        now = date.today()
        self.G_User_SetYear.setCurrentText(str(now.year))

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

        self.G_User_SetMonth.setCurrentText(str(now.month))

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
        self.G_Make_DocForm.setAutoDefault(True)
        
        #make activ button
        self.G_Open_DocForm = QPushButton(self.U_Get_GWHR_2)
        self.G_Open_DocForm.move(200, 15)
        self.G_Open_DocForm.resize(140, 32)
        self.G_Open_DocForm.setText('보고서 디렉토리 열기')
        self.G_Open_DocForm.clicked.connect(self.clicked_open_btn)
        self.G_Open_DocForm.setAutoDefault(True)


        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Ready')


    def clicked_make_btn(self):
        # 년
        self.set_day_info[0] = self.G_User_SetYear.currentText()
        # 월
        self.set_day_info[1] = self.G_User_SetMonth.currentText()
        # 시간
        self.set_day_info[2] = self.G_User_SetHour.currentText()
        # 분
        self.set_day_info[3] = self.G_User_SetMinute.currentText()
        print('\n')
        printText = '=================' + self.set_day_info[0] + '년' + self.set_day_info[1] + '월' + '================='
        print(printText)

        checkDay = getToday(self.set_day_info)
        if checkDay == False:
            showWarningDialog('현재 날짜보다 미래 날짜는 설정할 수 없습니다')
            return
        else:
            pass

        if not self.G_User_ID.text():
            showWarningDialog('아이디를 입력해주세요')
            return
        elif not self.G_User_PW.text():
            showWarningDialog('패스워드를 입력해주세요')
            return
        else:
            if os.path.isfile('phantomjs.exe'):
                class_hanbiro = Search_Hanbiro.SearchHanbiro()
                class_xlsx = Create_ExcelFile.CreateExcelFile()
            else:
                showCriticalDialog('phantomjs.exe가 존재하지 않습니다')
                return

            self.statusBar.showMessage('한비로에 로그인 중입니다...')
            [check_login, driver] = class_hanbiro.search_hanbiro_main(self.G_User_ID.text(), self.G_User_PW.text())


            if check_login != False:
                # 캘린더 로그인
                TimetoMoneyList = class_hanbiro.enter_calendar(driver, self.set_day_info)
                if not TimetoMoneyList:
                    self.statusBar.showMessage('프로그램 종료 - 야근한 날이 없습니다')
                    showInfoDialog('야근한 날이 없습니다')
                else:
                    filecheck = find_ExcelFile(self.set_day_info)
                    if filecheck == True:
                        answer = showQuestionDialog(self, '같은파일이 존재합니다. 계속하시겠습니까?')
                        if answer == QMessageBox.Yes:
                            self.statusBar.showMessage('엑셀 파일을 생성 중입니다...')
                            try:
                                self.filename = class_xlsx.create_xlsx(TimetoMoneyList, self.set_day_info)
                                self.statusBar.showMessage('프로그램 종료 - 경비보고서가 성공적으로 생성 되었습니다')
                                answer = showQuestionDialog(self, '경비보고서가 생성되었습니다. 여시겠습니까?')
                            except:
                                showCriticalDialog('해당 월의 경비보고서가 이미 실행중입니다.\n경비보고서를 닫고 다시 실행해주세요')
                                self.statusBar.showMessage('Ready')
                                return
                            if answer == QMessageBox.Yes:
                                os.popen(self.filename)
                            else:
                                pass
                        else:
                            showInfoDialog('파일 생성 취소')
                    else:
                        self.statusBar.showMessage('엑셀 파일을 생성 중입니다...')
                        self.filename = class_xlsx.create_xlsx(TimetoMoneyList, self.set_day_info)
                        self.statusBar.showMessage('프로그램 종료 - 경비보고서가 성공적으로 생성 되었습니다')
                        showInfoDialog('경비보고서 생성 완료')
                        answer = showQuestionDialog(self, '경비보고서가 생성되었습니다. 여시겠습니까?')
                        if answer == QMessageBox.Yes:
                            os.popen(self.filename)
                        else:
                            pass
                    
            else:
                self.statusBar.showMessage('로그인 실패 - 아이디와 패스워드를 확인바랍니다')
                showInfoDialog('로그인 실패')

    def clicked_open_btn(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File", None, "Excel Files (*.xlsx)")
        try:
            res = subprocess.Popen(fileName[0], shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
            [output, error] = res.communicate()
            if error:
                showCriticalDialog('해당 월의 경비보고서가 이미 실행중입니다.\n경비보고서를 닫고 다시 실행해주세요')
                self.statusBar.showMessage('Ready')
            else:
                pass
        except:
            pass

    def helpTrigger(self):
        filename = '.\\Report\\야근없는 그날까지 사용자 매뉴얼.htm'
        os.popen(filename)


def find_ExcelFile(set_day_info):
    filename = set_day_info[0] + '_' + set_day_info[1] + '_경비보고서.xlsx'
    file_exist = False
    current_dir = os.getcwd()
    file_list = os.listdir(current_dir)
    file_list.sort()
    for loopidx in range(file_list.__len__()):
        curtext = file_list[loopidx]
        if filename == curtext:
            file_exist = True
            break
        else:
            continue
    return file_exist

def showWarningDialog(strMsg):
   msgWarning = QMessageBox()
   msgWarning.setIcon(QMessageBox.Warning)
   msgWarning.setText(strMsg)
   msgWarning.setWindowTitle("Warning")
   msgWarning.setStandardButtons(QMessageBox.Ok)
   msgWarning.exec_()

def showInfoDialog(strMsg):
    msgInfo = QMessageBox()
    msgInfo.setIcon(QMessageBox.Information)
    msgInfo.setText(strMsg)
    msgInfo.setWindowTitle("Info")
    msgInfo.setStandardButtons(QMessageBox.Ok)
    msgInfo.exec_()

def showCriticalDialog(strMsg):
   msgCrtc = QMessageBox()
   msgCrtc.setIcon(QMessageBox.Critical)
   msgCrtc.setText(strMsg)
   msgCrtc.setWindowTitle("Error")
   msgCrtc.setStandardButtons(QMessageBox.Ok)
   msgCrtc.exec_()

def showQuestionDialog(self, strMsg):
    return QMessageBox.question(self, 'Question', strMsg, QMessageBox.Yes | QMessageBox.No)


def getToday(set_day_info):
    now = date.today()
    checkDay = True
    if int(set_day_info[0]) > int(now.year):
        # 미래이므로 종료
        checkDay = False
    elif (int(set_day_info[0]) == int(now.year)) and (int(set_day_info[1]) > int(now.month)):
            # 역시 미래이므로 종료
            checkDay = False
    else:
        pass

    return (checkDay)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
