__author__ = 'rbeelive'
from Tkinter import *
import tkMessageBox
# -*- coding: UTF-8 -*-

class ConfigWindow(Frame):
    def __init__(self):
            Frame.__init__(self)
            self.master.title('Tk Demo')  # 窗口标题
            self.master.geometry('500x300')  # 屏幕位置
            self.master.resizable(False, False) # 禁止改变窗口大小
            self.pack(side = TOP,expand = YES,fill = BOTH) # 将窗口放置在屏幕
            bt = Button(self,text='hello',command=self.hello) # 创建按钮
            bt.pack(side=TOP,expand=NO,fill=Y,pady=20,padx=20) # 将按钮放在窗口

    def hello(self):
            tkMessageBox.showinfo('Info','Hello,This is a demo for tkinter');


if __name__ == '__main__':
    ConfigWindow().mainloop()