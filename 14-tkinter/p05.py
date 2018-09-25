# Listbox为列表框控件，它可以包含一个或多个文本项(text item)，可以设置为单选或多选

'''1.创建一个Listbox，向其中添加三个item'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()

'''2.创建一个可以多选的Listbox,使用属性selectmaod'''
from tkinter import *
root = Tk()
lb = Listbox(root,selectmode = MULTIPLE)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()
# 依次点击这三个item，均显示为选中状态。
# 属性MULTIPLE允许多选，每次点击item，它将改变自己的当前选状态，与Checkbox有点相似

'''3这个属性selectmode还可以设置为BROWSE,可以通过鼠标来移动Listbox中的选中位置（不是移动item），这个属性也是Listbox在默认设置的值，这个程序与1.程序运行的结果的一样的。'''
from tkinter import *
root = Tk()
lb = Listbox(root,selectmode = BROWSE)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()
# 使用鼠标进行拖动，可以看到选中的位置随之变化。
# 与BROWSE相似 的为SINGLE，但不支持鼠标移动选中位置。
from tkinter import *
root = Tk()
lb = Listbox(root,selectmode = BROWSE)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()
# 使用鼠标进行拖动,没有任何变化
'''4.使用selectmode  = EXPANDED使用Listbox来支持Shift和Control。'''
from tkinter import *
root = Tk()
lb = Listbox(root,selectmode = EXTENDED)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()
# 运行程序，点中“python"，shift + 点击"widget"，会选中所有的item
# 运行程序，点中"python"，control + 点击"widget"，会选中python和widget，第二项tkinter处于非选中状态

'''5.向Listbox中添加一个item'''
# 以上的例子均使用了insert来向Listbox中添加 一个item，这个函数有两个属性一个为添加的索引值，另一个为添加的项(item)
#  有两个特殊的值ACTIVE和END，ACTIVE是向当前选中的item前插入一个（即使用当前选中的索引作为插入位置）；END是向
#  Listbox的最后一项添加插入一项
# 先向Listbox中追加三个item，再在Listbox开始添加三项
from tkinter import *
root = Tk()
lb = Listbox(root)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
# 只添加一项将[]作为一个item
# lb.insert(0,['linux','windows','unix'])
# 添加三项，每个string为一个item
lb.insert(0,'linux','windows','unix')
lb.pack()
root.mainloop()
'''6.删除Listbox中的项，使用delete，这个函数也有两个参数，第一个为开始的索引值；第二个为结束的索引值，如果不指定则只删除第一个索引项。'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.delete(1,3)
lb.pack()
root.mainloop()
# 运行程序，只有值0456789,1-3被删除
# 删除全部内容,使用delete指定第一个索引值0和最后一个参数END，即可
# lb.delete(0,END)
'''7.选中操作函数，使用函数实现。selection_set函数有两个参数第一个为开始的索引；第二个为结束的索引，如果不指定则只选中第一个参数指定的索引项'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.selection_set(0,10)
lb.pack()
root.mainloop()
#  程序运行结果，选中了所有的项。 此代码并未指定Listbox为MULTIPLE或EXTENDED，查通过selection_set仍旧可以对Listbox
# 进行操作。

# 与之相对的便是取消选中的函数了，参数与selection_set在参数相同，如下代码取消索引从0－3在状态
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.selection_set(0,10)
lb.selection_clear(0,3)
lb.pack()
root.mainloop()

'''8.得到当前Listbox中的item个数'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.delete(3)
print (lb.size())
lb.pack()
root.mainloop()
# 首先向Listbox中添加 了10个item,然后删除索引为3在item,最后的打印结果为9，即当前的Listbox中只有9项

'''9.返回指定索引的项'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
print (lb.get(3))
lb.pack()
root.mainloop()
# 返回值为300
# get也为两个参数的函数，可以返回多个项(item)，如下返回索引值3－7的值
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
print (lb.get(3,7))
lb.pack()
root.mainloop()
# 返回值为('300', '400', '500', '600', '700')，是一个tuple类型。

'''10.返回当前返回的项的索引，不是item的值'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
lb.selection_set(3,8)
print (lb.curselection())
lb.pack()
root.mainloop()
# 返回值为('3', '4', '5', '6', '7', '8')，而不是('300','400','500','600','700','800')，哑然无法直接得到各项的值，知道了索引，得到值
# 就很容易了:lb.get()就可以实现。

'''11.判断 一个项是否被选中，使用索引。'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
lb.selection_set(3,8)
print (lb.selection_includes(8))
print (lb.selection_includes(0))

lb.pack()
root.mainloop()
# 返回结果：True Flase，即8包含在选中的索引中，0不包含在选中的索引中

'''12.Listbox与变量绑定'''
# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
v = StringVar()
lb = Listbox(root,listvariable = v)
for i in range(10):
    lb.insert(END,str(i*100))
# 打印当前列表中的项值
print (v.get())
# 输出：('0', '100', '200', '300', '400', '500', '600', '700', '800', '900')
# 改变v的值,使用tuple可以与item对应
v.set(('1000','200'))
# 结果只有两项了1000和200
lb.pack()
root.mainloop()

'''13.Listbox与事件绑定'''
#  它不支持command属性来设置回调函数了，使用bind来指定回调函数,打印当前选中的值
# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
def printList(event):
    print (lb.get(lb.curselection()))
lb = Listbox(root)
lb.bind('<Double-Button-1>',printList)
for i in range(10):
    lb.insert(END,str(i*100))
lb.pack()
root.mainloop()

# 还有一个比较实用的功能没有介绍：滚动条的添加，留到后面介绍Scrollbar的时候再一并介绍