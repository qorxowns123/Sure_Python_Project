from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 한비로 로그인 주소
web_address = 'http://suresofttech.hanbiro.net/groupware/login.php'
calendar_address = 'http://suresofttech.hanbiro.net/groupware/?category=time&section=userCalendar'
# 구글 크롬 드라이버 사용(나중에는 PhantomJS를 사용할 예정)
driver = webdriver.Chrome('D:\chromedriver_win32/chromedriver')
# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)
# 한비로 접속
driver.get(web_address)
# 아이디 입력
driver.find_element_by_name('hmail_id').send_keys('tjback123')
# 비밀번호 입력
driver.find_element_by_name('hmail_pass').send_keys('xxxx')
# 자동 로그인 시도
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td').click()
# 바로 접속하면 캘린더로 접속이 안되므로 3초의 여유를 둔다.
time.sleep(3)
# 캘린더로 접속
driver.get(calendar_address)

# 이전달로 이동
# driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/span[1]').click()

# 다음달로 이동
# driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/span[2]').click()

# 웹페이지 소스 추출
get_html = driver.page_source
# HTML 소스 읽어오기
get_parser = BeautifulSoup(get_html, 'html.parser')
# 출근 정보 태그
get_tag = get_parser.find_all('img')

