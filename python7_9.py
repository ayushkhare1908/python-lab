from Tkinter import *
from math import *
root=Tk()
Label(root,text='Simple Interest Calculator!!!',font='Times 45 bold', fg='Black', bg='red').pack()
Label(root,text='Principle  ').pack()
p=Entry(root)
p.pack()
Label(root,text='Rate  ').pack()
r=Entry(root)
r.pack()
Label(root,text='Time  ').pack()
t=Entry(root)
t.pack()
def si():
    s=(int(p.get())*int(r.get())*int(t.get()))/100.0
    Label(root,text=s,font='Times 25 bold', bg='blue').pack()

Button(root,text='SI', bg='orange', command=si).pack()

root.mainloop()
