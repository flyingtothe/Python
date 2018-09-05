#Entry用来输入单行文本
'''1.第一个Entry程序'''
from tkinter import *
root = Tk()
Entry(root,text = 'input your text here').pack()
root.mainloop()
#上面的代码目的是创建一个Entry对象，并在Entry上显示'input your text here',运行此代码，并没有看到文本的显示，由此可知与Lable和Button不同，Entry的text属性不可以设置Entry的文本

'''2.在Entry中设定初始值，使用textvariable将变量与Entry绑定'''
from tkinter import *
root = Tk()
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('input your text here')
entry.pack()
root.mainloop()

#上面的例子中将变量e与Entry绑定，然后将e的值设置为'input your text here'，程序运行时的初始值便设置了。

'''3.设置为只读Entry.
Entry的另一个比较有用的属性，设置为只读，不允许用户对它的值改变。
设置state属性为'readonly'
'''
from tkinter import *
root = Tk()
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('input your text here')
entry.pack()
entry['state'] = 'readonly'
root.mainloop()

#实际上Entry的属性值可以使用的也为normal/active/disabled,'readonly'与disabled一样

'''4.设置为密码输入框
#将Entry作为一个密码输入框来使用，即不显示用户输入的内容值，用特定符号代替。使用用属性
show来指定。
'''
from tkinter import *
root = Tk()
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('input your text here')
entry.pack()
#使用*来显示输入的内容，如果喜欢可以改为其它字符
entry['show'] = '*'
#分别使用*#$显示输入的文本内容
for mask in ['*','#','$']:
    e = StringVar()
    entry = Entry(root,textvariable = e)
    e.set('password')
    entry.pack()
    entry['show'] = mask

root.mainloop()

'''5.验证输入的内容是否符合要求。
使用validate来校验输入的内容
使用validate方法来限制输入的内容
这是一个有问题的例子，无法调用validateText回调函数
‘'''
from tkinter import *
root = Tk()
e = StringVar()
def validateText(contents):
    print (contents)
    return contents.isalnum()

entry = Entry(root,validate = 'key',textvariable = e,validatecommand = validateText)
entry.pack()

root.mainloop()
'''
文档中说明使用validate来接受的事件，使用validatecommand来确定输入的内容是否合法，但
如何传入参数？没找到相应的说明
'''
# 还有其他的属性fg/bg/relief/width/height/justify/state使用方法与Button相同，不再举例