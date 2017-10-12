from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

def search_hanbiro_main(sure_id, sure_pw):
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
    # 자동 로그인 시도(비밀번호가 맞지 않을때 에러 구현 필요)
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td').click()
    # 바로 접속하면 캘린더로 접속이 안되므로 3초의 여유를 둔다.
    time.sleep(3)

    if (driver.current_url != login_adress):
        print('로그인 실패!!')
    else:
        print('로그인 성공!!')
        check_login = True

    return (check_login, driver)

def enter_calendar(driver, inout_year, inout_day):
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
    store_day_info = []
    # 출근체크 저장
    store_check_info = []
    for loopjdx in range(0, get_day_info.__len__()):
        store_day_info.append(get_day_info[loopjdx][1].text)
        store_check_info.append(get_day_info[loopjdx][3].text)
        store_check_info[loopjdx] = store_check_info[loopjdx].replace('\t','')
        store_check_info[loopjdx] = store_check_info[loopjdx].replace('\n', '')
        store_check_info[loopjdx] = store_check_info[loopjdx].replace(' ', '')


    get_check_day = []
    get_check_time = []
    # 정상퇴근 찾기
    for loopkdx in range(0, store_check_info.__len__()):
        cur_text = store_check_info[loopkdx]
        find_index = cur_text.find('정상퇴근')
        if find_index != -1:
            # 정상퇴근을 찾으면 해당 날짜 저장
            get_check_day.append(store_day_info[loopkdx])
            # 해당 시간 저장
            cur_text = cur_text[find_index+5:find_index+10]
            get_check_time.append(cur_text)

    store_over_work_day = []
    store_over_work_time = []
    store_over_work_range = []
    set_over_work_time = 18
    # 본사에서 8시 이후 퇴근한 날(다른 파견지도 넣을 예정)
    for loopmdx in range(0, get_check_time.__len__()):
        check_time = get_check_time[loopmdx] #'19:23'
        check_time = check_time[0:2] #'19'
        check_time = int(check_time) #19
        # 야근 했다면..
        if set_over_work_time < check_time:
            range_time = check_time - set_over_work_time
            if range_time >= 2:
                store_over_work_day.append(get_check_day[loopmdx])
                store_over_work_time.append(get_check_time[loopmdx])
                str_range_time = str(range_time)
                str_range_time = str_range_time + '시간'
                store_over_work_range.append(str_range_time)

    # HTML 파싱 끝(브라우져 종료)
    driver.close()
    return (store_over_work_day, store_over_work_time, store_over_work_range)


# 메인
if __name__  == "__main__":
    option = '야근경비'
    [check_login, driver] = search_hanbiro_main('tjback123', 'xxxx')

    if check_login != False:
        if option == '야근경비':
            [store_over_work_day, store_over_work_time, store_over_work_range] = enter_calendar(driver, '2016', '01')
            if not store_over_work_day:
                print('야근한 날이 없습니다.')
            else:
                # 엑셀 파싱 함수넣기
                pass
        else:
            # 옵션 더 추가..?
            pass
    else:
        pass
