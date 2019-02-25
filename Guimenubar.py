from tkinter import *

gui = Tk()


gui.title("Aliyas Shaik Widow1")
gui.geometry("500x500+100+50")


menu1 = Menu()
listone = Menu()
listone.add_command(label='New File')
listone.add_command(label='Open File')
listone.add_command(label='Save File')

listtwo = Menu()
listtwo.add_command(label='Copy')
listtwo.add_command(label='Past')
listtwo.add_command(label='Undo')

menu1.add_cascade(label="File", menu=listone)
menu1.add_cascade(label="Edit", menu=listtwo)
menu1.add_cascade(label="Help")

gui.config(menu=menu1)

gui.mainloop()
