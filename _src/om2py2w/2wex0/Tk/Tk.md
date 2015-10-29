# 什么是 Tkinter

## 背景 
> 开智学习第 2W 其中要求在 1W 的记住上使用 Tkinter 对建议记事本进行迭代更新，在原有功能不变的情况下最终实现简单 GUI 界面的记事本。

----------

## WHAT
### 什么是 Tkinter
Tkinter 模块 ("Tk 接口 ") 是 Python 的标准 Tk GUI 工具包的接口.Tk 和 Tkinter 可以在大多数的 Unix 平台下使用, 同样可以应用在 Windows 和 Macintosh 系统里.,Tk8.0 的后续版本可以实现本地窗口风格, 并良好地运行在绝大多数平台中. 

Tkinter 简称TK接口，是标准的 python GUI 接口，能使跨平台使用

## HOW
### 安装
> python 标准包无需安装，测试是否安装 Tk 命令
`import Tkinter`
OR
`from Tkinter import *`

### 使用
【思考】
GUI 是一种图形化显示，既然是显示那么设计到：
- 容器 	用来存放要显示的内容，也是显示基础
- 控件    包括文本框，按钮，等
- 布局    大小、颜色、位置
【问题】
1 如何显示
2 怎么显示
3 与其相关联的东西有什么

##### 实例
**Hell-word**
```
from Tkinter import *

root = Tk() # 创建容器
w = Label(root, text="Hello, world!") # 设置标签内容
w.pack() # 几何管理器，创建图形
root.mainloop() #进入事件循环，
```

【问题】
现在简单功能基本实现，主要问题是界面的布局和排版
1 使用什么控件进行排版
2 如何实现

## 界面排版
使用 grid 排版


> 搞明白，如何安装、配置、使用，也就是如何去实现，如何去安装，以及如何去使用。



**【错误记录】**
**问题**
get()函数取值出错
`TypeError: get() takes at least 2 arguments (1 given)`
**[方法](http://stackoverflow.com/questions/25010018/type-error-get-takes-at-least-2-arguments-1-given)：**

There is no widget called a "TextBox", so I don't know if you're talking about an Entry widget or a Text widget. The get method of the entry widget can be called without parameters, but the get method of the text widget requires two parameters. The two parameters are the starting and ending points of a region.

To get everything in a text widget, you should do it like this:

self.txtBox.get("1.0", "end-1c")
The "1.0" represents the first character, and "end-1c" represents the last character ("end") minus one character ("-1c") which will ignore the trailing newline that is always added by tkinter itself.

## WHY
> 为什么！通过自问的方式问自己什么要这种去实现，为什么要这种去思考。可横纵对比提出问题

----------

## 体验
通过对TK模块的使用发现，学习这种模块化的东西需要有手册的引导不要，不要盲目。
