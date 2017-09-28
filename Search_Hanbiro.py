from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver_win32/chromedriver')
driver.implicitly_wait(3)
web_address = 'http://suresofttech.hanbiro.net/groupware/login.php'
driver.get(web_address)
driver.find_element_by_name('hmail_id').send_keys('tjback123')
driver.find_element_by_name('hmail_pass').send_keys('비밀번호')
# /html/body/form/table/tbody/tr[1]/td/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td').click()
