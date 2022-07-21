import requests
import uuid

#이미지 추출

img_url = "https://movie-phinf.pstatic.net/20220708_75/16572722362230AyHS_JPEG/movie_image.jpg?type=m203_290_2"

#파일 이름 결정
saveName = str(uuid.uuid4())
print(saveName, type(saveName))

#저장위치+파일이름
filePath = "C:\\javaStudy\\upload\\movie\\"+saveName+".jpg"
#print(filePath)

img_response = requests.get(img_url)
#print(response.text)

file = open(filePath, "wb")
file.write(img_response.content)
file.close()
