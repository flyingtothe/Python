import tkinter
import tkinter.messagebox

top = tkinter.Tk()

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello Runoob")
# 颜色值必须为英文单词
B = tkinter.Button(top, text ="点我", command = helloCallBack, activebackground='red', activeforeground='yellow', bd=5, bg='green', fg='white',
                   font='gbk')

B.pack()
top.mainloop()
