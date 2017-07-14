# -*-coding:utf-8-*-
__author__ = 'Deen'
'''
题目描述：
    你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。


思路：
    获取目录下所有txt文件，逐个打开，进行词频统计，选出出现次数最多的那个
'''
import os
import re


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


if __name__ == '__main__':
    txt_files = list_files()
