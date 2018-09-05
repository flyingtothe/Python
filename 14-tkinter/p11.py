# Message也是用来显示文本的，用法与Label基本一样
'''1.创建一个简单的Message'''
from tkinter import *

root = Tk()
# 运行程序，可以看到Hello之后，Message显示在它的下一行，这也是Message的一个特性。Label没有。
Message(root, text='hello Message').pack()

'''2.如果不让它换行的话，指定足够大的宽度'''
Message(root, text='hello Message', width=100).pack()

'''3.使用aspect属性指定宽高比例'''
for i in range(10):
    Message(root, text='A' * i, aspect=400).pack()
root.mainloop()

'''4Message绑定变量'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
v = StringVar()
v.set('000')
for i in range(10):
    Message(root, text='A', textvariable=v).pack()
# 打印当前的v值，只要是其中的一个Message的值发生变化，则此v值就会改变。
# 绑定变量v，虽然创建Message时使用了text来指定Message的值，绑定的变量优先级高，可以改变text指定的值。
print(v.get())

'''5.测试一下justify属性'''
for i in [LEFT, RIGHT, CENTER]:
    Message(root, text='ABC DEF GHI', justify=i).pack()
# 显示的文本自动断行，上下行分别使用了左对齐，右对齐和居中对齐
root.mainloop()
root.mainloop()