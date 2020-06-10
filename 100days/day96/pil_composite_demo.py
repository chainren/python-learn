# 组合两张图片

from PIL import Image

image1 = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/1581041682390.jpg')

image2 = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/1581041700586.jpg')

# 分离image1的通道
r, g, b = image1.split()

# 合成图像
im = Image.composite(image1, image2, mask=b)
im.show()