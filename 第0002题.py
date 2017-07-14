#-*-coding:utf-8-*- 
__author__ = 'Deen' 
'''
题目描述：
    将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
"""
import MySQLdb as mdb

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'db': 'student',
    'charset': 'utf8'
}
conn = mdb.connect(**config)
cursor = conn.cursor(cursorclass=mdb.cursors.DictCursor)



cursor.execute('set names gbk')



n=0
num=list()


for line in open("student12.txt"):
	line=line.decode('gbk').encode('utf-8')

	n=n+1

	if n%6==1:
		cursor.execute('insert into student12(sno) VALUES (%s)'%(line))

"""

import MySQLdb as mdb

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'db': 'ctf_test',
    'charset': 'utf8'
}
conn = mdb.connect(**config)
cursor = conn.cursor(cursorclass=mdb.cursors.DictCursor)
cursor.execute('set names gbk')

cursor.execute('create table codes(id int(5),code char(20))')
with open('poll_codes.txt','r') as fp:
    for line in fp.readlines():
        line = line.strip('\n').split(':')
        cursor.execute('INSERT INTO codes VALUES (%s,%s)',line)


conn.commit()
cursor.close()
conn.close()





