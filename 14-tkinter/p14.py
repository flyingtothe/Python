# Scrollbar（滚动条），可以单独使用，但最多的还是与其它控件（Listbox,Text,Canva等)结合使用
'''1创建一个Scrollbar'''
from tkinter import *

root = Tk()
Scrollbar(root).pack()
# 显示了一个Scrollbar，但什么也做不了，无法拖动slider。

'''2.通过set方法来设置slider的位置'''
# 使用水平滚动条，通过set将值设置为(0.5,1),即slider占整个Srollbar的一半
sl = Scrollbar(root, orient=HORIZONTAL)
sl.set(0.5, 1)
sl.pack()

root.mainloop()

'''3.使用回调函数（不建议这样使用）'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()


def scrollCall(moveto, pos):
    # 如何得到两个参数：使用如下打印中的信息，可以看到解释器传给scrollCall函数的两个参数，一个为
    # moveto,参考手册可以得知，它是当拖动slider时调用的函数；另一个参数为slider的当前位置，我们
    # 可以通过set函数来设置slider的位置，因此使用这个pos就可以完成控制slider的位置。
    # print moveto,pos
    sl.set(pos, 0)
    print(sl.get())


sl = Scrollbar(root, orient=HORIZONTAL, command=scrollCall)
sl.pack()
root.mainloop()
# 这样还有一个严重问题，只能对其进行拖动。对两个按钮及pagedwon/pageup的响应，由于up按钮响应的为三个参数，故会出
# 现异常。这个例子只是用来说明command属性是可用的，如果喜欢自己可以处理所有的消息，将scrollCall是否可以改为变参数函数？
# 对于不同的输入分别进行不同的处理。


'''4.单独使用还是比较少见，大部分应用还是与其它控件的绑定，以下是将一个Listbox与Scrollbar绑定的例子'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
lb = Listbox(root)
sl = Scrollbar(root)
sl.pack(side=RIGHT, fill=Y)
# side指定Scrollbar为居右；fill指定填充满整个剩余区域，到WM在时候再详细介绍这几个属性。
# 下面的这句是关键：指定Listbox的yscrollbar的回调函数为Scrollbar的set
lb['yscrollcommand'] = sl.set
for i in range(100):
    lb.insert(END, str(i))
# side指定Listbox为居左
lb.pack(side=LEFT)
# 下面的这句是关键：指定Scrollbar的command的回调函数是Listbar的yview
sl['command'] = lb.yview
root.mainloop()

'''5.这样理解二者之间的关系：当Listbox改变时，Scrollbar调用set以改变slder的位置；当Scrollbar改变了slider的位置时，Listbox调用yview以显示新的list项,为了演示这两种关系先将yscrollcommad与scrollbar的set解除绑定，看看会有什么效果'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
lb = Listbox(root)
sl = Scrollbar(root)
sl.pack(side=RIGHT, fill=Y)
# 解除Listbox的yscrollcommand与Scrollbar的set绑定
# lb['yscrollcommand'] = sl.set
for i in range(100):
    lb.insert(END, str(i))
# 使用索引为50的元素可见
lb.see(50)
lb.pack(side=LEFT)
sl['command'] = lb.yview
root.mainloop()
# 运行结果，Listbox显示了50项，即Listbox的视图已经到50了，但Scrollbar的slider仍旧位于0处。也就是说Scroolbar没有收到set
# 的命令。即说明解除此绑定，Scrollbar将不再响应Listbox视图改变的消息。但仍可以使用Scrollbar的slider来移动Listbox的视图。


'''6.再测试一下，解除Scrollbar的command与Listbox的yview的关系，测试代码如下：'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
lb = Listbox(root)
sl = Scrollbar(root)
sl.pack(side=RIGHT, fill=Y)
# 下面的这句是关键：指定Listbox的yscrollbar的回调函数为Scrollbar的set
lb['yscrollcommand'] = sl.set
for i in range(100):
    lb.insert(END, str(i * 100))
# 使用索引为50的元素可见
lb.see(50)
lb.pack(side=LEFT)
# 解除Scrollbar的command与Listbox的yview的关系
# sl['command'] = lb.yview
root.mainloop()
# 运行程序，Scrollbar的slider已经到了50位置，也就是说Scrollbar响应了Listbox视图改变的消息，调用 了自己的set函数。
# 进行操作：拖动slder或点击up/down按钮，Listbox的视图没有任何反应，即Listbox不会响应Scrollbar的消息了。