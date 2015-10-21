__author__ = 'rbeelive'
import  sys
import time


def Get_Time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def show():
    with open('daily.txt','r')as f:
        for line in f.readlines():
            if '#' in line :
                pass
            else:
                print line


def run():


    print show()

    print "*"*20

    print "Usage: hammer.py [Auth] [Options] [Targets]\n"
    print "Usage: hammer.py [Auth] [Options] [Targets]\n"


    Input = str(raw_input('>'))


    if Input == "w":
        txt=open('daily.txt' , 'a')
        while True:
            wir = str(raw_input("www"))
            if wir == "exit":
                sys.exit()
            else:
                txt.write(Get_Time())
                txt.write('\n')
                txt.write(wir)
                txt.write('\n')
                txt.write("#")
                txt.write('\n')
        txt.close()

    elif Input == "exit":
        sys.exit()
if __name__ == '__main__':
    run()