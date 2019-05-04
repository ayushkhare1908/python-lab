from Tkinter import *
from tkMessageBox import *
root=Tk()
Label(root,text='click on button below').pack()
def fun():
    showinfo('hi','GoodMorning')
    showerror('error','something Wrong')
    askyesno('response','Do you agree')
    askyesnocancel('response','Do you agree')
Button(root,text='click',command=fun).pack()
mainloop()    
