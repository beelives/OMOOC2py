from Tkinter import *
# -*- coding: UTF-8 -*-
# 问题，按钮不能平排列
#LAb>Frame>Text>but
root = Tk()
root.title("中文")
root.geometry('500x600')


# 创建容器 Frame

frame_top = Frame()

# 创建元素
text_msglist = Text(frame_top)

text_msglist.grid()
frame_top.pack()




"""

Label(root, text='tt', font=('Arial', 20)).pack()
frm = Frame(root)

frm_L = Frame(frm)
t = Text()

t.pack()


Button(root, text="press", command = "").pack()
Button(root, text="pr", command = "").pack()

frm_L.pack()


frm.pack()






frm_L = Frame(frm)
frm_L.pack()
t = Text()

t.pack()

#Label(frm_L, text='厚德', font=('Arial', 15)).pack(side=TOP)
#Label(frm_L, text='博学', font=('Arial', 15)).pack(side=TOP)



"""






root.mainloop()
