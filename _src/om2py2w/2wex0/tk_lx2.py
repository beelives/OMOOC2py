# -*- coding: UTF-8 -*-
from Tkinter import *
root = Tk()
mbYes,mbYesNo,mbYesNoCancel,mbYesNoAbort = 0,1,2,4
# 定义一个消息对话框，依据传入的参数不同，弹出不同的提示信息
def MessageBox(): # 没有使用使用参数
    mbType = mbYesNo
    textShow = 'Yes'
    if mbType == mbYes:
         textShow = 'Yes'
    elif mbType == mbYesNo:
         textShow = 'YesNo'
    elif mbType == mbYesNoCancel:
         textShow = 'YesNoCancel'
    elif mbType == mbYesNoAbort:
         textShow = 'YesNoAbort'
         tl = Toplevel(height = 200,width = 400)
         Label(tl,text = textShow).pack()

Button(root,text = 'click me',command = MessageBox).pack()
root.mainloop()