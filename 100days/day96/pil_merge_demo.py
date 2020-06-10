#  通过单通道创建图像

from PIL import Image

im = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/1581041682390.jpg')
# 将三个通道分开
im_split = im.split()

# 分别显示三个单通道图像
# im_split[0].show()
# im_split[1].show()
# im_split[2].show()

# 将三个通道再次合并
im2 = Image.merge('RGB', im_split)
im2.show()

im3 = Image.open('C:/Users/yanhao/Pictures/Saved Pictures/1581041700586.jpg')

im3_spilt = im3.split()

rgbs = [im3_spilt[0], im_split[0], im_split[1]]

# 选择两张图片中的部分通道，在合并起来
im4 = Image.merge('RGB', rgbs)
im4.show()
