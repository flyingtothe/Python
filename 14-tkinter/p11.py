'''1.创建一个简单的Menu'''
# 添加菜单hello和quit，将hello菜单与hello函数绑定；quit菜单与root.quit绑定
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()


def hello():
    print('hello menu')


menubar = Menu(root)
# 创建主菜单，每个菜单对应的回调函数都是hello
for item in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']:
    menubar.add_command(label=item, command=hello)
# 将root的menu属性设置为menubar
root['menu'] = menubar
root.mainloop()
# 这个菜单没有下拉菜单，仅包含两个菜单项


'''2.添加下拉菜单'''
from tkinter import *

root = Tk()


def hello():
    print('hello menu')


menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
for item in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']:
    filemenu.add_command(label=item, command=hello)
# 将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label='Language', menu=filemenu)
root['menu'] = menubar
root.mainloop()

'''3.向菜单中添加Checkbutton项'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()


# 每次打印出各个变量的当前值
def printItem():
    print('Python = ', vPython.get())
    print('PHP = ', vPHP.get())
    print('CPP = ', vCPP.get())
    print('C = ', vC.get())
    print('Java = ', vJava.get())
    print('JavaScript = ', vJavaScript.get())
    print('VBScript = ', vVBScript.get())


menubar = Menu(root)

vPython = StringVar()
vPHP = StringVar()
vCPP = StringVar()
vC = StringVar()
vJava = StringVar()
vJavaScript = StringVar()
vVBScript = StringVar()

filemenu = Menu(menubar, tearoff=0)
for k, v in {'Python': vPython,
             'PHP': vPHP,
             'CPP': vCPP,
             'C': vC,
             'Java': vJava,
             'JavaScript': vJavaScript,
             'VBScript': vVBScript}.items():
    # 绑定变量与回调函数
    filemenu.add_checkbutton(label=k, command=printItem, variable=v)
# 将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label='Language', menu=filemenu)
root['menu'] = menubar
root.mainloop()
# 程序运行，使用了Checkbutton，并通过printItem将每个Checkbutton在当前值打印出来。


'''4.向菜单 中添加Radiobutton项'''
# -*- coding: utf8 -*-
from tkinter import *

root = Tk()

menubar = Menu(root)
vLang = StringVar()


# 每次打印出当前选中的语言
def printItem():
    print('vLang = ', vLang.get())


filemenu = Menu(menubar, tearoff=0)
for k in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']:
    # 绑定变量与回调函数，指定的变量vLang将这几项划为一组
    filemenu.add_radiobutton(label=k, command=printItem, variable=vLang)
# 将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label='Language', menu=filemenu)
root['menu'] = menubar
root.mainloop()
# 程序每次打印出当前选中的语言
# 与Checkbutton不同的是，同一个组内只有一个处于选中状态。


'''5.向菜单中添加分隔符'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
menubar = Menu(root)


# 每次打印出当前选中的语言
def printItem():
    print
    'add_separator'


filemenu = Menu(menubar, tearoff=0)
for k in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']:
    filemenu.add_command(label=k, command=printItem)
    # 将各个菜单项使用分隔符隔开
    filemenu.add_separator()
menubar.add_cascade(label='Language', menu=filemenu)
root['menu'] = menubar
root.mainloop()
# 分隔符将相关的菜单项进行分组，只是UI上的实现，程序上没有任何改变，它也不执行任何的命令


''' 6.将以上的例5中的菜单改为右击弹出菜单'''
# 方法是通过绑定鼠标右键，每当点击时弹出这个菜单，去掉与root的关联
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
menubar = Menu(root)


def printItem():
    print('popup menu')


filemenu = Menu(menubar, tearoff=0)
for k in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']:
    filemenu.add_command(label=k, command=printItem)
    filemenu.add_separator()
menubar.add_cascade(label='Language', menu=filemenu)


# 此时就不要将root的menu设置为menubar了
# root['menu'] = menubar
def popup(event):
    # 显示菜单
    menubar.post(event.x_root, event.y_root)


# 在这里相应鼠标的右键事件，右击时调用popup,此时与菜单绑定的是root，可以设置为其它的控件，在绑定的控件上右击就可以弹出菜单
root.bind('<Button-3>', popup)
root.mainloop()
# 运行测试一个，可以看到各个菜单 项的功能都是可以使用的，所以弹出菜单与一般的菜单功能是一样的，只是弹出的方式不同而已。


''' 7.以下的代码演示了菜单项的操作方法，包括添加各种菜单项，删除一个或多个菜单项'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
menubar = Menu(root)


def printItem():
    print('add_separator')


filemenu = Menu(menubar, tearoff=0)
for k in range(5):
    filemenu.add_command(label=str(k), command=printItem)
menubar.add_cascade(label='Language', menu=filemenu)

'''以下为向菜单中添加项的操作'''
# 在索引1添加一菜单command项
filemenu.insert_command(1, label='1000', command=printItem)
# 在索引2添加一菜单checkbutton项
filemenu.insert_checkbutton(2, label='2000', command=printItem)
# 在索引3添加一菜单radiobutton项
filemenu.insert_radiobutton(3, label='3000', command=printItem)
# 将新添加的菜单项使用分隔符隔开
filemenu.insert_separator(1)
filemenu.insert_separator(5)

'''以下为删除菜单项的操作'''
# 删除索引6-9的菜单项
filemenu.delete(6, 9)
# 删除索引为0的菜单项
filemenu.delete(0)

root['menu'] = menubar
root.mainloop()
# 分隔符将相关的菜单项进行分组，只是UI上的实现，程序上没有任何改变，它也不执行任何的命令