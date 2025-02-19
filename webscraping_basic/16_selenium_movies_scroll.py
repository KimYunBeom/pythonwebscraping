import time
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = 'https://play.google.com/store/movies'
browser.get(url)

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

soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all('div', attrs={'class':'ULeU3b neq64b'})
print(len(movies))

for movie in movies:
  title = movie.find('div', attrs={'class':'Epkrse'})
  if title:
    title = title.get_text()
  else:
    continue
  
  # 할인 전 가격
  original_price = movie.find('span', attrs={'class':'SUZt4c P8AFK'}
  )
  if original_price:
    original_price = original_price.find('span').get_text()
  else:
    continue

  # 할인된 가격
  price = movie.find('span', attrs={'class':'VfPpfd VixbEe'})
  if price:
    price = price.find('span').get_text()
  else:
    continue

  # 링크
  link  = movie.find('a', attrs={'class':'Si6A0c ZD8Cqc'})['href']
  # 올바른 링크 : https://play.google.com + link

  print(f'제목 :{title}')
  print(f'할인 전 금액 :{original_price}')
  print(f'할인 후 금액 :{price}')
  print('링크 : ', 'https://play.google.com' + link)
  print('-' * 100)

browser.quit()
