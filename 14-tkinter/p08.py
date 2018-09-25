'''1.Label的第一个例子
text属性使用方法
'''
# 要使用Tk模块，除非你不想使用这个模块，那整个教程就不需要看了
from tkinter import *
# 初始化Tk
root = Tk()
# 创建一个label，使用编码，到现在为止还没有使用过直接通过“drag-and-drop”就可以完成的IDE。
label = Label(root, text='Hello Tkinter')
# 显示label，给相应组件制定布局，必须含有此语句
label.pack()
# root.pack()
# 但root是不需要（严格地说是必须不这样使用），否则解释器抱怨
# 进入消息循环
root.mainloop()
# 控件的显示步骤：
# 1.创建这个控件
# 2.指定这个空间的master，即这个控件属于哪一个
# 3.告诉GM(geometry manager)有一个控件产生了
'''
还有更简单的一个例子：将‘Hello Tkinter’打印到标题上，Label也不用创建了
from Tkinter import *
root = Tk()
root.title('hello Tkinter')
root.mainloop()
再没法儿简化了，就这样吧
'''
'''2.在label上使用内置位图
bitmap的使用方法
'''
from tkinter import *
# 初始化Tk
root = Tk()
# 创建一个label，使用编码，到现在为止还没有使用过直接通过“drag-and-drop”就可以完成的IDE。
label = Label(root,bitmap = 'error')
# 上面的代码使用了内置位图error

# 显示label，必须含有此语句
label.pack()

# 进入消息循环
root.mainloop()
'''
其他可用的位图：
    * error
    * hourglass
    * info
    * questhead
    * question
    * warning
    * gray12 
    * gray25 
    * gray50
    * gray75
若要查看各自的效果，可以使用相应的名称将bitmpa = 'error'替换。
据说还可以使用自己指定的位图文件,网上找了一下，格式如下：
    Label(root, bitmap="@/path/bitmapname")
不过我试了一下，从来没有成功过，我已经将位图该为单色的了:(

另：还有的网上的文章说明如何使用PhotoImage和BitmapImage显示bmp或gif文件，提到一点
防止图像文件被python自动回收(garbage collected)，应将bmp或gif放到全局(global)或实体
(instance)中，使用如下两种方法，仍未奏效：
'''
# 使用image属性
#    bm = PhotoImage(file = 'c:/python.gif')
#    label = Label(root,image = bm)
#    label.bm = bm
# 错误信息：
# TclError: image "pyimageXX" doesn't exist
# 使用bitmap属性
#    bm = BitmapImage(file='c:/python2.bmp')
#    label = Label(root,bitmap=bm)
#    label.bm = bm
#    label.pack()
# 错误信息：
# TclError: format error in bitmap data
'''
虽然二者均没有起作用，还是要说明一下，bitmap与image的关系，如果同时指定这两参数，image
优先。
'''

'''3.改变控件的前景色和背景色
fg:前景色
bg:背景色
设置背景色的一个大的用处是：可以判断控件的大小（不同的控件使用不同的颜色，后续内容
可以使用此特性来调试container）
'''
from tkinter import *
root = Tk()
#在创建Label时指定各自使用的颜色
'''可以使用的颜色值：'''
#使用颜色名称
Label(root,fg = 'red',bg = 'blue',text = 'Hello I am Tkinter').pack()
#使用颜色值#RRGGBB
Label(root,fg = 'red',bg = '#FF00FF',text = 'Hello I am Tkinter').pack()
#使用系统相关的颜色值（Windows），不建议使用这样的值，不利于平台移植
Label(root,fg = 'red',bg = 'SystemButtonShadow',text = 'Hello I am Tkinter').pack()
root.mainloop()
'''
(1).使用颜色名称
Red
Green
Blue
Yellow
LightBlue
......
(2).使用#RRGGBB
label = Label(root,fg = 'red',bg = '#FF00FF',text = 'Hello I am Tkinter')
指定背景色为绯红色
(3).除此之外，Tk还支持与OS相关的颜色值，如Windows支持
SystemActiveBorder, 
SystemActiveCaption, 
SystemAppWorkspace, 
SystemBackground,
......
'''
'''4.设置宽度与高度
width:    宽度
height:    高度
'''
from tkinter import *
root = Tk()
# 创建三个Label，分别显示red,blue,yellow
# 注意三个Label的大小，它们均与文本的长度有关
Label(root,text = 'red',bg = 'red').pack()
Label(root,text = 'blue',bg = 'blue').pack()
Label(root,text = 'yellow',bg = 'yellow').pack()

# 再创建三个Label，与上次不同的是这三个Label均使用width和heigth属性
# 三个Label的大小由width和height指定
Label(root,bg = 'red',width = 10,height = 3).pack()
Label(root,bg = 'blue',width = 10,height = 3).pack()
Label(root,bg = 'yellow',width = 10,height = 3).pack()
root.mainloop()
'''5.同时使用图像与文本
compound:    指定文本(text)与图像(bitmap/image)是如何在Label上显示，缺省为None，
当指定image/bitmap时，文本(text)将被覆盖，只显示图像了。可以使用的值：
    left：    图像居左
    right:    图像居右
    top：    图像居上
    bottom：图像居下
    center：文字覆盖在图像上
bitmap/image:
    显示在Label上的图像
text:
    显示在Label上的文本
label = Label(root,text = 'Error',compound = 'left',bitmap = 'error')
'''
from tkinter import *
root = Tk()
# 演示compound的使用方法
# 图像与文本在Label中的位置
# 图像居下
Label(root,text = 'botton',compound = 'bottom',bitmap = 'error').pack()
# 图像居上
Label(root,text = 'top',compound = 'top',bitmap = 'error').pack()
# 图像居右
Label(root,text = 'right',compound = 'right',bitmap = 'error').pack()
# 图像居左
Label(root,text = 'left',compound = 'left',bitmap = 'error').pack()
# 文字覆盖在图像上
Label(root,text = 'center',compound = 'center',bitmap = 'error').pack()

# 消息循环
root.mainloop()

'''6.文本的多行显示
在Tk004中，使用width和heigth来指定控件的大小，如果指定的大小无法满足文本的要求是，会出现
什么现象呢？如下代码：
    Label(root,bg = 'welcome to jcodeer.cublog.cn',width = 10,height = 3).pack()
运行程序，超出Label的那部分文本被截断了，常用的方法是：使用自动换行功能，及当文本长度大于
控件的宽度时，文本应该换到下一行显示，Tk不会自动处理，但提供了属性：
wraplength：    指定多少单位后开始换行
justify:        指定多行的对齐方式
ahchor：        指定文本(text)或图像(bitmap/image)在Label中的显示位置
可用的值：
e
w
n
s
ne
se
sw
sn
center
布局如下图

                nw        n        ne
                w      center    e
                sw        s        se
'''
from tkinter import *
root = Tk()
# 左对齐，文本居中
Label(root,text = 'welcome to jcodeer.cublog.cn',bg = 'yellow',width = 40,height = 3,wraplength = 80,justify = 'left').pack()
# 居中对齐，文本居左
Label(root,text = 'welcome to jcodeer.cublog.cn',bg = 'red',width = 40,height = 3,wraplength = 80,anchor = 'w').pack()
# 居中对齐，文本居右
Label(root,text = 'welcome to jcodeer.cublog.cn',bg = 'blue',width = 40,height = 3,wraplength = 80,anchor = 'e').pack()

root.mainloop()

'''
运行一下程序就可以直观的看出，justify与anchor的区别了：一个用于控制多行的对齐；另一个用于
控制整个文本块在Label中的位置
'''