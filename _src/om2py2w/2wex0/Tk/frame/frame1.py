﻿__author__ = 'rbeelive'
# -*- coding: UTF-8 -*-
from Tkinter import *

"""
1 创建容器存放元素
2 创建元素
3 指定容器包含元素
4 设置容器属性
5 界面构建
"""

root = Tk()
root.title('笔记')

# 创建容器
main=Frame()
r=Frame()
but=Frame()

# 创建元素
logo=Label(r,text='Readm')
text=Text(main)
b=Button(but,text='走着')



# 位置
main.grid(row=0, column=0, padx=2, pady=5)
but.grid(row=1, column=0, padx=2, pady=5)
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

root.mainloop()
