# -*-coding:utf-8-*-
__author__ = 'Deen'
'''
题目描述：
     一个HTML文件，找出里面的正文。

思路：
    利用BeautifulSoup或者正则表达式

'''
'''
import requests
from bs4 import BeautifulSoup


def get_body(url):
    response = requests.get(url)
    soup = BeautifulSoup(response)
    print soup.body.text
'''
from bs4 import BeautifulSoup

def find_the_content(path):
    with open(path) as f:
        text = BeautifulSoup(f, 'lxml')
        content = text.get_text().strip('\n')

        return content.encode('gbk','ignore')


if __name__ == '__main__':
    print find_the_content('Show-Me-the-Code_show-me-the-code_1.html')
