'''
Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

[조회 조건]
1. http://daum.net 접속
2. '송파 헬리오시티' 검색
3. 다음 부동산 부분에 나오는 결과 정보

[출력 결과]
=========== 매물 1 ===========
거래 : 매매
면적 : 84/59 (공급/전용)
가격 : 165,000 (만원)
동 : 214동
층 : 고/23
=========== 매물 2 ===========
   ...

[주의 사항]
- 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def set_browser_option(is_show = True):
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging']) # 메시지 제거 : USB: usb_device_handle_win.cc:1049 Failed to read descriptor from node connection
  if is_show == False:
    options.headless = True
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36')
  return options

# ---

options = set_browser_option(False)
service = Service('./chromedriver')
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()

url = 'https://realty.daum.net/home/apt/danjis/38487/items?business=da_www'
browser.get(url)

elems = browser.find_elements(By.CSS_SELECTOR, 'div.css-1dbjc4n.r-13awgt0.r-eqz5dr.r-1777fci')

for idx, elem in enumerate(elems):
  print('=========== 매물 {} ==========='.format(idx + 1))
  elem_1 = elem.find_element(By.CSS_SELECTOR, 'div:nth-child(1)')
  elem_2 = elem.find_element(By.CSS_SELECTOR, 'div:nth-child(2)')
  elem_1_arr = elem_1.text.split(' ')
  elem_2_arr = elem_2.text.split(' ')
  
  trade_type = elem_1_arr[0]
  
  price1 = elem_1_arr[1]
  price2 = ''
  if len(elem_1_arr) == 3:
    price2 = ' ' + elem_1_arr[2]
  price = price1 + price2

  width = elem_2_arr[0]

  ho = ''
  if len(elem_2_arr) == 2:
    ho = elem_2_arr[1]

  print('거래 : {}'.format(trade_type))
  print('면적(공급/전용) 동 : {}'.format(width))
  print('가격 : {} (원)'.format(price))
  print('호 : {}'.format(ho))

browser.quit()
