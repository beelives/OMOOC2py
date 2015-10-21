# 介绍
极简日志记录工具

# 功能
- 记录输入日志
- 每次打开后显示其记录日志


# 截图
![](http://i.imgur.com/UiskKln.jpg)


# 过程记录
 **目标**
完成一个极简交互式日记系统
**要求**

 - 一次接收输入一行日记
 - 保存为本地文件
 - 再次运行系统时,能打印出过往的所有日记
 
## 任务分解
### 思考
#### 需求 1 : 交互输入
 **分析：** 通过终端输入内容，加上逻辑控制实现
 **伪代码**

#### 需求 2： 输入内容存储为本地文件，即 txt 文档
**问题 1  ：** 如何保存
方法 1 :输入一行内容存储一行。（一行，回车符）
方法 2 :全部输入完毕后进行存储
> 问题:如何判断已经全部输入完毕

**问题 2 :** 用什么格式进行存储    
方法 1 ： 在每一行后添加特殊字母来区分如 "-" 或 "#" （将每一行日分割成固定区域）
方法 2 : 在每一条日志后自动换行

#### 需求3 程序运行时可显示过往日志
**问题 3 :** 如何区分每条记录   
方法 1 ： 该方法实现与问题2实现方法相关


### 确定方案
- 运行程序
 - 显示使用信息并接收用户输入
- **写**
 - 读取用户输入一次一行
 - 输入一行写入一行
- **读**
 - 一次读取文件全部内容

### 伪代码
    
    # _*_ coding:utf-8 _*_
    显示使用操作
    str(Input) = raw_input('警告！将初始化日记！是否继续(y/n)？ ')
    if Input == "w":
       pass
    elif Iiput == "r":
       pass
    
    elif Iiput == "e":
       pass

## 第一版 【代码】

```
# _*_ coding:utf-8 _*_

import  sys

def show():
    daily=open('daily.txt' , 'r')
    for line in daily:
        print line
    daily.close()

def run():

    print show()

    print "*"*20

    print "Usage: hammer.py [Auth] [Options] [Targets]\n"
    print "Usage: hammer.py [Auth] [Options] [Targets]\n"


    Input = str(raw_input('>'))


    if Input == "w":
        txt=open('daily.txt' , 'a')
        while True:
            wir = str(raw_input('写入'))
            if wir == "exit":
                sys.exit()
            else:
                txt.write(wir)
                txt.write('\n')

    elif Input == "exit":
        sys.exit()
if __name__ == '__main__':
    run()
```
    
**小结**
问题 ：1 

## 第二版 【代码】

```
__author__ = 'rbeelive'
import  sys
import time


def Get_Time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def show():
    with open('daily.txt','r')as f:
        for line in f.readlines():
            if '#' in line :
                pass
            else:
                print line


def run():


    print show()

    print "*"*20

    print "Usage: hammer.py [Auth] [Options] [Targets]\n"
    print "Usage: hammer.py [Auth] [Options] [Targets]\n"


    Input = str(raw_input('>'))


    if Input == "w":
        txt=open('daily.txt' , 'a')
        while True:
            wir = str(raw_input("www"))
            if wir == "exit":
                sys.exit()
            else:
                txt.write(Get_Time())
                txt.write('\n')
                txt.write(wir)
                txt.write('\n')
                txt.write("#")
                txt.write('\n')
        txt.close()

    elif Input == "exit":
        sys.exit()
if __name__ == '__main__':
    run()
```

**小结**
【增加功能】
- 增加时间输入
- 修改文件读取方式
- 增加储存格式

【问题】
- 重复代码过多
- 现有存储格式若在增加内容不能有效区分关联


## 第三版 【代码】
```
# -*- coding: UTF-8 -*-
__author__ = 'rbeelive'

import  sys
import time


def Get_Time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def show():
    with open('daily.txt','r')as f:
        for line in f.readlines():
            tt=line.split('|')
            strHello = " 您在%s  曰:%s" %(tt[0],tt[1])
            print strHello



def run():


    print show()

    print "*"*10 +"使用帮助"+"*"*10

    print "w: w -> write 写作模式\n"
    print "e: e -> exit 退出写作\n"
    print "n: n -> Null 清空你的秘密 \n"
    print "*"*20

    Input = str(raw_input('>'))


    if Input == "w":
        txt=open('daily.txt' , 'a')
        while True:
            wir = str(raw_input("曰:"))
            if wir == "exit":
                sys.exit()
            else:
                data=Get_Time()+'|'+wir+'\n'
                txt.write(data)

        txt.close()

    elif Input == "e":
        sys.exit()
    elif Input == "n":
        txt=open('daily.txt','w')

if __name__ == '__main__':
    run()
```

   **小结**
【增加功能】
- 优化提示和输出样式
- 重新定义存储格式


【问题】
- 进入到清空模式后直接退出程序
- windows 下中文显示乱码


## 第四版 【代码】
```
# -*- coding: UTF-8 -*-
__author__ = 'rbeelive'


import sys
import time


def Get_Time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def show():
    with open('daily.txt', 'r')as f:
        for line in f.readlines():
            tt = line.split('|')
            str = "%s  :%s" % (tt[0], tt[1])
            print str


def write():
    txt = open('daily.txt', 'a')
    while True:
        wir = str(raw_input("(-_-):"))
        if wir == "exit":
            sys.exit()
        else:
            data = Get_Time() + '|' + wir + '\n'
            txt.write(data)
    txt.close()


def run():
    print show()

    print ("*" * 10 + "使用帮助" + "*" * 10).decode('utf-8')
    print ("w: w -> write 写作模式 (=￣ω￣=)\n").decode('utf-8')
    print ("e: e -> exit 退出创作 ╮(╯▽╰)╭ \n") .decode('utf-8')
    print ("n: n -> Null 清空你的秘密 (＞﹏＜) \n").decode('utf-8')
    print "*" * 20

    Input = str(raw_input(':'))

    if Input == "w":
        write()
    elif Input == "e":
        sys.exit()
    elif Input == "n":
        txt = open('daily.txt', 'w')
        write()


if __name__ == '__main__':
    run()
```
 **小结**
【增加功能】
- 美化显示
- 修复中文乱码
- 添加清空日志后直接跳转到写作模式


## 后续功能
- 私密日志
	- 对存储内容加密
	- 显示私密日志需要密码

- 色彩显示

# 总结
整个学习过程中以项目驱动学习，不是单纯的学习某个知识。


# 发现问题
- 对 Github 使用不够熟练在版本控制等方面做的不是太好
- 任务分解时思路不够清晰
