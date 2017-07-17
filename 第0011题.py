# -*-coding:utf-8-*-


def test(content):
    flag = 0
    with open('filtered_words.txt') as fp:
        for line in fp.readlines():
            if line.strip('\n') in content:
                flag = 1
            else:
                pass

    if flag == 1:
        print "Freedom"
    else :
        print "Human rights"

if __name__ == '__main__':
    test()
