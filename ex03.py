import requests
from bs4 import BeautifulSoup
import util

#댓글 추출

#1.사이트에 응답(html)을 받기 - requests
url = "https://movie.daum.net/moviedb/grade?movieId=132346"

#요청하기
response = requests.get(url);

html = response.text
#print(html)

#2.필요한 태그 추출하기 - BeautifulSoup4
soup = BeautifulSoup(html, "html.parser")
tags = soup.select(".cmt_info")
print(tags)