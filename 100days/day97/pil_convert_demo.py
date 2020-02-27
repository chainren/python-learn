from PIL import Image

im = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/风景1.jpg')

im.show()

# 将图像转换成黑白色并返回新图像
im1 = im.convert('L')
im1.show()