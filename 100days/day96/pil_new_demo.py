from PIL import Image

# 创建一个图片，RGB模式，尺寸450，450，红色
im = Image.new('RGB',(450,450), (255, 245, 180))
im.show()

im1 = Image.new('RGB', (450,450), 'green')
im1.show()


im2 = Image.new('RGB', (450, 450), '#FF0000')
im2.show()

# 保存图片
# im2.save('./im2.jpg')

im2_copy = Image.open('./im2.jpg')

# 图片类型
print(im2_copy.format)

# 转成png格式
#im2_copy.save('im2.png')

im2_png = Image.open('./im2.png')

print(im2_png.format)

