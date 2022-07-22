from selenium import webdriver
from selenium.webdriver.common.by import By

#브라우저 생성
wd = webdriver.Chrome("C:\\javaStudy\\chromedriver\\chromedriver.exe")

#사이트 요청
url = "https://movie.daum.net/moviedb/grade?movieId=132346"
wd.get(url)
wd.implicitly_wait(10) #최대 10초 로딩 끝나면 그 전에 끝남

#더보기 클릭
while(True):
    try:
        wd.find_element(By.CSS_SELECTOR, ".alex_more").click()
        wd.implicitly_wait(2)
    except:
        print("마지막")
        break



#필요한 태그 추출하기 webdriver
cmt_tags = wd.find_elements(By.CSS_SELECTOR, ".cmt_info")

for i, cmt_tag in enumerate(cmt_tags):
    point = cmt_tag.find_element(By.CSS_SELECTOR, ".ratings").text

    try:
        cmt = cmt_tag.find_element(By.CSS_SELECTOR, "li p").text
    except:
        cmt = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        
    date = cmt_tag.find_element(By.CSS_SELECTOR, ".txt_date").text

    print(i+1, point, cmt, date, end="\n\n")
