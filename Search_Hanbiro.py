import requests
from bs4 import BeautifulSoup as bs # HTML 파싱 : beautifulSoup 사용

# 로그인할 유저정보를 넣어주자(모두 문자열)
LOGIN_INFO = { 'hmil_id': 'tjback123', 'hmil_pass': 'dowk0056' }

# Session 생성, with 구문 안에서 유지, with 구문이 끝나면 자동으로 세션을 닫음
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url과 함께 전송될 data를 넣어주자
    # 한비로 홈페이지 접속
    login_req = s.post('http://suresofttech.hanbiro.net/groupware/login.php', data = LOGIN_INFO)
    #print(login_req.status_code) # 200일 경우 로그인 성공
    if login_req.status_code != 200:
        raise Exception('로그인이 되지 않았습니다. 아이디와 비밀번호를 다시한번 확인해주세요') # raise를 에러를 직접 만든다.

    # -- 여기서부터 로그인 된 세션 유지 --
    set_url = 'http://suresofttech.hanbiro.net/groupware/?category=index&section=main'
    post_one = s.get(set_url)
    print(post_one.text)
   #soup = bs(post_one.text, 'html.parser')
    #date = soup.findAll('tr')