# -*-coding:utf-8-*-

'''
题目描述：
  使用 Python 生成类似于下图中的字母验证码图片

思路：
  运用PIL库加random 随机字母进行生成

'''

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def rnword():
    return random.choice(string.letters)


def color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def draw(width, height, n):
    bgcolor = (255, 2155, 255)
    image = Image.new('RGB', (width, height), bgcolor)
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', 30)
    fontcolor = (0, 0, 0)
    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=color())

    for w in range(n):
        draw.text((60 * w + 10, 10), rnword(), font=font, fill=color2())

    image = image.filter(ImageFilter.BLUR)
    image.save('test3.jpg', 'jpeg')


if __name__ == '__main__':
    draw(240, 60, 4)
