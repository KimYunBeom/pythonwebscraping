from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = 'https://play.google.com/store/movies'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36', 'Accept-Language': 'ko-KR,ko'}
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도)의 높이인 1080 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)') # 1920 x 1080
# browser.execute_script('window.scrollTo(0, 2080)')

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
  # 스크롤을 가장 아래로 내림
  browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

  # 페이징 로딩 대기
  time.sleep(interval)

  # 현재 문서 높이를 가져와서 저장
  curr_height = browser.execute_script('return document.body.scrollHeight')

  # 이전 높이와 현재 높이가 같으면, 즉 더 로딩하지 않는다면 종료
  if curr_height == prev_height:
    break

  # 변경된 높이만큼 현재 높이를 업데이트
  prev_height = curr_height

print('스크롤 완료')
