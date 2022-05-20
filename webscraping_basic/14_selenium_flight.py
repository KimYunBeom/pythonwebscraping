from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com'
browser.get(url) # url 로 이동

# 가는 날 선택 클릭
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

time.sleep(1)

# 이번달 27일, 28일 선택
# browser.find_elements(By.XPATH, '//b[text()="27"]')[0].click()
# browser.find_elements(By.XPATH, '//b[text()="28"]')[0].click()

# 다음달 27일, 28일 선택
# browser.find_elements_by_xpath('//b[text()="27"]')[1].click()
# browser.find_elements(By.XPATH, '//b[text()="28"]')[1].click()

# 이번달 27일, 다음달 28일 선택
browser.find_elements(By.XPATH, '//b[text()="27"]')[0].click()
browser.find_elements(By.XPATH, '//b[text()="28"]')[1].click()

# 제주도 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()

time.sleep(1)

browser.find_element(By.CSS_SELECTOR, '.autocomplete_input__1vVkF').send_keys('제주')

time.sleep(1)

browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a/div/div[1]/i[1]/mark').click()

browser.find_element(By.CSS_SELECTOR, 'div.main_searchbox__3vrV3 > div > div > button').click()
