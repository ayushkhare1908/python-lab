from Tkinter import *
from math import *
root=Tk()
Label(root,text='Calculator!!!',font='Times 30 bold', fg='Blue', bg='red').pack()
Label(root,text='Enter first number  ').pack()
n1=Entry(root)
n1.pack()
Label(root,text='Enter second Number  ').pack()
n2=Entry(root)
n2.pack()
def s():
    s=int (n1.get())+int (n2.get())
    Label(root,text=s,font='Times 20 bold', fg='Red', bg='yellow').pack()
def su():
    s=int(n1.get())- int(n2.get())
    Label(root,text=s,font='Times 20 bold', fg='Red', bg='yellow').pack()
def m():
    s=int(n1.get())* int(n2.get())
    Label(root,text=s,font='Times 20 bold', fg='Red', bg='yellow').pack()
def d():
    s=int(n1.get())/ int(n2.get())
    Label(root,text=s,font='Times 20 bold', fg='Red', bg='yellow').pack()
Button(root,text='Sum', bg='orange', command=s).pack()
Button(root,text='Sub', bg='orange', command=su).pack()
Button(root,text='Mul', bg='orange', command=m).pack()
Button(root,text='Div', bg='orange', command=d).pack()
root.mainloop()
