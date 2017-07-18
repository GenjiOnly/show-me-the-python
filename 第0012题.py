# -*-coding:utf-8-*-


def test(content):
    text = content
    flag = 0
    with open('filtered_words.txt') as fp:
        for line in fp.readlines():
            text = text.replace(line.strip('\n'),'**')
            # print text
        #print text
        fp.close()
    print text
               

    

if __name__ == '__main__':
    test()
