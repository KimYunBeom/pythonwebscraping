'''
[IT 뉴스]
1. 무슨 무슨 일이...
 (링크 : http://...)
2. 어떤 어떤 일이...
 (링크 : http://...)
3. 이런 저런 일이...
 (링크 : http://...)
'''

from bs4 import BeautifulSoup
import requests

def create_soup(url):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, 'lxml')
  return soup

def scrape_weather():
  print('[오늘의 날씨]')

  url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'

  soup = create_soup(url)

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

def print_news(index, title, link):
    print('{}. {}'.format(index + 1, title))
    print(' (링크 : {})'.format(link))

def scrape_headline_news():
  print('[언론사별 랭킹뉴스]')

  url = 'https://news.naver.com/main/ranking/popularDay.naver'

  soup = create_soup(url)

  news_list = soup.find_all('ul', {'class':'rankingnews_list'})[0].find_all('a', {'class':'list_title'})

  for index, news in enumerate(news_list):
    title = news.get_text().strip()
    link = news['href']
    print_news(index, title, link)

def scrape_it_news():
  print('[IT 일반]')

  url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'

  soup = create_soup(url)

  news_list = soup.find('ul', {'class':'type06_headline'}).find_all('li', limit=5)

  for index, news in enumerate(news_list):
    a_idx = 0
    img = news.find('img')
    if img:
      a_idx = 1 # img 태그가 있으면 1번째 img 태그의 정보를 사용
    
    a_tag = news.find_all('a')[a_idx]
    title = a_tag.get_text().strip()
    link = a_tag['href']
    print_news(index, title, link)

if __name__ == '__main__':
  # scrape_weather() # 오늘의 날씨 정보 가져오기
  # scrape_headline_news()
  scrape_it_news()
