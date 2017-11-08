from selenium import webdriver
from bs4 import BeautifulSoup
import time
import Create_ExcelFile

class SearchHanbiro:
    def search_hanbiro_main(self, sure_id, sure_pw):
        # 한비로 로그인 주소
        main_address = 'http://suresofttech.hanbiro.net/groupware/login.php'
        # 로그인 화면
        login_adress = 'http://suresofttech.hanbiro.net/groupware/?category=index&section=main'
        # 정상로그인 확인
        check_login = False
        # 구글 크롬 드라이버 사용(나중에는 PhantomJS를 사용할 예정)
        driver = webdriver.Chrome('D:\chromedriver_win32/chromedriver')
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

        if (driver.current_url != login_adress):
            print('로그인 실패!!')
        else:
            print('로그인 성공!!')
            check_login = True

        return (check_login, driver)

    def enter_calendar(self, driver, inout_year, inout_day):
        # 한비로 캘린더 주소
        calendar_address = 'http://suresofttech.hanbiro.net/groupware/?category=time&section=userCalendar'

        driver.get(calendar_address)
        # 목록으로 보기
        driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/button[1]').click()
        # 년도 입력
        driver.find_element_by_name('syear').send_keys(inout_year)
        # 월 입력
        driver.find_element_by_name('smonth').send_keys(inout_day)
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

        # 일자 저장
        store_day_info_temp = []
        # 출근체크 저장
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

        cnt = 1
        week_mode = str(cnt) + '주차'
        temp_store_day_info.append(week_mode)
        temp_store_check_info.append(week_mode)

        for looppdx in range(0, store_day_info_temp.__len__()):
            if store_day_info_temp[looppdx][12] == '일':
                cnt = cnt + 1
                week_mode = str(cnt) + '주차'

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

        # store_day_info.__len__() # 리스트 전체 갯수
        # store_day_info[0].__len__() # 0번째 리스트 개수

        get_check_day = []
        get_check_info = []

        # 정상퇴근 찾기
        for loopkdx in range(0, store_check_info.__len__()):

            get_check_day_temp = []
            get_check_info_temp = []

            get_check_day_temp.append(store_day_info[loopkdx][0])
            get_check_info_temp.append(store_check_info[loopkdx][0])

            get_check_day.append(get_check_day_temp)
            get_check_info.append(get_check_info_temp)

            for loopldx in range(1, store_check_info[loopkdx].__len__()):
                cur_text = store_check_info[loopkdx][loopldx]
                find_index = cur_text.find('정상퇴근')
                if find_index != -1:
                    # 정상퇴근을 찾으면 해당 날짜 저장
                    get_check_day_temp.append(store_day_info[loopkdx][loopldx])
                    # 해당 시간 저장
                    cur_text = cur_text[find_index + 5:find_index + 10]
                    get_check_info_temp.append(cur_text)
                else:
                    pass

        store_over_work_day = []
        store_over_work_time = []
        store_over_work_money = []
        set_over_work_time = 18

        store_over_work_day_temp = []
        store_over_work_time_temp = []
        store_over_work_money_temp = []

        # 본사에서 8시 이후 퇴근한 날
        for loopmdx in range(0, get_check_info.__len__()):
            if not store_over_work_day_temp:
                pass
            else:
                store_over_work_day.append(store_over_work_day_temp)
                store_over_work_time.append(store_over_work_time_temp)
                store_over_work_money.append(store_over_work_money_temp)

                store_over_work_day_temp = []
                store_over_work_time_temp = []
                store_over_work_money_temp = []

            if get_check_info[loopmdx].__len__() == 1:
                continue
            else:
                for loopndx in range(1, get_check_info[loopmdx].__len__()):
                    check_time = get_check_info[loopmdx][loopndx]  # '19:23'
                    check_time = check_time[0:2]  # '19'
                    check_time = int(check_time)  # 19

                    # 야근 했다면..
                    if set_over_work_time < check_time:
                        range_time = check_time - set_over_work_time
                        if range_time >= 2:
                            store_over_work_day_temp.append(get_check_info[loopmdx][0])  # ? 주차
                            store_over_work_day_temp.append(get_check_info[loopmdx][loopndx])  # 시간

                            store_over_work_time_temp.append(get_check_info[loopmdx][0]) # ? 주차
                            store_over_work_time_temp.append(get_check_day[loopmdx][loopndx]) # 날짜

                            store_over_work_money_temp.append(get_check_info[loopmdx][0])
                            if (range_time >= 2 and range_time < 4):
                                store_over_work_money_temp.append('10,000')
                            elif (range_time >= 4 and range_time < 8):
                                store_over_work_money_temp.append('20,000')
                            elif range_time >= 8:
                                store_over_work_money_temp.append('40,000')
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass

        for looopqdx in range(0, store_over_work_time.__len__()):
            for loopwdx in range(1, store_over_work_time[looopqdx].__len__()):
                fix_text = store_over_work_time[looopqdx][loopwdx]
                fix_text = fix_text[5:] # 01-06 (수)
                fix_text = fix_text[0:5]
                fix_text = fix_text[0:2] + '월' + fix_text[3:5] + '일'
                store_over_work_time[looopqdx][loopwdx] = fix_text

        print(store_over_work_day)
        print(store_over_work_time)
        print(store_over_work_money)

        return (store_over_work_day, store_over_work_time, store_over_work_money)


# 메인
if __name__  == "__main__":
    class_hanbiro = SearchHanbiro()
    class_createexcelfile = Create_ExcelFile.CreateExcelFile()

    [check_login, driver] = class_hanbiro.search_hanbiro_main('tjback123', 'wkfmqks0047')

    if check_login != False:
        [store_over_work_day, store_over_work_time, store_over_work_money] = class_hanbiro.enter_calendar(driver, '2016', '03')
        if not store_over_work_day:  # 조금 더 생각해 보기
            print('야근한 날이 없습니다.')
        else:
            # 엑셀 파싱 함수넣기
            class_createexcelfile.create_xlsx(store_over_work_day, store_over_work_time, store_over_work_money)
    else:
        pass