# _*_ coding:utf-8 _*_

import  sys

def show():
    daily=open('daily.txt' , 'r')
    for line in daily:
        print line
    daily.close()

def run():

    print show()
    print "*"*20
    print "w \n"
    print "exit \n"


    Input = str(raw_input('>'))


    if Input == "w":
        txt=open('daily.txt' , 'a')
        while True:
            wir = str(raw_input('写入'))
            if wir == "exit":
                sys.exit()
            else:
                txt.write(wir)
                txt.write('\n')

    elif Input == "exit":
        sys.exit()
if __name__ == '__main__':
    run()