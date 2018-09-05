# 与Entry类似，但可以指定输入范围值
'''1.创建一个Spinbox'''
from tkinter import *

root = Tk()
Spinbox(root).pack()
'''2.设置Spinbox的最大、最小值和步距值'''
Spinbox(root,
        from_=0,  # 设置最小值
        to=100,  # 设置最大值
        increment=5  # 设置增量值为5，这个与Scale的resolution意思相同
        ).pack()
root.mainloop()
# 只是创建了一个Spinbox，其它的什么也做不了，与Scale不同，Scale使用缺省值就可以控制 值的改变。


'''3.设置Spinbox的值，设置属性values，设置此值后，每次更新值将使用values指定的值，'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
sb = Spinbox(root,
             values=(0, 2, 20, 40, -1),
             increment=2
             )
sb.pack()
# 打印当前的Spinbox的值，为一tuple
print(sb['values'])

# 显示的第一个值为0,up按钮则为2,20,40,-1，不再是增2操作，它会使用tuple的索引递增，至到tuple的最后一个项时，将不再增加；
# down按钮与up按钮恰好相反，它使用tuple的索引递减

'''4.Spinbox绑定变量 '''
v = StringVar()
sb = Spinbox(root,
             values=(0, 2, 20, 40, -1),
             increment=2,
             textvariable=v
             )
v.set(20)
print(v.get())
sb.pack()
# 上面的代码将变量v与sb绑定，并将Spinbox的初始值设置为20，运行程序,Spinbox的值显示为20，再点击up按钮，此时值变为40，
# 即tuple的下一个值，再看下面的代码，与这个不同的是设置的值不包含在tuple之内
v = StringVar()
sb = Spinbox(root,
             values=(0, 2, 20, 40, -1),
             increment=2,
             textvariable=v
             )
v.set(200)
print(v.get())
sb.pack()
# 运行程序，显示的值为200，再次点击up按钮，显示的值为2，即虽然Spinbox能将值显示出来，但并不会将200添加到变量中，此时的
# 索引值依旧为0，因为没有找到200的项。当点击up时，索引值变为1，即显示的值为2。
root.mainloop()

'''5.设置Spinbox的回调函数'''
from tkinter import *

root = Tk()


def printSpin():
    print(sb.get())
    # 使用get()方法来得到当前的显示值


sb = Spinbox(root,
             from_=0,  # 最小值
             to=10,  # 最大值
             command=printSpin  # 回调函数
             )

sb.pack()
root.mainloop()
# 每次点击Spinbox按钮时就会调用printSpin函数，打印出'Spinbox'。与Scale不同的是：它不需要参数。


'''7.删除Spinbox指定位置的字符'''
# delete函数
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()


def printSpin():
    print(sb.get())


sb = Spinbox(root,
             from_=1234,  # 最小值
             to=9999,  # 最大值
             increment=1,
             command=printSpin  # 回调函数
             )
sb.delete(0)
print(sb.get())
sb.pack()
root.mainloop()

'''8.在Spinbox指定位置插入文本'''
# 在每项后面添加.00表示精度，同样使用回调函数实现，代码如下：
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()


def printSpin():
    # 使用get()方法来得到当前的显示值
    sb.insert(END, '.00')
    print(sb.get())


sb = Spinbox(root,
             from_=1234,  # 最小值
             to=9999,  # 最大值
             increment=1,
             command=printSpin  # 回调函数
             )
sb.pack()
root.mainloop()
# 每次点击Spinbox按钮时就会调用printSpin函数，当前的显示值均添加了两个有数字".00"。这个与delete不同，倒是可以正确显示。