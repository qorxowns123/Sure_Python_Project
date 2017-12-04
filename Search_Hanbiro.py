from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os


class SearchHanbiro:
    def search_hanbiro_main(self, sure_id, sure_pw):
        # 한비로 로그인 주소
        main_address = 'http://suresofttech.hanbiro.net/groupware/login.php'
        # 로그인 화면
        login_adress = ['http://suresofttech.hanbiro.net/groupware/?category=index&section=main', 'http://suresofttech.hanbiro.net/ngw/app/#/']

        # 정상로그인 확인
        check_login = False
        # 현재 실행 경로 구하기 및 이름 합치기
        excutepath = os.getcwd()
        excutename = 'phantomjs.exe'
        excutepath = os.path.join(excutepath, excutename)
        driver = webdriver.PhantomJS(excutepath)


        # 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
        driver.implicitly_wait(3)
        # 한비로 접속
        driver.get(main_address)
        # 아이디 입력
        driver.find_element_by_name('hmail_id').send_keys(sure_id)
        # 비밀번호 입력
        driver.find_element_by_name('hmail_pass').send_keys(sure_pw)
        # 자동 로그인 시도(비밀번호    가 맞지 않을때 에러 구현 필요)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td').click()
        # 바로 접속하면 캘린더로 접속이 안되므로 3초의 여유를 둔다.
        time.sleep(3)

        if ((driver.current_url == login_adress[0]) or (driver.current_url == login_adress[1])):
            check_login = True
        else:
            time.sleep(3)
            if ((driver.current_url == login_adress[0]) or (driver.current_url == login_adress[1])):
                check_login = True
            else:
                pass

        return (check_login, driver)

    def enter_calendar(self, driver, set_day_info):
        over_work_time = ['', '']
        # 년
        input_year = set_day_info[0]
        # 월
        input_day = set_day_info[1]
        # 시간
        over_work_time[0] = int(set_day_info[2])
        # 분
        over_work_time[1] = int(set_day_info[3])

        # 한비로 캘린더 주소
        calendar_address = 'http://suresofttech.hanbiro.net/groupware/?category=time&section=userCalendar'

        driver.get(calendar_address)
        
        # 웹페이지 소스 추출
        get_html = driver.page_source
        # HTML 소스 읽어오기
        get_parser = BeautifulSoup(get_html, 'html.parser')
        # 태그를 통한 현재 날짜 가져오기
        get_tag_info = get_parser.find_all('b')
        get_current_day = get_tag_info[0].text
        setCurYear = get_current_day[0:4]
        setCurMonth = get_current_day[5:]
        # 목록으로 보기
        driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/button[1]').click()

        # 년도 입력
        if input_year != setCurYear:
            driver.find_element_by_name('syear').send_keys(input_year)
        else:
            pass

        # 월 입력
        if input_day != setCurMonth:
            driver.find_element_by_name('smonth').send_keys(input_day)
        else:
            pass

        # 검색
        driver.find_element_by_xpath('//*[@id="monthTerm"]/form/table/tbody/tr/td[2]/input').click()

        # 웹페이지 소스 추출
        get_html = driver.page_source
        # HTML 소스 읽어오기
        get_parser = BeautifulSoup(get_html, 'html.parser')

        # 태그를 통한 일자와 근태 내용 가져오기
        get_tag_info = get_parser.find_all('tr', height = '26')
        get_day_info = []
        for loopidx in range(0, get_tag_info.__len__()):
            get_day_info.append(get_tag_info[loopidx].contents)

        # 브라우져 종료
        driver.close()

        # 년/월/일자 저장
        store_day_info_temp = []
        # 출근여부저장
        store_check_info_temp = []
        for loopjdx in range(0, get_day_info.__len__()):
            store_day_info_temp.append(get_day_info[loopjdx][1].text)
            store_check_info_temp.append(get_day_info[loopjdx][3].text)
            store_check_info_temp[loopjdx] = store_check_info_temp[loopjdx].replace('\t', '')
            store_check_info_temp[loopjdx] = store_check_info_temp[loopjdx].replace('\n', '')
            store_check_info_temp[loopjdx] = store_check_info_temp[loopjdx].replace(' ', '')

        # 주차 정리
        store_day_info = []
        temp_store_day_info = []
        store_check_info = []
        temp_store_check_info = []


        week_mode = '주차'
        temp_store_day_info.append(week_mode)
        temp_store_check_info.append(week_mode)

        # 주차로 나누기(일요일을 만나면 한 주로 설정)
        for looppdx in range(0, store_day_info_temp.__len__()):
            if store_day_info_temp[looppdx][12] == '일':
                #cnt = cnt + 1

                store_day_info.append(temp_store_day_info)
                temp_store_day_info = []
                temp_store_day_info.append(week_mode)
                temp_store_day_info.append(store_day_info_temp[looppdx])

                store_check_info.append(temp_store_check_info)
                temp_store_check_info = []
                temp_store_check_info.append(week_mode)
                temp_store_check_info.append(store_check_info_temp[looppdx])
            else:
                temp_store_day_info.append(store_day_info_temp[looppdx])
                temp_store_check_info.append(store_check_info_temp[looppdx])

        store_day_info.append(temp_store_day_info)
        store_check_info.append(temp_store_check_info)

        [get_day_list, get_inTime_list, get_outTime_list] = checkLeaveWork(store_day_info, store_check_info)
        '''
        print(get_day_list)
        print(get_inTime_list)
        print(get_outTime_list)
        '''
        # 야근한 날 체크
        OverWorkTimeList = checkOverWork(get_day_list, get_inTime_list, get_outTime_list, over_work_time)
        TimetoMoneyList = overTimetoMoney(OverWorkTimeList)
        return (TimetoMoneyList)
# end enter_calendar Func


def overTimetoMoney(overWorkTimeList):
    setTimetoMoney = []
    for loopidx in range(0, overWorkTimeList.__len__()):
        tempList = []
        if overWorkTimeList[loopidx].__len__() == 1:
            continue
        else:
            for loopjdx in range(1, overWorkTimeList[loopidx].__len__()):
                getTime = overWorkTimeList[loopidx][loopjdx]
                if getTime >= 2 and getTime < 4:
                    tempList.append(10000)
                elif getTime >= 4 and getTime < 8:
                    tempList.append(20000)
                elif getTime >= 8:
                    tempList.append(40000)
                else:
                    pass
            setTimetoMoney.append(tempList)
    return (setTimetoMoney)

def checkOverWork(get_day_list, get_inTime_list, get_outTime_list, over_work_time):
    setOverTimeList = []
    for loopidx in range(0, get_day_list.__len__()):
        tempList = []
        tempList.append('주차')
        if get_day_list[loopidx].__len__() == 1:
            # ['주차']만 있을경우는 넘어가기
            setOverTimeList.append(tempList)
            continue
        else:
            for loopjdx in range(1, get_day_list[loopidx].__len__()):
                # 휴무와 평일을 구분하여 야근시간 계산하기
                day_text = get_day_list[loopidx][loopjdx]
                find_holiday = day_text.find('휴무')
                find_overNight = day_text.find('자정후퇴근')
                # 평일인 경우
                if find_holiday == -1:
                    result = setWeekday(get_inTime_list, over_work_time, get_outTime_list, loopidx, loopjdx, find_overNight,get_day_list)
                    if result == -1:
                        # 야근한 날이 없을 경우
                        pass
                    else:
                        # 야근한 날이 있을 경우
                        tempList.append(result)
                # 주말인 경우
                else:
                    result = setHoliday(get_inTime_list, get_outTime_list, loopidx, loopjdx, find_overNight, get_day_list)
                    if result == -1:
                        # 야근한 날이 없을 경우
                        pass
                    else:
                        # 야근한 날이 있을 경우
                        tempList.append(result)

            setOverTimeList.append(tempList)

    return (setOverTimeList)



def setHoliday(get_inTime_list, get_outTime_list, loopidx, loopjdx, overNight, get_day_list):
    # 출근 시간
    setStartWork = get_inTime_list[loopidx][loopjdx]
    # 야근(퇴근) 시간
    setEndWork = get_outTime_list[loopidx][loopjdx]
    
    # 출근시간을 시/분으로 나누기
    setStartWorkHour = int(setStartWork[0:2])
    setStartWorkMin = int(setStartWork[3:])

    # 야근(퇴근)시간을 시/분으로 나누기
    setEndWorkHour = int(setEndWork[0:2])
    setEndWorkMin = int(setEndWork[3:])

    textTemp = get_day_list[loopidx][loopjdx]

    # 자정후 퇴근이라면...
    if overNight != -1:
        # 자정후 퇴근한것이 진짜 맞다면...
        if setStartWorkHour > setEndWorkHour:
            setEndWorkHour = 24
            setEndWorkMin = 0
        else:
            pass
    else:
        pass

    hourRange = setEndWorkHour - setStartWorkHour
    minRange = setEndWorkMin - setStartWorkMin


    # 시간이 2시간 이상이고, 분이 음수가 아니라면...
    if (hourRange > 2) and (minRange <= -1):
        # 해당 야근시간을 리스트에 저장
        hourRange = hourRange - 1
        textTemp = textTemp + ' ---- 야근'
        print(textTemp)
    elif ((hourRange <= 2) and (minRange <= -1)) or (hourRange <= 1):
        # 야근이 아니라고 판단...
        hourRange = -1
    else:
        textTemp = textTemp + ' ---- 야근'
        print(textTemp)
    return hourRange


def setWeekday(get_inTime_list, over_work_time, get_outTime_list, loopidx, loopjdx, overNight, get_day_list):
    # 퇴근설정시간
    overWorkHour = int(over_work_time[0])
    overWorkMin = int(over_work_time[1])
    
    # 야근시간을 시/분으로 나누기
    setEndWork = get_outTime_list[loopidx][loopjdx]
    setEndWorkHour = int(setEndWork[0:2])
    setEndWorkMin = int(setEndWork[3:])

    # 출근시간을 시/분으로 나누기
    setStartWork = get_inTime_list[loopidx][loopjdx]
    setStartWorkHour = int(setStartWork[0:2])

    textTemp = get_day_list[loopidx][loopjdx]

    # 자정후 퇴근이라면...
    if overNight != -1:
        # 자정후 퇴근한것이 진짜 맞다면...
        if setStartWorkHour > setEndWorkHour:
            setEndWorkHour = 24
            setEndWorkMin = 0
        else:
            pass
    else:
        pass

    hourRange = setEndWorkHour - overWorkHour
    minRange = setEndWorkMin - overWorkMin

    # 시간이 2시간 이상이고, 분이 음수가 아니라면...
    if (hourRange > 2) and (minRange <= -1):
        # 해당 야근시간을 리스트에 저장
        hourRange = hourRange - 1
        textTemp = textTemp + ' ---- 야근'
        print(textTemp)
    elif ((hourRange <= 2) and (minRange <= -1)) or (hourRange <= 1):
        # 야근이 아니라고 판단...
        hourRange = -1
    else:
        textTemp = textTemp + ' ---- 야근'
        print(textTemp)
    return hourRange

def checkLeaveWork(store_day_info, store_check_info):
    get_day_list = []
    get_inTime_list = []
    get_outTime_list = []

    # 정상출근/지각, 정상퇴근 찾기
    for loopkdx in range(0, store_check_info.__len__()):

        # 일자 저장
        get_day_list_temp = []
        # 출근 시간 저장(지각 포함)
        get_inTime_list_temp = []
        # 퇴근 시간 저장
        get_outTime_list_temp = []

        get_day_list_temp.append(store_day_info[loopkdx][0])
        get_inTime_list_temp.append(store_check_info[loopkdx][0])
        get_outTime_list_temp.append(store_check_info[loopkdx][0])

        # 아래 for문에서 파싱한 내용 넣기
        get_day_list.append(get_day_list_temp)
        get_inTime_list.append(get_inTime_list_temp)
        get_outTime_list.append(get_outTime_list_temp)

        for loopldx in range(1, store_check_info[loopkdx].__len__()):
            cur_text = store_check_info[loopkdx][loopldx]
            get_text = ''
            find_inTime = cur_text.find('정상출근')
            find_lateTime = cur_text.find('지각')
            # 정상 출근이나 지각을 한 경우 정상퇴근 찾기
            if (find_inTime != -1) or (find_lateTime != -1):
                find_outTime = cur_text.find('정상퇴근')
                find_earlyTime = cur_text.find('조퇴')
                find_overTime = cur_text.find('자정후퇴근')
                if (find_outTime != -1) or (find_earlyTime != -1):
                    # 휴무찾기
                    find_workoffTime = cur_text.find('휴무')
                    # 휴무라면..
                    if find_workoffTime != -1:
                        # 정상 출근이라면..
                        if find_inTime != -1:
                            get_text = returnCurText(cur_text, find_inTime, '정상출근')
                            get_inTime_list_temp.append(get_text)
                        else:
                            # 지각이라면..
                            get_text = returnCurText(cur_text, find_lateTime, '지각')
                            get_inTime_list_temp.append(get_text)

                        # 정상 퇴근이라면...
                        if find_outTime != -1:
                            get_text = returnCurText(cur_text, find_outTime, '정상퇴근')
                            get_outTime_list_temp.append(get_text)
                            # 자정후 퇴근이라면...
                            if find_overTime != -1:
                                get_text = store_day_info[loopkdx][loopldx] + ' / 휴무(자정후퇴근)'
                            # 자정후 퇴근이 아니라면...
                            else:
                                get_text = store_day_info[loopkdx][loopldx] + ' / 휴무'
                            get_day_list_temp.append(get_text)
                        else:
                            # 조퇴라면...
                            get_text = returnCurText(cur_text, find_earlyTime, '조퇴')
                            get_outTime_list_temp.append(get_text)
                            get_text = store_day_info[loopkdx][loopldx] + ' / 휴무'
                            get_day_list_temp.append(get_text)
                    # 휴무가 아니라면..
                    else:
                        if find_earlyTime != -1:
                            # 평일에 조퇴는 야근이 아니므로 패스
                            continue
                        else:
                            # 정상 출근이라면..
                            if find_inTime != -1:
                                get_text = returnCurText(cur_text, find_inTime, '정상출근')
                                get_inTime_list_temp.append(get_text)
                            else:
                                # 지각이라면..
                                get_text = returnCurText(cur_text, find_lateTime, '지각')
                                get_inTime_list_temp.append(get_text)

                            # 정상퇴근
                            get_text = returnCurText(cur_text, find_outTime, '정상퇴근')
                            get_outTime_list_temp.append(get_text)
                                # 자정후 퇴근 이라면...
                            if find_overTime != -1:
                                get_day_list_temp.append(store_day_info[loopkdx][loopldx] + ' / 자정후퇴근')
                                # 자정후 퇴근이 아니라면...
                            else:
                                get_day_list_temp.append(store_day_info[loopkdx][loopldx])
                else:
                    # 퇴근시간이 없으므로 넘어가기
                    continue
            else:
                # 정상출근이나 지각을 하지 않았으므로, 넘어가기
                continue

    return (get_day_list, get_inTime_list, get_outTime_list)


def returnCurText(cur_text, find_index, check_mode):
    set_index = 0
    if (check_mode == '정상출근') or (check_mode == '정상퇴근'):
        set_index = find_index + 4
        check_word = cur_text[set_index]
    else: # 지각 and 조퇴
        set_index = find_index + 2
        check_word = cur_text[set_index]

    if check_word == '-':
        cur_text = cur_text[set_index + 1:set_index + 6]
    else:
        cur_text = cur_text[set_index:set_index + 5]

    return cur_text




