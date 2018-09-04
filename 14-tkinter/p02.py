import tkinter
import tkinter.messagebox
#
top = tkinter.Tk()

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello Runoob")
B = tkinter.Button(top, text ="点我", command = helloCallBack, activebackground='red', activeforeground='yellow', bd=5, bg='green', fg='white',
                   font=("Arial", 8), compound='center', height=50, highlightcolor='yellow')

B.pack()
top.mainloop()
