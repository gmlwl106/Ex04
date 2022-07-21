import requests
from bs4 import BeautifulSoup

#1.사이트에 요청 응답(html)을 받기
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

#요청하기
response = requests.get(url);

#응답확인
print(response.status_code) #상태코드
html = response.text

#2. 필요한 태그 추출하기 - BeautifulSoup
soup = BeautifulSoup(html, "html.parser") #parser:(html)문자열 자름
'''
tag = soup.select_one(".tit3>a")
print(tag)
'''
tags = soup.select(".tit3>a")
'''
for tag in tags:
    title = tag.text
    print(title)
'''

for index, tag in enumerate(tags): #index 값도 같이 사용할때 enumerate 사용
    rank = index + 1
    title = tag.text
    print(rank, title)