import requests

from PIL import Image
import io # 입출력(Input/Output) 스트림
img_link = 'https://bookthumb-phinf.pstatic.net/cover/168/513/16851325.jpg?type=m1&udate=20210210'
response = requests.get(img_link)
in_memory_file = io.BytesIO(response.content)
im = Image.open(in_memory_file)
im.save('a.png')
print(response.content)

# 이미지 파일을 파이썬 파일로 저장 !!
