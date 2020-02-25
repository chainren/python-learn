# 缩略图

from PIL import Image

im = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/风景1.jpg')

im.show()

# 缩放
im.thumbnail((128,128), Image.ANTIALIAS)
im.show()
