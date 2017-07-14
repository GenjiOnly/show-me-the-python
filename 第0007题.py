# -*-coding:utf-8-*-
__author__ = 'Deen'
'''
题目描述：
    有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

    根据注释和正常语句的区别，进行筛选计数
'''

import os


# 首先还是获取该目录下所有文件名，返回一个list进行储存
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


def count(file):
    blank_num = 0
    code_num = 0
    annotations_num = 0
    line_num = 0
    annotations_nums = list()
    with open(file) as fp:
        for line in fp.readlines():
            line_num += 1
            line = line.strip('\n')
            if '#' in line:
                annotations_num += 1
            if "'''" in line:
                annotations_nums.append(line_num)
            elif len(line) > 0:
                code_num += 1
            else:
                blank_num += 1

        fp.close()

    j = 0
    result = 0
    for i in annotations_nums:
        j += 1
        if j % 2 == 0:
            result += int(i) - annotations_nums[j - 2]
    return code_num, annotations_num + result + 1, blank_num


if __name__ == '__main__':
    files = list_files('G://code')
    for file in files:
        count_result = count(file)
        dic = dict(zip(['code_num', 'annotations_num', 'blank_num'], list(count_result)))
        print dic
