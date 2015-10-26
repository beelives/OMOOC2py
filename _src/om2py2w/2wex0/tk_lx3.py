__author__ = 'rbeelive'
# -*- coding: UTF-8 -*-
#向该空间输入文本
#http://www.cnblogs.com/kaituorensheng/p/3287652.html

from Tkinter import *
root = Tk()
root.title("hello world")
root.geometry('300x200')

t = Text(root)
#t.insert(1.0, 'hello\n')
#t.insert(END, 'hello000000\n')
#t.insert(END, 'nono')
t.pack()

root.mainloop()