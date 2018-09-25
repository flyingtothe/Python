# 创建主窗口
import tkinter as tk

window = tk.Tk()
window.title('弹窗')
window.geometry('200x200')


def hit_me():
    # 创建弹窗
    # 下面有六种类型的弹窗，可以一一分别尝试
    # tk.messagebox.showinfo(title='Hi', message='hahahaha')  # 通知型弹窗
    # tk.messagebox.showwarning(title='Hi', message='nononono')  # 警告型弹窗
    # tk.messagebox.showerror(title='Hi', message='No!! never')  # 报错型弹窗
    # print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))  # 询问型弹窗
    # print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))  # 询问型弹窗
    print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))  # 询问，有三种回答


# 创建按钮，点击该按钮会弹出新窗口
tk.Button(window, text='点击我', command=hit_me).pack()

window.mainloop()





import tkinter.messagebox # 弹窗库

# 1、提示消息框

tkinter.messagebox.showinfo('提示','人生苦短')

# 2、消息警告框

tkinter.messagebox.showwarning('警告','明日有大雨')

# 3、错误消息框

tkinter.messagebox.showerror('错误','出错了')

# 4、对话框

tkinter.messagebox.askokcancel('提示', '要执行此操作吗')#确定/取消，返回值true/false

tkinter.messagebox.askquestion('提示', '要执行此操作吗')#是/否，返回值yes/no

tkinter.messagebox.askyesno('提示', '要执行此操作吗')#是/否，返回值true/false

tkinter.messagebox.askretrycancel('提示', '要执行此操作吗')#重试/取消，返回值true/false

# 5、文件对话框

import tkinter.filedialog
a=tkinter.filedialog.asksaveasfilename()#返回文件名
print(a)
a =tkinter.filedialog.asksaveasfile()#会创建文件
print(a)
a =tkinter.filedialog.askopenfilename()#返回文件名
print(a)
a =tkinter.filedialog.askopenfile()#返回文件流对象
print(a)
a =tkinter.filedialog.askdirectory()#返回目录名
print(a)
a =tkinter.filedialog.askopenfilenames()#可以返回多个文件名
print(a)
a =tkinter.filedialog.askopenfiles()#多个文件流对象
print(a)

