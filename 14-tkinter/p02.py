# Button功能触发事件
'''1.一个简单的Button应用'''
from tkinter import *

# 定义Button的回调函数
def helloButton():
    print
    'hello button'

root = Tk()
# 通过command属性来指定Button的回调函数
Button(root, text='Hello Button', command=helloButton).pack()
root.mainloop()

'''
执行的结果:每次点击一次，程序向标准输出打印'hello button',以上为Button使用方法，可以
再做一下简化，如不设置Button的回调函数，这样也是允许的但这样的结果与Label没有什么太
大的区别，只是外观看起来有所不同罢了，失去了Button的作用。
from Tkinter import *
root = Tk()
#下面的relief = FLAT设置，就是一个Label了！！！
Button(root,text = 'hello button',relief=FLAT).pack()
root.mainloop()
'''

'''2.测试Button的relief属性'''
# 运行下面的代码可以看到Button的各个不同效果，均没有回调函数。
from tkinter import *

root = Tk()
# flat, groove, raised, ridge, solid, or sunken
Button(root, text='hello button', relief=FLAT).pack()
Button(root, text='hello button', relief=GROOVE).pack()
Button(root, text='hello button', relief=RAISED).pack()
Button(root, text='hello button', relief=RIDGE).pack()
Button(root, text='hello button', relief=SOLID).pack()
Button(root, text='hello button', relief=SUNKEN).pack()

root.mainloop()

'''
Button显示图像
image:可以使用gif图像，图像的加载方法img = PhotoImage(root,file = filepath
bitmap:使用X11 格式的bitmap,Windows的Bitmap没法显示的，在Windows下使用GIMP2.4将windows
Bitmap转换为xbm文件，依旧无法使用.linux下的X11 bitmap编辑器生成的bitmap还没有测试，但可
以使用内置的位图。
(1).使用位图文件
bp = BitmapImage(file = "c:/python2.xbm")
Button(root,bitmap = bp).pack()
(2).使用位图数据
BITMAP = """
#define im_width 32
#define im_height 32
static char im_bits[] = {
0xaf,0x6d,0xeb,0xd6,0x55,0xdb,0xb6,0x2f,
0xaf,0xaa,0x6a,0x6d,0x55,0x7b,0xd7,0x1b,
0xad,0xd6,0xb5,0xae,0xad,0x55,0x6f,0x05,
0xad,0xba,0xab,0xd6,0xaa,0xd5,0x5f,0x93,
0xad,0x76,0x7d,0x67,0x5a,0xd5,0xd7,0xa3,
0xad,0xbd,0xfe,0xea,0x5a,0xab,0x69,0xb3,
0xad,0x55,0xde,0xd8,0x2e,0x2b,0xb5,0x6a,
0x69,0x4b,0x3f,0xb4,0x9e,0x92,0xb5,0xed,
0xd5,0xca,0x9c,0xb4,0x5a,0xa1,0x2a,0x6d,
0xad,0x6c,0x5f,0xda,0x2c,0x91,0xbb,0xf6,
0xad,0xaa,0x96,0xaa,0x5a,0xca,0x9d,0xfe,
0x2c,0xa5,0x2a,0xd3,0x9a,0x8a,0x4f,0xfd,
0x2c,0x25,0x4a,0x6b,0x4d,0x45,0x9f,0xba,
0x1a,0xaa,0x7a,0xb5,0xaa,0x44,0x6b,0x5b,
0x1a,0x55,0xfd,0x5e,0x4e,0xa2,0x6b,0x59,
0x9a,0xa4,0xde,0x4a,0x4a,0xd2,0xf5,0xaa
};
"""
使用tuple数据来创建图像
bmp = BitmapImage(data = BITMAP)
Button(root,bitmap = bmp)
'''

'''3.与Label一样，Button也可以同时显示文本与图像，使用属性compound'''
from tkinter import *

root = Tk()
# 图像居下,居上，居右，居左，文字位于图像之上
Button(root, text='botton', compound='bottom', bitmap='error').pack()
Button(root, text='top', compound='top', bitmap='error').pack()
Button(root, text='right', compound='right', bitmap='error').pack()
Button(root, text='left', compound='left', bitmap='error').pack()
Button(root, text='center', compound='center', bitmap='error').pack()
# 消息循环
root.mainloop()

'''4.控件焦点问题
创建三个Button，各自对应回调函数；将第二个Button设置焦点，程序运行是按“Enter”，判断
程序的打印结果
'''
from tkinter import *

def cb1():
    print
    'button1 clicked'

def cb2(event):
    print
    'button2 clicked'

def cb3():
    print
    'button3 clicked'

root = Tk()

b1 = Button(root, text='Button1', command=cb1)
b2 = Button(root, text='Button2')
b2.bind("<Return>", cb2)
b3 = Button(root, text='Button3', command=cb3)
b1.pack()
b2.pack()
b3.pack()

b2.focus_set()
root.mainloop()
'''
上例中使用了bind方法，它建立事件与回调函数（响应函数）之间的关系，每当产生<Enter>事件
后，程序便自动的调用cb2，与cb1,cb3不同的是，它本身还带有一个参数----event,这个参数传递
响应事件的信息。
'''
from tkinter import *

def printEventInfo(event):
    print
    'event.time = ', event.time
    print
    'event.type = ', event.type
    print
    'event.WidgetId = ', event.widget
    print
    'event.KeySymbol = ', event.keysym


root = Tk()
b = Button(root, text='Infomation')
b.bind("<Return>", printEventInfo)
b.pack()
b.focus_set()
root.mainloop()

'''
犯了个错误，将<Return>写成<Enter>了，结果是：当鼠标进入Button区域后，事件printEventInfo
被调用。程序打印出了event的信息。
'''

'''5.指定Button的宽度与高度
width:    宽度
heigth:    高度
使用三种方式：
1.创建Button对象时，指定宽度与高度
2.使用属性width和height来指定宽度与高度
3.使用configure方法来指定宽度与高度
'''
from tkinter import *
root = Tk()
b1 = Button(root,text = '30X1',width = 30,height = 2)
b1.pack()

b2 = Button(root,text = '30X2')
b2['width'] = 30
b2['height'] = 3
b2.pack()

b3 = Button(root,text = '30X3')
b3.configure(width = 30,height = 3)
b3.pack()

root.mainloop()
# 上述的三种方法同样也适合其他的控件
'''6.设置Button文本在控件上的显示位置
anchor：
使用的值为:n(north),s(south),w(west),e(east)和ne,nw,se,sw，就是地图上的标识位置了，使用
width和height属性是为了显示各个属性的不同。
'''
from tkinter import *
root = Tk()

#简单就是美！
for a in ['n','s','e','w','ne','nw','se','sw']:
    Button(root,
    text = 'anchor',
    anchor = a,
    width = 30,
    height = 4).pack()
#如果看的不习惯，就使用下面的代码。
# Button(root,text = 'anchor',width = 30,height =4).pack()
# Button(root,text = 'anchor',anchor = 'center',width = 30,height =4).pack()
# Button(root,text = 'anchor',anchor = 'n',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 's',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'e',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'w',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'ne',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'nw',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'se',width = 30,height = 4).pack()
# Button(root,text = 'anchor',anchor = 'sw',width = 30,height = 4).pack()

root.mainloop()
'''7.改变Button的前景色与背景色
fg:    前景色
bg：背景色
'''
from tkinter import *
root = Tk()
bfg = Button(root,text = 'change foreground',fg = 'red')
bfg.pack()

bbg = Button(root,text = 'change backgroud',bg = 'blue')
bbg.pack()

root.mainloop()

'''8.设置Button的边框
bd(bordwidth):缺省为1或2个像素
'''
# 创建5个Button边框宽度依次为：0，2，4，6，8
from tkinter import *
root = Tk()
for b in [0,1,2,3,4]:
    Button(root,
    text = str(b),
    bd = b).pack()
root.mainloop()

'''9.设置Button的风格
relief/raised/sunken/groove/ridge
'''
from tkinter import *
root = Tk()
for r in ['raised','sunken','groove','ridge']:
    Button(root,
    text = r,
    relief = r,
    width = 30).pack()
root.mainloop()

'''10.设置Button状态
normal/active/disabled
'''
from tkinter import *
root = Tk()
def statePrint():
    print('state')
for r in ['normal','active','disabled']:
    Button(root,
    text = r,
    state = r,
    width = 30,
    command = statePrint).pack()
root.mainloop()
#例子中将三个Button在回调函数都设置为statePrint,运行程序只有normal和active激活了回调函数，而disable按钮则没有，对于暂时不
#需要按钮起作用时，可以将它的state设置为disabled属性

'''11.绑定Button与变量
设置Button在textvariable属性
'''
from tkinter import *
root = Tk()
def changeText():
    if b['text'] == 'text':
        v.set('change')
        print('change')
    else:
        v.set('text')
        print('text')
v = StringVar()
b = Button(root,textvariable = v,command = changeText)
v.set('text')
b.pack()
root.mainloop()

'''
将变量v与Button绑定，当v值变化时，Button显示的文本也随之变化
'''