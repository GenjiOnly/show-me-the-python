#-*-coding:utf-8-*- 
__author__ = 'Deen' 
'''
题目描述：任一个英文的纯文本文件，统计其中的单词出现的个数。
参考学习链接：
    re  http://www.cnblogs.com/tina-python/p/5508402.html#undefined
    collections  http://blog.csdn.net/liufang0001/article/details/54618484
'''
import re,collections
with open('english.txt','r') as fp:
    text=fp.read().strip(',')
    s=re.compile(r'\w+\b')
    words=s.findall(text)
    b=list()
    dic=collections.defaultdict(lambda :0)
    for word in words:
        dic[word.lower()] +=1

    print dic

'''
import collections,re
import sys
def cal(filename = 'english.txt'):
	print 'now processing:' + filename + '......'
	f = open(filename,'r')
	data = f.read()
	dic = collections.defaultdict(lambda :0)
	data = re.sub(r'[\W\d]',' ',data)
	data = data.lower()
	datalist = data.split(' ')
	for item in datalist:
		dic[item] += 1
	del dic['']
	return dic
try:
	print sorted(cal().items())
except:
	print 'no input file'
'''