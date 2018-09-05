'''1.创建第一个Text'''
from tkinter import *

root = Tk()
t = Text(root)
'''2.向Text中添加文本'''
# 向第一行,第一列添加文本0123456789
t.insert(1.0, '0123456789')
# 向第一行第一列添加文本ABCDEFGHIJ
t.insert(1.0, 'ABCDEFGHIJ')
t.pack()
root.mainloop()
# root中含有一Text控件,可以在这个控件内输入文本,可以使用Ctrl+C/V向Text内添加剪切板上的内容(文本),不接受Ctrl+Z执行操作


'''3.使用line.col索引添加内容'''
# 使用indexes来添加Text的内容
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
t = Text(root)
# 向第一行,第一列添加文本0123456789
t.insert(1.0, '0123456789')
t.insert(1.0, ' ')
# 向第一行第一列添加文本ABCDEFGHIJ
t.insert(1.0, 'ABCDEFGHIJ')
t.pack()
root.mainloop()
# 可以看到使用indexes时，如果其值超过了Text的buffer值，程序不会抛出异常，它会使用向给定值靠近。


'''mark是用来表示在Text中位置的一类符号'''
'''4.使用内置的mark控制添加位置'''
# 演示了内置的mark:INSERT/CURRENT/END/SEL_FIRST/SEL_LAST的用法
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
t = Text(root)
# 向Text中添加10行文本
for i in range(1, 10):
    t.insert(1.0, '0123456789 ')


# 定义各个Button的回调函数，这些函数使用了内置的mark:INSERT/CURRENT/END/SEL_FIRST/SEL_LAST
def insertText():
    t.insert(INSERT, 'jcodeer')


def currentText():
    t.insert(CURRENT, 'jcodeer')


def endText():
    t.insert(END, 'jcodeer')


def selFirstText():
    t.insert(SEL_FIRST, 'jcodeer')


def selLastText():
    t.insert(SEL_LAST, 'jcodeer')


# INSERT
Button(root,
       text='insert jcodeer at INSERT',
       command=insertText
       ).pack(fill=X)
# CURRENT
Button(root,
       text='insert jcodeer at CURRENT',
       command=insertText
       ).pack(fill=X)
# END
Button(root,
       text='insert jcodeer at END',
       command=endText
       ).pack(fill=X)
# SEL_FIRST
Button(root,
       text='insert jcodeer at SEL_FIRST',
       command=selFirstText
       ).pack(fill=X)
# SEL_LAST
Button(root,
       text='insert jcodeer at SEL_LAST',
       command=selLastText
       ).pack(fill=X)

t.pack()
root.mainloop()
# 几个内置的mark：
# INSERT:光标的插入点
# CURRENT:鼠标的当前位置所对应的字符位置
# END:这个Text buffer的最后一个字符
# SEL_FIRST:选中文本域的第一个字符，如果没有选中区域则会引发异常
# SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发 异常


'''5.使用表达式来增强mark'''
# 表达式(expression)可以个性任何的Indexes，如下：
'''
+ count chars :前移count字符
- count chars :后移count字符
+ count lines :前移count行
- count lines :后移count行
linestart:移动到行的开始
linesend:移动到行的结束
wordstart:移动到字的开始
wordend:移动到字的结束
'''
# 演示修饰符表达式的使用方法，如何与当前可用的indexes一起使用
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
t = Text()
# 向第一行,第一列添加文本0123456789
for i in range(1, 10):
    t.insert(1.0, '0123456789 ')
a = 'test_mark'


def forwardChars():
    # 直接连接字符串
    # t.mark_set(a,CURRENT + '+ 5 chars')
    t.mark_set(a, CURRENT + '+5c')


def backwardChars():
    # t.mark_set(a,CURRENT + '- 5 chars')
    t.mark_set(a, CURRENT + '-5c')


def forwardLines():
    # t.mark_set(a,CURRENT + '+ 5 lines)
    t.mark_set(a, CURRENT + '+5l')


def backwardLines():
    # t.mark_set(a,CURRENT + '- 5 lines)
    t.mark_set(a, CURRENT + '-5l')


def lineStart():
    # 注意linestart前面的那个空格不可省略
    t.mark_set(a, CURRENT + ' linestart')


def lineEnd():
    # 注意lineend前面的那个空格不可省略
    t.mark_set(a, CURRENT + ' lineend')


def wordStart():
    # 移动到当前字的开始。
    t.mark_set(a, CURRENT + ' wordstart')


def wordend():
    # 移动到当前字的结束
    t.mark_set(a, CURRENT + ' wordend')


# mark:test_mark默认值为CURRENT
t.mark_set(a, CURRENT)
Button(root, text='forward 5 chars', command=forwardChars).pack(fill=X)
Button(root, text='backward 5 chars', command=backwardChars).pack(fill=X)
Button(root, text='forward 5 lines', command=forwardLines).pack(fill=X)
Button(root, text='backward 5 lines', command=backwardLines).pack(fill=X)
Button(root, text='line start', command=lineStart).pack(fill=X)
Button(root, text='line end', command=lineEnd).pack(fill=X)
Button(root, text='word start', command=lineEnd).pack(fill=X)
Button(root, text='word end', command=lineEnd).pack(fill=X)


# 测试三个位置的不同，CURRENT可以得知是当前光标的位置；mark就表示mark的位置了,INSERT好像一植都在1.0处没有改变。
def insertText():
    t.insert(INSERT, 'insert')


def currentText():
    t.insert(CURRENT, 'current')


def markText():
    t.insert(a, 'mark')


Button(root, text='insert jcodeer.cublog.cn', command=insertText).pack(fill=X)
Button(root, text='current jcodeer.cublog.cn', command=currentText).pack(fill=X)
Button(root, text='mark jcodeer.cublog.cn', command=markText).pack(fill=X)
t.pack()
root.mainloop()

'''Tkinter教程之Text(2)篇'''
'''6.使用tag来指定文本的属性'''
# 创建一个指定背景颜色的TAG
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
t = Text(root)
# 创建一个TAG，其前景色为红色
t.tag_config('a', foreground='red')
# 使用TAG 'a'来指定文本属性
t.insert(1.0, '0123456789', 'a')
t.pack()
root.mainloop()
# 结果是文本颜色改变为红色了


'''7.同时使用两个文本指定同一个属性'''
# 没有特别设置的话，最后创建的那个会覆盖掉其它所有的设置
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
t = Text(root)
# 创建一个TAG，其前景色为红色
t.tag_config('a', foreground='red')
t.tag_config('b', foreground='blue')
# 使用TAG 'a'来指定文本属性
t.insert(1.0, '0123456789', ('b', 'a'))
t.pack()
root.mainloop()
# 结果是文本的颜色不是按照insert给定的顺序来设置，而是按照tag的创建顺序来设置的。


'''8.控制tag的级别'''
# 使用tag_lower/tag_raise来降低或提高tag的级别
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
t = Text(root)
# 创建一个TAG，其前景色为红色
t.tag_config('a', foreground='red')
t.tag_config('b', foreground='blue')
# 使用tag_lower来降低a的级别
t.tag_lower('a')
# 使用TAG 'a'来指定文本属性
t.insert(1.0, '0123456789', ('b', 'a'))
t.pack()
root.mainloop()
# 结果：文本内容颜色变为了蓝色，蓝色的作用级别大于红色了，即使是先创建了蓝色。


'''9.对文本块添加tag'''
# tag_add方法的使用
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
t = Text(root)
# 创建一个TAG，其前景色为蓝色
t.tag_config('b', foreground='blue')
for i in range(10):
    t.insert(1.0, '0123456789\n')
t.tag_add('b', '2.5', '2.end')
t.pack()
root.mainloop()
# 先向Text中添加了10行文本，创建一tag，将第2行第6列至第二行行尾使用使用此tag

'''10.使用自定义mark对文本块添加tag'''
# -*- coding: utf-8 -*-
# tag_add方法的使用
from tkinter import *

root = Tk()
t = Text(root)
# 创建一个TAG，其前景色为蓝色
t.tag_config('b', foreground='blue')
for i in range(10):
    t.insert(1.0, '0123456789\n')
# 自定义两个mark，并使用它们来指定添加tag的文本块
t.mark_set('ab', '3.1')
t.mark_set('cd', END)
t.tag_add('b', 'ab', 'cd')

t.pack()
root.mainloop()
# 先向Text中添加了10行文本，创建两个mark('ab'和'cd')，将使用这两个tag指定文本的文本块使用此tag


'''11.使用indexes获得Text中的内容'''
# -*- coding: utf-8 -*-
# 分别使用内置的indexes和自定义mark来获取文本
# get方法的使用
from tkinter import *

root = Tk()
t = Text(root)
for i in range(10):
    t.insert(1.0, str(i) + ' 0123456789\n')
# 获得1.0-2.3的文本
print(t.get('1.0', '2.3'))
# 自定义两个mark，并使用它们来获得文本块
t.mark_set('ab', '3.1')
t.mark_set('cd', END)
print(t.get('ab', 'cd'))
t.pack()
root.mainloop()

'''12.测试delete对tag的影响'''
# -*- coding: utf-8 -*-
# delete方法不会对tag造成影响，也就是说删除文本与tag没有任何关系
from tkinter import *

root = Tk()
t = Text(root)
# 创建一个TAG，其前景色为蓝色
t.tag_config('b', foreground='blue')
for i in range(10):
    t.insert(1.0, str(i) + ' 0123456789\n')
# 自定义两个mark，并使用它们来指定添加tag的文本块
t.mark_set('ab', '3.1')
t.mark_set('cd', END)
t.tag_add('b', 'ab', 'cd')
# 删除(1.0 - 4.0)的文本
t.delete('1.0', '4.0')
t.pack()
root.mainloop()
# (1.0-4.0)的文本全部初始删除了，剩余的文本全部以蓝色显示，即还保留tag的属性


'''13.使用tag_delete对文本属性的影响'''
# -*- coding: utf-8 -*-
# 使用tag_delete方法操作tag
from tkinter import *

root = Tk()
t = Text(root)
# 创建一个TAG，其前景色为蓝色
t.tag_config('b', foreground='blue')
for i in range(10):
    t.insert(1.0, str(i) + ' 0123456789\n')
# 自定义两个mark，并使用它们来指定添加tag的文本块
t.mark_set('ab', '3.1')
t.mark_set('cd', END)
t.tag_add('b', 'ab', 'cd')
# 删除tag 'b'，注意这个操作是在tag_add之后进行的。
t.tag_delete('b')
t.pack()
root.mainloop()
# 结果所有的文本没有了tag('b')属性，即tag_delete会清除所有与此tag相关的属性，不论是之前还是之后


'''Tkinter教程之Text篇(3)'''
'''14.自定义tag的两个内置属性'''''
# tag.first:tag之前插入文本，此文本不包含在这个tag中
# tag.last:tag之后插入文本，此文本包含在这个tag中
# -*- coding: utf-8 -*-
# 使用tag的内置属性来插入文本
from tkinter import *

root = Tk()
t = Text(root)
# 创建一个TAG，其前景色为蓝色
t.tag_config('b', foreground='blue')
for i in range(10):
    t.insert(1.0, str(i) + ' 0123456789\n')
# 自定义两个mark，并使用它们来指定添加tag的文本块
t.mark_set('ab', '3.1')
t.mark_set('cd', END)
t.tag_add('b', 'ab', 'cd')
# 删除tag 'b'，注意这个操作是在tag_add之后进行的。
# 在tag('b')之前插入'first'
t.insert('b.first', 'first')
# 在tag('b')之后插入'last'
t.insert('b.last', 'last')
t.pack()
root.mainloop()
# 注意：first没有使用tag('b')属性，last使用了tag('b')属性


'''15.在Text中创建按钮'''
# -*- coding: utf-8 -*-
# 使用window_create在Text内创建一widget
from tkinter import *

root = Tk()
t = Text(root)
for i in range(10):
    t.insert(1.0, '0123456789 ')


def printText():
    print('buttin in text')


bt = Button(t, text='button', command=printText)
# 在Text内创建一个按钮
t.window_create('2.0', window=bt)
# 没有调用pack()
# bt.pack()
t.pack()
root.mainloop()
# 注意：使用window_create，而不是使用insert('2.0',bt);pack()也不用调用;
# 点击这个按钮，打印出'button in text'，证明这个按钮是可以正常工作的。


'''16.在Text中创建一个图像(未实现)'''
# -*- coding: utf-8 -*-
# 使用window_create在Text内创建一widget
from tkinter import *

root = Tk()
t = Text(root)
for i in range(10):
    t.insert(1.0, '0123456789\n')
# 分别使用BitmapImage和PhotoImage进行测试，均没有显示出图像？？？
# bm = BitmapImage('gray75')
bm = PhotoImage('d:/1.png')
# 在Text内创建一个图像
t.image_create('2.0', image=bm)
print(t.image_names())
# 打印的图像名称都是正确的
t.pack()
root.mainloop()
# 按照手册中的说明未实现这种效果，原因不知。


'''17.绑定tag与事件'''
# -*- coding: utf-8 -*-
# 使用tag_bind方法
from tkinter import *

root = Tk()
t = Text(root)
for i in range(10):
    t.insert(1.0, '0123456789\n')
# 创建一个tag
t.tag_config('a', foreground='blue', underline=1)


# Enter的回调函数
def enterTag(event):
    print('Enter event')


# 绑定tag('a')与事件('<Enter>')
t.tag_bind('a', '<Enter>', enterTag)
t.insert(2.0, 'Enter event ', 'a')
t.pack()
root.mainloop()
# 注意：使用tag_bind绑定tag与事件，当此事件在tag上发生时便就会调用这个tag的回调函数
# 因为使用了Enter事件，此事件含有一个参数，故将enterTag加了一个参数，程序中不使用此参数


'''18.使用edit_xxx实现编辑常用功能(未实现)'''
# -*- coding: utf-8 -*-
# 使用edit_xxx函数实现编辑常用功能
from tkinter import *

root = Tk()
t = Text(root)
for i in range(10):
    t.insert(1.0, '0123456789\n')
t.pack()


# 定义回调函数
# 撤消回调函数
def undoText():
    t.edit_undo()


# 插入文本函数
def insertText():
    t.insert(1.0, 'insert text')


Button(root, text='undo', command=undoText).pack(fill=X)
Button(root, text='insert text', command=insertText).pack(fill=X)

root.mainloop()
# 这个edit_undo方法也是不起作用，不知为何？？？