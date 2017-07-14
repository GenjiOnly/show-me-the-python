# -*-coding:utf-8-*-
__author__ = 'Deen'
'''
题目说明： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

思路： 先获取该目录下所有图片的绝对路径，再一个一个打开,resiz改变大小保存
'''

from PIL import Image
import os


# 获取目录下所有图片的绝对路径
def list_files(dir, wirldcard, recursion):
    files_text = list()
    exts = wirldcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            list_files(fullname, wirldcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    files_text.append(fullname)
                    break
    # print files_text
    return files_text


def images_resize(imgs, width, height):
    n = 0
    for img in imgs:
        n += 1
        image = Image.open(img)
        out = image.resize((width, height), Image.ANTIALIAS)
        out.save(str(n) + '.jpg', 'jpeg')


if __name__ == '__main__':
    dir = "E:\\images"
    wildcard = ".jpg .png"
    images_resize(list_files(dir, wildcard, 1), 500, 500)

'''
参考代码：
import os

from PIL import Image

def resize_image(image):
	im = Image.open(image)
	width, height = im.size
	if height > 1136 or width > 640:
		th = height / 1136
		td = width / 640
		ts = max(th, td)
		nh = int(height / ts)
		nw = int(width / ts)
		im = im.resize((nw, nh))
		im.save(image)
		print('Successfully resized %s. New width is %i, new height is %i.' % (image, nh, nw))
	else:
		print("There's no need to resize %s." % image)

def main():
	for i in os.listdir():
		try:
			resize_image(i)
		except IOError:
			print("Oops! %s is not supported to make the change!" % i)

if __name__ == '__main__':
	main()

'''
