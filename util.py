import requests
from bs4 import BeautifulSoup
import uuid

def imgDown(sub_page_url):
    # sub_page_url 요청 -> 응답(html)
    #요청하기
    response = requests.get(sub_page_url)
    html = response.text

    # 필요한 poster_url 추출
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.select_one(".poster>a>img")
    poster_url = tag["src"]

    # poster_url 요청 -> 응답
    # 파일이름
    saveName = str(uuid.uuid4())

    #저장위치+파일이름
    filePath = "C:\\javaStudy\\upload\\movie\\" + saveName + ".jpg"

    #요청
    img_response = requests.get(poster_url)

    # C:\\javaStudy\\upload\\movie\\ 저장
    file = open(filePath, "wb")
    file.write(img_response.content)
    file.close()

    # 파일경로 리턴
    return filePath

'''
result = imgDown()
print(result)
'''