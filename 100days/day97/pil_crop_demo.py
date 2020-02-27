#  从图片中按某个坐标位置扣取一个图Image.crop(box) box = (0,0,240,240)

from PIL import Image

im = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/风景1.jpg')
print(im.size)
im.show()

# 定义了图像的坐标位置，从左、上、右、下
box = (100, 100, 400, 400)

region = im.crop(box)
print(region.size)

region.show()

