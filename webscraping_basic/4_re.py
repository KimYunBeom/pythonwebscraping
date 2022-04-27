'''
주민등록번호
901201-1111111

이메일 주소
nadocoding@gmail.com
nadocoding@gmail.com@gmail.com

차량 번호
11가 1234
123가 1234

IP 주소
192.168.0.1
1000.2000.3000.4000
'''

import re

# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile('ca.e') 
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)  : 문자열의 끝 > case, base (O) | face (X)

def print_match(m):
  if m:
    print(m.group())
  else:
    print('매칭되지 않았습니다')

m = p.match('careless') # match() : 주어진 문자열이 처음부터 일치하는지 확인
print_match(m)
