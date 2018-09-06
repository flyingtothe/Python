'''这是一个过时了的控件，从Tk8.0开始将不再使用这个控件，取而代之的是Menu,这里介绍它是为了
兼容以前版本的Tk，能够知道有这个东东就可以了'''
'''1.介绍一下Menubutton的常用 方法，可以看到与Menu的使用方法基本相同。'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
mbLang = Menubutton(root, text='Language')

mbLang.menu = Menu(mbLang)
# 生成菜单项
for item in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']:
    # add_command：如果是顶层菜单，则从左向右添加，否则就是下拉菜单
    # 参数：
    #   label：定义菜单名称     command：点击后调用的函数
    #   accceletor：快捷键      underline：指定菜单信息是否有下划线
    #   men：指定使用哪一个作为顶级菜单
    mbLang.menu.add_command(label=item)
mbLang['menu'] = mbLang.menu
mbLang.pack(side=LEFT)
# 分隔符将相关的菜单项进行分组，只是UI上的实现，程序上没有任何改变，它也不执行任何的命令

# 添加向菜单中添加checkbutton项
mbOS = Menubutton(root, text='OS')
mbOS.menu = Menu(mbOS)
for item in ['Unix', 'Linux', 'Soloris', 'Windows']:
    mbOS.menu.add_checkbutton(label=item)
mbOS['menu'] = mbOS.menu
mbOS.pack(side=LEFT)

# 向菜单中添加radiobutton项
mbLinux = Menubutton(root, text='Linux')
mbLinux.menu = Menu(mbLinux)
for item in ['Redhat', 'Fedra', 'Suse', 'ubuntu', 'Debian']:
    mbLinux.menu.add_radiobutton(label=item)
mbLinux['menu'] = mbLinux.menu
mbLinux.pack(side=LEFT)

# 对菜单项进行操作
# 向Language菜单中添加一项"Ruby",以分隔符分开
mbLang.menu.add_separator()
mbLang.menu.add_command(label='Ruby')

# 向OS菜单中第二项添加"FreeBSD",以分隔符分开
mbOS.menu.insert_separator(2)
mbOS.menu.insert_checkbutton(3, label='FreeBSD')
mbOS.menu.insert_separator(4)

# 将Linux中的“Debian”删除
mbLinux.menu.delete(5)

root.mainloop()
# 这个控件已经不提倡使用，取而代之的是Menu，使用这个比使用Menubutton更为方便。如果不是特别需要不要使用这个控件。