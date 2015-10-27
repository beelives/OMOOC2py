__author__ = 'rbeelive'
# -*- coding: UTF-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
改用Class实现
"""
from Tkinter import *


class PostToolGUI():
    def __init__(self):
        self.root = root = Tk()
        root.withdraw()    #hide window
        root.title('Tk Post Tool') # 标题内容
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight() - 100    #a taskbar may lie under the screen
        root.resizable(False,False)

        from ImageTk import PhotoImage
        icon = PhotoImage(file='icon.gif')
        root.tk.call('wm', 'iconphoto', root._w, icon)



        Label(root, text='(→_→)').grid(row=2, column=0, sticky=NW, padx=10, pady=10)
        data_bar = Scrollbar()

        self.txtData = txtData = Text(root, bg='#FAEBD7', yscrollcommand=data_bar.set)
        txtData.grid(row=2, column=1, sticky=W, pady=15)
        txtData.config(width=60, height=30)
        data_bar.grid(row=2, column=2, sticky=NS, pady=15)
        txtData.focus_set()
        #data_bar.config(command=txtData.yview)


        self.cmdPost = cmdPost = Button(root, text='GO', bg='#FFDEAD', width=15, command=lambda: self.cmd_click(self))
        cmdPost.grid(row=3, column=1, sticky=NW)

        self.cmdShow = cmdShow = Button(root, text='(--------------)', bg='#FFDEAD', width=2, command=lambda: self.cmd_show(self))
        cmdShow.grid(row=3, column=2,)



        root.update_idletasks()
        root.deiconify()    #calculate window size
        root.withdraw()     #hide it
        #put it on screen center
        root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height(),
                                       (screen_width - root.winfo_width())/2, (screen_height - root.winfo_height())/2) )
        root.deiconify()

    def cmd_click(self, event):
        pass

    def cmd_show(self, event):
        pass
        #print "sdfsdfsdfsdf"


if __name__ == '__main__':
    testapp = PostToolGUI()
    testapp.root.mainloop()