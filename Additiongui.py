from tkinter import *
gui = Tk()
def add():
    a=10
    b=20
    c=a+b
    guil3 = Label (text=c,fg='red',bg='yellow',font=('arial',24,'italic')).pack()

def Multiplication():
    a=10
    b=20
    e=a*b
    guil4 = Label (text=e,fg='red',bg='yellow',font=('times',24,'bold')).pack()
def Subtraction():
    a=10
    b=20
    d=b-a
    
    guil5 = Label (text=d,fg='red',bg='yellow',font=('times',24,'bold')).pack()
    
gui.title("Aliyas Shaik Button Program")
gui.geometry("500x500+100+100")
#guil1 = Label (text='',fg='red',bg='yellow',font=('times',24,'bold')).pack()
button1 = Button(text='Addition of two no. is',fg='red',bg='yellow',command = add,font=('times',24,'bold')).pack()
button2 = Button(text='Multiplication of a and b is',fg='red',bg='yellow',command = Multiplication,font=('times',24,'bold')).pack()
button3 = Button(text='Subtraction of a and b is',fg='red',bg='yellow',command = Subtraction,font=('times',24,'bold')).pack()
#Place method places label @ specified place within the window
gui.mainloop()


