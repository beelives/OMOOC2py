#!/usr/bin/env python
#encoding:utf-8

from main import PostToolGUI
import time
import httplib
import tkMessageBox
import threading
import chardet





def Get_Time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))




class PostTool(PostToolGUI):
    def wir(val):
        txt = open('daily.txt', 'a')
        data = Get_Time() + '|' + val + '\n'
        txt.write(data)
        txt.close()
    def cmd_click(self, event):
        url = self.txtData.get("1.0", "end-1c")
        if url=='':
            tkMessageBox.showinfo('(→_→)', '什么都没有存什么')
        else:
            txt = open('daily.txt', 'a')
            data = Get_Time() + '|' + url + '\n'
            txt.write(data)
            txt.close()

            tkMessageBox.showinfo('(→_→)', '保存成功不在写点什么！')






    def cmd_show(self,event):
        with open('daily.txt','r') as f:
            for line in f.readlines():
                s=line

            tkMessageBox.showinfo('(→_→)', message =s)


app = PostTool()
app.root.mainloop()
