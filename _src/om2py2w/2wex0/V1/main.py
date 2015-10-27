__author__ = 'rbeelive'
# -*- coding: UTF-8 -*-
from Tkinter import *
import tkMessageBox
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
【问题】
查看历史弹出多个对话框
"""

def Get_Time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def show():
    with open('1.txt', 'r')as f:
        for line in f.readlines():
            tkMessageBox.showinfo("title",line)


            #root.mainloop()



def wir():
    txt = open('1.txt', 'a')
    wir = text.get("1.0",END)
    data = Get_Time() + '|' + wir + '\n'
    txt.write(data)
    txt.close()



"""
1 创建容器存放元素
2 创建元素
3 指定容器包含元素
4 设置容器属性
5 界面构建
"""

def run():
    global  text
    global root
    root = Tk()
    root.title('笔记')

# 创建容器
    main=Frame()
    r=Frame()
    but=Frame()
    lal=Frame()

# 创建元素
    logo=Label(r,text='Readm')
    text=Text(main)
    b=Button(but,text='走着',command=wir)
    s=Button(lal,text='历史',command=show)



# 位置
    main.grid(row=0, column=0, padx=2, pady=5)
    but.grid(row=1, column=0, padx=2, pady=5)
    lal.grid(row=2, column=0, padx=2, pady=5)
    r.grid(row=0, column=1, padx=1, pady=1)
    """
grid() 参数说明
row:行
columu:列
padx, pady: 多少部件的像素，水平和垂直方向
grid_propagate 父组将集合大小有组件控制
    """

    main.grid_propagate(0)
    but.grid_propagate(0)
    r.grid_propagate(0)



    logo.pack()
    text.pack()
    b.pack()
    s.pack()

    root.mainloop()
if __name__=="__main__":
    run()


