from PIL import Image
from io import BytesIO

import requests

# 打开图像文件
img = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/风景1.jpg')

# 从文件流中打开图像
r = requests.get('http://f.hiphotos.baidu.com/image/pic/item/b151f8198618367aa7f3cc7424738bd4b31ce525.jpg')
img1 = Image.open(BytesIO(r.content))

# 展示图像
#img.show()
img1.show()

# 翻转90度展示
img1.rotate(90).show()

