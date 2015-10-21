# -*- coding: UTF-8 -*-
__author__ = 'rbeelive'

import sys
import time


def Get_Time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

def show():
    with open('daily.txt', 'r')as f:
        for line in f.readlines():
            tt = line.split('|')
            str = " 您在%s  曰:%s" % (tt[0], tt[1])
            print str

def write():
    txt = open('daily.txt', 'a')
    while True:
        wir = str(raw_input("曰:"))
        if wir == "exit":
            sys.exit()
        else:
            data = Get_Time() + '|' + wir + '\n'
            txt.write(data)
    txt.close()

def run():
    print show()

    print "*" * 10 + "使用帮助" + "*" * 10
    print "w: w -> write 写作模式\n"
    print "e: e -> exit 退出写作\n"
    print "n: n -> Null 清空你的秘密 \n"
    print "*" * 20

    Input = str(raw_input(':'))

    if Input == "w":
        write()
    elif Input == "e":
        sys.exit()
    elif Input == "n":
        txt = open('daily.txt', 'w')
        write()


if __name__ == '__main__':
    run()