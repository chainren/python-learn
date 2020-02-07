"""
使用requests下载图片 (或二进制数据)

安装PIL
pip install pillow
"""

import requests

from PIL import Image
from io import BytesIO

resp = requests.get('http://img.sccnn.com/bimg/326/203.jpg')

print(resp.content)

bi = BytesIO(resp.content)

i = Image.open(bi)

print(i)
