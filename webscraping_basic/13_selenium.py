from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome() # './chromedriver.exe'

# 1. 네이버 이동
browser.get('http://naver.com')

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CSS_SELECTOR, '.link_login')
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, 'id').send_keys('id1') # TODO 실제 ID가 필요
browser.find_element(By.ID, 'pw').send_keys('pw1')

time.sleep(1)

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, 'log.login').click()

# 5. id 를 새로 입력
browser.find_element(By.ID, 'id').clear()
browser.find_element(By.ID, 'id').send_keys('id2')

# 6. html 정보 출력
print(browser.page_source)

time.sleep(1)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료
