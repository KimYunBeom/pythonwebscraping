import requests
res = requests.get('http://nadocoding.tistory.com')

# if you get 403 response from tistory
# url = 'http://nadocoding.tistory.com'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
# res = requests.get(url, headers=headers)
res.raise_for_status()

with open('nadocoding.html', 'w', encoding='utf8') as f:
  f.write(res.text)
