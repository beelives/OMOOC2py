__author__ = 'rbeelive'
# -*- coding: UTF-8 -*-
# 使用Listbox控件显示文件内容
#1 显示内容太小

from Tkinter import *

i=open('Tk.md','r')

root = Tk()

txt=Listbox(root)

for file in i:
    #print file
    txt.insert(0,file)

txt.pack()
root.mainloop()