'''
[오늘의 날씨]
흐림, 어제보다 00˚ 높아요
현재 00˚(최저 00˚ / 최고 00˚)
오전 강수확률 00% / 오후 강수확률 00%

미세먼지 00㎍/㎥좋음
초미세먼지 00㎍/㎥좋음
'''

from bs4 import BeautifulSoup
import requests

def scrape_weather():
  print('[오늘의 날씨]')

  url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, 'lxml')

  # 흐림, 어제보다 00˚ 높아요
  cast = soup.find('p', attrs={'class':'summary'}).get_text()
  
  # 현재 00˚(최저 00˚ / 최고 00˚)
  curr_temp = soup.find('div', attrs={'class':'temperature_text'}).get_text().replace('온도', '').lstrip()
  min_temp = soup.find_all('span', attrs={'class':'lowest'})[0].get_text()
  max_temp = soup.find_all('span', attrs={'class':'lowest'})[1].get_text()
  
  morning_rain_rate = soup.find_all('span', attrs={'class':'rainfall'})[0].get_text()
  afternoon_rain_rate = soup.find_all('span', attrs={'class':'rainfall'})[1].get_text()

  pm10 = soup.find_all('li', attrs={'class':'level2'})[0].find('span').get_text()
  pm25 = soup.find_all('li', attrs={'class':'level2'})[1].find('span').get_text()

  print(cast)
  print('{} ({} / {})'.format(curr_temp, min_temp, max_temp))
  print('오전 강수확률 {} / 오후 강수확률 {}'.format(morning_rain_rate, afternoon_rain_rate))
  print()
  print('미세먼지 {}'.format(pm10))
  print('초미세먼지 {}'.format(pm25))
  print()

if __name__ == '__main__':
  scrape_weather() # 오늘의 날씨 정보 가져오기

