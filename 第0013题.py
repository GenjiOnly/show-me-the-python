# -*-coding:utf-8-*—
'''
    题目描述：
         用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
    地址：
        http://tieba.baidu.com/p/2166231880

    思路：
        用正则表达式匹配图片链接，然后进行下载

'''
'''
import re
import requests

def main():
    url = 'http://tieba.baidu.com/p/2166231880'
    response = requests.get(url)
    html = response.text
    match = re.compile('img .*?src=\"(.*?)\"')
    for i in  match.findall(html):
        if 'imgsrc' in i :
            print i

if __name__ == '__main__':
    main()
'''
 
import urllib2
import re
from os.path import basename
from urlparse import urlsplit

url = "http://tieba.baidu.com/p/2166231880"
def getPage(url):
    url=url+"?see_lz=1"
    urlContent = urllib2.urlopen(url).read()
    page='<span class="red">(.*?)</span>'
    thePage=re.findall(page,urlContent)
    return int(thePage[0])
def downImg(url):
    urlContent = urllib2.urlopen(url).read()    
    spans='<cc>(.*?)</cc>'
    ss=re.findall(spans,urlContent)
    obImgs=','.join(ss)
    imgUrls = re.findall('img .*?src="(.*?)"', obImgs)
    for imgUrl in imgUrls:
        print imgUrl
        '''
        try:
            imgData = urllib2.urlopen(imgUrl).read()
            fileName = basename(urlsplit(imgUrl)[2])
            output = open(fileName,'wb')
            output.write(imgData)
            output.close()
        except:
            print "Er.."
        '''
def downLoad(url):
    numb=getPage(url)
    cont=0
    print "There are "+str(numb)+" pages."
    while cont<numb:
        cont+=1
        print "Downloading "+url+"?see_lz=1&pn="+str(cont)+"..."
        downImg(url+"?see_lz=1&pn="+str(cont))
    print 'Completed!'

downImg(url)