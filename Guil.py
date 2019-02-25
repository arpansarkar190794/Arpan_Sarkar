from tkinter import *
gui = Tk()
def Name():
    guil3 = Label (text='Arpan',fg='red',bg='yellow',font=('arial',24,'italic')).pack()

def Height():
    guil4 = Label (text='5feet5inch',fg='red',bg='yellow',font=('times',24,'bold')).pack()

def weight():
    guil5 = Label (text='63kg',fg='red',bg= 'yellow',font=('times',24,'bold')).pack()
    
gui.title("Arpan Sarkar Button Program")
gui.geometry("500x500+100+100")
guil1 = Label (text='Arpan',fg='red',bg='yellow',font=('times',24,'bold')).pack()
button1 = Button(text='Name',fg='red',bg='yellow',command = Name,font=('times',24,'bold')).pack()
button2 = Button(text='Height',fg='red',bg='yellow',command = Height,font=('times',24,'bold')).pack()
button3 = Button(text='Weight',fg='red',bg='yellow',command = weight,font=('times',24,'bold')).pack()
#Place method places label @ specified place within the window
gui.mainloop()

