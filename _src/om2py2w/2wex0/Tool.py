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
        txt = open('1.txt', 'a')
        data = Get_Time() + '|' + val + '\n'
        txt.write(data)
        txt.close()
    def cmd_click(self, event):
        url = self.txtData.get("1.0", "end-1c")
        if url=='':
            tkMessageBox.showinfo('(→_→)', '什么都没有存什么')
        else:
            txt = open('1.txt', 'a')
            data = Get_Time() + '|' + url + '\n'
            txt.write(data)
            txt.close()

            tkMessageBox.showinfo('(→_→)', '保存成功不在写点什么！')






    def cmd_show(self,event):
        with open('1.txt','r') as f:
            for line in f.readlines():
                s=line

            tkMessageBox.showinfo('(→_→)', message =s)





def post(self):
    self.cmdPost.config(text='Posting...', state='disabled')
    self.txtHTML.delete('1.0', 'end')    #clear txtHTML
    try:
        if self.protocol == 'http':
            conn = httplib.HTTPConnection(self.host)
        else:
            conn = httplib.HTTPSConnection(self.host)
        self.cmdPost.config(state='disabled')    #disable the button
        conn.request(method='POST', url=self.path, body=self.params, headers=self.headers)
        response = conn.getresponse()
        self.txtHTML.insert('end', response.getheaders())
        self.txtHTML.insert('end', '\n\n')
        self.txtHTML.tag_add('headers', '1.0', 'current')    #add tag to headers
        html_doc = response.read()
        try:
            encoding = chardet.detect(html_doc)['encoding']
            if not encoding is None:
                html_doc = html_doc.decode(encoding, 'ignore')
        except:
            pass
        self.txtHTML.insert('end', html_doc.replace('\r', ''))
        self.txtHTML.tag_configure('headers', foreground='blue')
        
    except Exception, e:
        self.txtHTML.insert('end', unicode(e))
        self.txtHTML.tag_add("errmsg", '1.0', 'end')
        self.txtHTML.tag_configure('errmsg', foreground='red')
        
    self.cmdPost.config(text='Post', state='normal')
    return


app = PostTool()
app.root.mainloop()
