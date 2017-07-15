'''
题目描述：
  找出一个html文件中所有的url
  
思路 ：
  利用正则表达式进行匹配

'''


import re


with open('test.txt') as fp:
    text = fp.read()
    pattern = re.compile(
        "((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?", re.DOTALL)
    urls = pattern.findall(text)
    for i in urls:
        full_url = ''
        for url in i:
            full_url += url

        print full_url
