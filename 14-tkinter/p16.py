# TopLevel与Frame类似，但它包含窗体属性（如Title）
'''1.创建简单的Toplevel'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
tl = Toplevel()
# 为了区别root和tl，我们向tl中添加了一个Label
Label(tl, text='hello label').pack()
root.mainloop()
# 运行结果生成了两个窗体，一个是root启动的，另一个则是Toplevel创建的，它包含有一个label;
# 关闭tl则没有退出程序，Tk仍旧工作；若关闭Tk，整个Tk结束tl也结束，它不能单独存在。


'''2.设置Toplevel的属性'''
# title设置标题
# geometry设置宽和高
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
tl = Toplevel()
# 设置tl的title
tl.title('hello Toplevel')
# 设置tl在宽和高
tl.geometry('400x300')
# 为了区别root和tl，我们向tl中添加了一个Label
Label(tl, text='hello label').pack()
root.mainloop()

'''3.使用Toplevel自己制作提示框'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
mbYes, mbYesNo, mbYesNoCancel, mbYesNoAbort = 0, 1, 2, 4


# 定义一个消息对话框，依据传入的参数不同，弹出不同的提示信息
def MessageBox():  # 没有使用使用参数
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
    tl = Toplevel(height=200, width=400)
    Label(tl, text=textShow).pack()


# 由Button来启动这个消息框，因为它使用了空的回调函数，故MessageBox改为了无参数形式，使用了固定
# 值mbYesNo
Button(root, text='click me', command=MessageBox).pack()
root.mainloop()