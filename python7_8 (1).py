from Tkinter import *
root=Tk()
def fun():
    Button(root,text='OK',bg='orange',command=fun1).pack()
def fun1():
    Label(root,text='Nice Job!!!',font='Times 20 bold', bg='red').pack()

Button(root,text='OK',bg='orange',command=fun).pack()
root.mainloop()
