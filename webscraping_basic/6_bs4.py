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
# rank1 = soup.find('li', attrs={'class', 'rank01'})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent)

# rank2 = rank1.find_next_sibling('li')
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling('li')
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())

# print(rank1.find_next_siblings('li'))

webtoon = soup.find('a', text='약한영웅-189화')
print(webtoon)
