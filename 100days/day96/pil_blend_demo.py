# 融合图像

from PIL import Image

# 蓝色图像
image1 = Image.new('RGB', (128, 128), (0, 0, 255))
# 红色图像
image2=Image.new('RGB', (128, 128), (255, 0, 0))

# 融合两张图片
im  = Image.blend(image1, image2, 0.5)

image1.show()
image2.show()

im.show()
