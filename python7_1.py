from Tkinter import *
root=Tk()
root.title('My GUI')
Label(root,text="Hello python").pack()
Entry(root).pack()
Button(root,text="OK",command=root.bell).pack()
def info():
    Label(root,text="Hello Python").pack()
root.mainloop()
