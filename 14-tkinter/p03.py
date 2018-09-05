#Checkbutton又称为多选按钮，可以表示两种状态：On和Off，可以设置回调函数，每当点击此按钮时回调函数被调用
'''1.一个简单的Checkbutton例子'''
#创建一个Checkbutton,显示文本为"python"
from tkinter import *
root = Tk()
Checkbutton(root,text = 'python').pack()
root.mainloop()

'''2.设置Checkbutton的回调函数'''
from tkinter import *
def callCheckbutton():
    print ('you check this button')
root = Tk()
Checkbutton(root,text = 'check python',command = callCheckbutton).pack()
root.mainloop()
#不管Checkbutton的状态如何，此回调函数都会被调用

'''3.通过回调函数改变Checkbutton的显示文本text的值'''
from tkinter import *
def callCheckbutton():
    #改变v的值，即改变Checkbutton的显示值
    v.set('check Tkinter')

root = Tk()
v = StringVar()
v.set('check python')
#绑定v到Checkbutton的属性textvariable
Checkbutton(root,text = 'check python',textvariable = v,command = callCheckbutton).pack()

root.mainloop()

'''4.上述的textvariable使用方法与Button的用法完全相同，使用此例是为了区别Checkbutton的另外的一个属性variable,此属性与textvariable不同，它是与这个控件本身绑定，Checkbutton自己有值：On和Off值，缺省状态On为1，Off为0，如：'''
#显示Checkbutton的值
from tkinter import *
root = Tk()
#将一整数与Checkbutton的值绑定，每次点击Checkbutton，将打印出当前的值
v = IntVar()
def callCheckbutton():
    print (v.get())
Checkbutton(root,
            variable = v,
            text = 'checkbutton value',
            command = callCheckbutton).pack()
root.mainloop()

'''5.Checkbutton的值不仅仅是1或0，可以是其他类型的数值，可以通过onvalue和offvalue属性设置Checkbutton的状态值，如下代码将On设置为'python',Off值设置为'Tkinter'，程序的打印值将不再是0或1，而是'Tkinter’或‘python’'''
from tkinter import *
root = Tk()
#将一字符串与Checkbutton的值绑定，每次点击Checkbutton，将打印出当前的值
v = StringVar()
def callCheckbutton():
    print (v.get())
Checkbutton(root,
            variable = v,
            text = 'checkbutton value',
            onvalue = 'python',        #设置On的值
            offvalue = 'tkinter',    #设置Off的值
            command = callCheckbutton).pack()
root.mainloop()

# 6.还有其他的属性fg/bg/relief/width/height/justify/state使用方法与Button相同，不再举例。