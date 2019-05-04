from Tkinter import *
root=Tk()
Label(root,text='welcome').pack()
root.title("GUI")
Entry(root).pack()
def fun():
    Label(root,text="good afternoon")
    Button(root,text="ok",command=fun).pack()
    name=Entry(root)
    name.pack()
 
    root.geometry('300x300')
    
root.mainloop()
