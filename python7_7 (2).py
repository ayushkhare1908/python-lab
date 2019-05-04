from Tkinter import *
root=Tk()
Label(root,text="Hello World!!!", font='Times 39 bold',bg='red', fg='green').pack()

def fun():
    Label(root,text= first_name.get()+' '+ 'Welcome!!!\n',font='Impact 19 bold').pack()
Label(root,text='First Name:  ').pack()
first_name=Entry(root)
first_name.pack()
Label(root,text='Surname: ').pack()
sur_name=Entry(root)
sur_name.pack()
Label(root,text=first_name.get()).pack()
Label(root,text=sur_name.get()).pack()
Button(root,text='SUBMIT',bg='blue',command=fun).pack()
root.geometry('600x500')





root.mainloop()
