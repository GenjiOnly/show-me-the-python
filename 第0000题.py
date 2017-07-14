#-*-coding:utf-8-*- 
__author__ = 'Deen' 
'''
题目说明：
    将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''
from PIL import Image
from PIL import ImageChops
from PIL import ImageDraw
from PIL import ImageFont

# im = Image.open('source\\0000.jpg')
# print im.getbands()
# print im.mode
# print im.size
# print im.size[0]
# print im.size[1]

'''
PIL使用笛卡尔像素坐标系统，坐标(0，0)位于左上角。注意：坐标值表示像素的角；位于坐标（0，0）处的像素的中心实际上位于（0.5，0.5）。

坐标经常用于二元组（x，y）。长方形则表示为四元组，前面是左上角坐标。例如，一个覆盖800x600的像素图像的长方形表示为（0，0，800，600）。
'''

# info 返回一个对象
# print im.info

'''
 ImageChops模块

ImageChops模块包含一些算术图形操作，叫做channel operations（“chops”）。这些操作可用于诸多目的，比如图像特效，图像组合，算法绘图等等。通道操作只用于8位图像（比如“L”模式和“RGB”模式）。
'''

'''
 ImageDraw模块

ImageDraw模块为image对象提供了基本的图形处理功能。例如，它可以创建新图像，注释或润饰已存在图像，为web应用实时产生各种图形。

ImageDraw模块的使用如下：

>>>from PIL import Image, ImageDraw

>>> im = Image.open('D:\\Code\\Python\\test\\img\\1.jpg')

>>>draw = ImageDraw.Draw(im)

>>>draw.line((0,0) + im.size, fill = 128)

>>>draw.line((0, im.size[1], im.size[0], 0), fill=128)

>>>im.show()

>>> deldraw

>>>im.show()
'''


# im2 = ImageChops.duplicate(im)
# print im2.size
# draw = ImageDraw.Draw(im2)
'''
draw.line((141, 15)+(141, 53), fill=(255, 0, 0))
draw.line((141, 15)+(123, 33), fill=(255, 0, 0))
draw.line((123, 33)+(150, 33), fill=(255, 0, 0), width=5)
'''
'''
ft = ImageFont.truetype("C:/windows/fonts/Arial.ttf", 20)
draw.text((30,30),u"4",font=ft,fill='red')
im2.show()
'''

def add_num(img):
    draw = ImageDraw.Draw(img)
    ft = ImageFont.truetype("C:/windows/fonts/Arial.ttf", 20)
    draw.text((img.size[0]-40, 0), u'99+',font=ft, fill='red')
    img.save('result.jpg', 'jpeg')

    return 0

if __name__ == '__main__':
    image= Image.open('source/0000.jpg')
    add_num(image)
