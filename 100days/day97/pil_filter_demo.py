from PIL import Image, ImageFilter

im = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/风景1.jpg')

# im.show()

# 模糊
#im2 = im.filter(ImageFilter.BLUR)
#im2.show()

# 轮廓滤波
#im3 = im.filter(ImageFilter.CONTOUR)
#im3.show()

# 细节增强
im4 = im.filter(ImageFilter.DETAIL)
im4.show()