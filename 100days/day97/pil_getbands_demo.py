from PIL import Image

im = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/风景1.jpg')
# 创建新图像
im1 = Image.new('L', (450, 450), 50)

# 获取图像的通道名称元组
print(im.getbands())
print(im1.getbands())