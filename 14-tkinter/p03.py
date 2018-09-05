# 提供可以用来进行绘图的Container，支持基本的几何元素，使用Canvas进行绘图时，所有的操作都是通过Canvas，不是通过它的元素
# 元素的表示可以使用handle或tag。
'''1.第一个Canvas程序'''
# -*- coding: cp936 -*-
# 指定画布的颜色为白色
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
cv.pack()
root.mainloop()
# 为明显起见，将背景色设置为白色，用以区别root

'''2.创建一个item'''
# -*- coding: cp936 -*-
# 创建一个矩形，指定画布的颜色为白色
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 创建一个矩形，坐标为(10,10,110,110)
cv.create_rectangle(10,10,110,110)
cv.pack()
root.mainloop()
# 为明显起见，将背景色设置为白色，用以区别root
'''3.指定item的填充色'''
# -*- coding: cp936 -*-
# 创建一个矩形，指定画布的背景色为白色
# 使用属性fill设置它的填充颜色
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
cv.create_rectangle(10,10,110,110,fill = 'red')
cv.pack()
root.mainloop()
# 指定矩形的填充色为红色
'''4.指定item的边框颜色'''
# -*- coding: cp936 -*-
# 创建一个矩形，指定画布的背景色为白色
# 使用属性outline设置它的边框颜色
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
cv.create_rectangle(10,10,110,110,outline = 'red')
cv.pack()
root.mainloop()
# 指定矩形的边框颜色为红色
'''5.指定边框的宽度'''
# -*- coding: cp936 -*-
# 指定画布的背景色为白色
# 使用属性width指定线的宽度
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
cv.create_rectangle(10,10,110,110,outline = 'red',width = 5)
cv.pack()
root.mainloop()
# 指定矩形的边框颜色为红色，设置线宽为5，注意与Canvas的width是不同的。
'''6.画虚线'''
# -*- coding: cp936 -*-
# 指定画布的背景色为白色
# 使用属性dash,这个值只能为奇数
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
cv.create_rectangle(10,10,110,110,
                    outline = 'red',
                    dash = 10,
                    fill = 'green')
cv.pack()
root.mainloop()
# 指定矩形的边框颜色为红色,画虚线
'''7.使用画刷填充'''
# -*- coding: cp936 -*-
# 指定画布的背景色为白色
# 使用属性stipple
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
cv.create_rectangle(10,10,110,110,
                    outline = 'red',
                    stipple = 'gray12',
                    fill = 'green')
cv.pack()
root.mainloop()
# 指定矩形的边框颜色为红色,自定义画刷
'''8.修改item的坐标'''
# -*- coding: cp936 -*-
# 指定画布的背景色为白色
# 使用Canvas的方法来重新设置item的坐标
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
rt = cv.create_rectangle(10,10,110,110,
                    outline = 'red',
                    stipple = 'gray12',
                    fill = 'green')
cv.pack()
# 重新设置rt的坐标（相当于移动一个item）
cv.coords(rt,(40,40,80,80))
root.mainloop()
# 动态修改item的坐标

'''9.创建item的tags'''
# -*- coding: cp936 -*-
# 使用属性tags设置item的tag
# 使用Canvas的方法gettags获取指定item的tags
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 使用tags指定一个tag('r1')
rt = cv.create_rectangle(10,10,110,110,
                         tags = 'r1'
                         )
cv.pack()

print(cv.gettags(rt))
# 使用tags属性指定多个tags,即重新设置tags的属性
cv.itemconfig(rt,tags = ('r2','r3','r4'))
print(cv.gettags(rt))
root.mainloop()
# 动态修改item的坐标
'''10.多个item使用同一个tag'''
# -*- coding: cp936 -*-
# 多个控件使用同一个tag
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 使用tags指定一个tag('r1')
rt = cv.create_rectangle(10,10,110,110,
                         tags = ('r1','r2','r3')
                         )
cv.pack()

cv.create_rectangle(20,20,80,80,tags = 'r3')
print (cv.find_withtag('r3'))
root.mainloop()
# 动态修改item的坐标
#fid_withtag返回所有与tag绑定的item。
'''11.通过tag来访问item'''
# -*- coding: cp936 -*-
# 得到了tag值也就得到了这个item，可以对这个item进行相关的设置。
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 使用tags指定一个tag('r1')
rt = cv.create_rectangle(10,10,110,110,
                         tags = ('r1','r2','r3')
                         )
cv.pack()

cv.create_rectangle(20,20,80,80,tags = 'r3')
# 将所有与tag('r3')绑定的item边框颜色设置为蓝色
for item in cv.find_withtag('r3'):
    cv.itemconfig(item,outline = 'blue')
root.mainloop()
# 动态修改与tag('r3')绑定的item边框颜色
'''13.向其它item添加tag'''
# -*- coding: cp936 -*-
# 使用addtag_来向上一个或下一个item添加tag
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 创建三个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    tags = ('r1','r2','r3'))
rt2 = cv.create_rectangle(
    20,20,80,80,
    tags = ('s1','s2','s3'))
rt3 = cv.create_rectangle(
    30,30,70,70,
    tags = ('y1','y2','y3'))
# 向rt2的上一个item添加r4
cv.addtag_above('r4',rt2)
# 向rt2的下一个item添加r5
cv.addtag_below('r5',rt2)

for item in [rt1,rt2,rt3]:
    print (cv.gettags(item))

cv.pack()
root.mainloop()
#Canvas使用了stack的技术，新创建的item总是位于前一个创建的item之上，故调用above时，它会查找rt2上面的item为rt3,故rt3中添加了tag('r4')，同样add_below会查找下面的item。
'''14.返回其它item'''
# -*- coding: cp936 -*-
# 使用find_xxx查找上一个或下一个item
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 创建三个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    tags = ('r1','r2','r3'))
rt2 = cv.create_rectangle(
    20,20,80,80,
    tags = ('s1','s2','s3'))
rt3 = cv.create_rectangle(
    30,30,70,70,
    tags = ('y1','y2','y3'))
# 查找rt2的上一个item,并将其边框颜色设置为红色
cv.itemconfig(cv.find_above(rt2),outline = 'red')
# 查找rt2的下一个item,并将其边框颜色设置为绿色
cv.itemconfig(cv.find_below(rt2),outline = 'green')

cv.pack()
root.mainloop()
# Canvas使用了stack的技术，新创建的item总是位于前一个创建的item之上，故调用above时，它会查找rt2上面的item为rt3,故rt3中边框颜色设置为红色，同样add_below会查找下面的item。

'''16.移动item'''
# -*- coding: cp936 -*-
# move指定x,y在偏移量
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 创建两个同样的rectangle，比较移动前后的不同
rt1 = cv.create_rectangle(
    10,10,110,110,
    tags = ('r1','r2','r3'))
cv.create_rectangle(
    10,10,110,110,
    tags = ('r1','r2','r3'))
# 移动rt1
cv.move(rt1,20,-10)
cv.pack()
root.mainloop()
# move可以指定x,y在相对偏移量，可以为负值
'''17.删除item'''
# -*- coding: cp936 -*-
# delete删除给定的item
from tkinter import *
root = Tk()
cv = Canvas(root,bg = 'white')
# 创建两个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    tags = ('r1','r2','r3'))
r2 = cv.create_rectangle(
    20,20,110,110,
    tags = ('s1','s2','s3'))
# 使用id删除rt1
cv.delete(rt1)
# 使用tag删除r2
cv.delete('s1')

cv.pack()
root.mainloop()
# 两种方法删除item(id/tag)
'''18.缩放item'''
# -*- coding: cp936 -*-
# scale缩放item,计算公式:(coords - offset)*scale + offset
from tkinter import *
root = Tk()
cv = Canvas(root,bg = 'white')
# 创建两个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    tags = ('r1','r2','r3'))
# 将y坐标放大为原来的2位，x坐标值不变
cv.scale(rt1,0,0,1,2)
cv.pack()
root.mainloop()
# scale的参数为(self,xoffset,yoffset,xscale,yscale)
'''19.绑定item与event'''
# -*- coding: cp936 -*-
# 使用tag_bind来绑定item与事件
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 创建三个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    width = 8,
    tags = ('r1','r2','r3'))
def printRect(event):
    print('rectangle')
# 绑定item与事件
cv.tag_bind('r1','<Button-1>',printRect)
cv.pack()
root.mainloop()
# 只有点击到矩形的边框时才会触发事件
'''20.添加绑定事件'''
# -*- coding: cp936 -*-
# 使用tag_bind来绑定item与事件，与参考上测试结果不一致。
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 创建三个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    width = 8,
    tags = ('r1','r2','r3'))
def printRect(event):
    print( 'rectangle')
def printLine(event):
    print ( 'line')
# 绑定item与左键事件
cv.tag_bind('r1','<Button-1>',printRect)
# 绑定item与右键事件
cv.tag_bind('r1','<Button-3>',printLine)
cv.pack()
root.mainloop()
# 只有点击到矩形的边框时才会触发事件,不使用add参数，默认就是向这个item添加一个处理函数，它不会替换原来的事件函数，例子结果：既响应左键又响应右键
'''21.绑定新的item与现有的tags'''
# -*- coding: cp936 -*-
# 使用tag_bind来绑定item与事件，测试结果与参考上的说法不一致
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'white')
# 创建三个rectangle
rt1 = cv.create_rectangle(
    10,10,110,110,
    width = 8,
    tags = ('r1','r2','r3'))
def printRect(event):
    print ('rectangle')
def printLine(event):
    print ('line')
# 绑定item与左键事件
cv.tag_bind('r1','<Button-1>',printRect)
# 绑定item与右键事件
cv.tag_bind('r1','<Button-3>',printLine)
# 创建一个line，并将其tags设置为'r1'
cv.create_line(10,200,100,200,width = 5,tags = 'r1')
cv.pack()
root.mainloop()
# 将事件与tag('r1')绑定后，创建新的item并指定已绑定事件的tag,新创建的item同样也与事件绑定，这个与参考上的说法也不一致