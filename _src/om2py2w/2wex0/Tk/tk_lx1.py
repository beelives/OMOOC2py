__author__ = 'rbeelive'
from Tkinter import *
# -*- coding: UTF-8 -*-
# 使用消息控件弹出文件内容
# 消息控件特点，不能选则和查看
i=open('Tk.md','r')
root = Tk()
for file in i:
    Message(root,text =file).pack()
root.mainloop()