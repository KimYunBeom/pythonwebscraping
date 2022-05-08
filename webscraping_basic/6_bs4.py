import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text()) # 텍스트만 가져옴
# print(soup.a) # 처음 발견된 <a>를 가져옴
# print(soup.a.attrs) # <a>의 속성을 dictionary로 가져옴
# print(soup.a.attrs['href']) # <a>의 href 속성의 값

# print( soup.find('a', attrs={'class':'Nbtn_upload'}) ) # 속성 기준으로 a 엘리먼트 찾기
# print( soup.find(attrs={'class':'Nbtn_upload'}) ) # 속성 기준으로 아무 엘리먼트 찾기

# print( soup.find('li', attrs={'class', 'rank01'}) )
rank1 = soup.find('li', attrs={'class', 'rank01'})
print(rank1.a)
