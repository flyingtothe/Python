'''
# Scale为输出限定范围的数字区间，可以为之指定最大值，最小值及步距值
'''

# _*_coding:utf-8_*_
import tkinter as tk
from tkinter import *

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Scale')
    root.geometry("1800x800+120+100")  # 设置窗口大小  并初始化桌面位置
    root.resizable(width=True, height=True)  # 宽不可变 高可变  默认True

    fram = Frame(root)
    # 创建一个垂直Scale，最大值为100，最小值为0，步距值为1。这个参数设置也就是Scale的缺省设置了
    Scale(fram).pack(side=LEFT)

    # 2、改变这三个参数，生成 一个水平Scale，最小值为－500，最大值为500，步距值为5
    Scale(fram, from_=-500,  # 设置最小值,注意from_的使用方式，在其后添加了"_"，避免与关键字from的冲突
          to=500,  # 设置最大值
          resolution=5,  # 设置步距值
          orient=HORIZONTAL  # 设置水平方向
          ).pack(side=LEFT)

    fram.pack(side=TOP)

    # 3、Scale绑定变量
    fram1 = Frame(root)
    v = StringVar()
    Scale(fram1, from_=-500,
          to=200,
          resolution=1,
          orient=HORIZONTAL,
          variable=v
          ).pack(side=LEFT)  # 绑定变量
    print(v.get())


    # 4、使用回调函数打印当前的值
    # 定义回调函数,这个回调函数有一个参数，这个值是当前的Scale的值，每移动一个步距就会调用一次这个函数，只保证最后一个肯定会调用，
    # 中间的有可能不会调用,通过上例可以看到二者的值是完全一样的
    def callScale(text):
        print('v = ' + v.get())
        print('text = ' + text)


    v = StringVar()
    Scale(fram1, from_=-500,
          to=500.0,
          resolution=0.0001,
          orient=HORIZONTAL,
          variable=v,
          command=callScale  # 设置回调函数
          ).pack(side=LEFT)
    print(v.get())
    fram1.pack(side=TOP)

    # 5、控制显示位数，可以理解为：Scale的值为一整形，在输出显示时，它将会被转化为一字符串，如1.2转化为1.2或1.2000都是可以的
    # 属性digits是控制显示的数字位数,将上面的例子中的数据以8位形式显示，在最后一位会添加一个0
    fram2 = Frame(root)
    Scale(fram2, from_=-500,
          to=500.0,
          resolution=0.0001,
          orient=HORIZONTAL,
          digits=8,  # 设置显示的位数为8,属性digits是控制显示的数字位数,将上面的例子中的数据以8位形式显示，在最后一位会添加一个0
          ).pack(side=LEFT)
    fram2.pack(side=TOP)

    # 6、设置Scale的标签属性label
    # 由label设置的值会显示在水平Scale的上方，用于提示信息
    fram3 = Frame(root)
    Scale(fram3, from_=-500,
          to=500.0,
          resolution=0.0001,
          orient=HORIZONTAL,
          label='Scale',  # 设置标签值
          ).pack(side=LEFT)
    fram3.pack(side=TOP)

    # 7、设置/取得Scale的值
    # slider的位置位于了中间，sl.set(50)起作用了，打印值为50。
    fram4 = Frame(root)
    sl = Scale(fram4)
    sl.set(50)  # 将Scale的值设置为50
    print(sl.get())  # 打印当前的Scale的值
    sl.pack(side=LEFT)
    fram4.pack(side=TOP)

    root.mainloop()