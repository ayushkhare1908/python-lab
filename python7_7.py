from Tkinter import *
root=Tk()
root.geometry('100x100')
Label(root,text="WELCOME").pack()
Entry(root).pack()
def fun():
    Label(root,text="GOOD")
Button(root,text="SUBMIT",command=fun).pack()
root.mainloop()
