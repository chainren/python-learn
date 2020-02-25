from PIL import Image

im = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/风景1.jpg')

#  将每个像素值翻倍（相当于亮度翻倍）
evl1 = Image.eval(im, lambda x: x*2)
evl1.show()

# 将每个像素值减半（相当于亮度减半）
evl2 = Image.eval(im, lambda x : x/2)
evl2.show()