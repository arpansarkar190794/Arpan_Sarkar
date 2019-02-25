from tkinter import *

gui = Tk()


gui.title("Notepad")
gui.geometry("500x500+100+50")


menu1 = Menu()
listone = Menu()
listone.add_command(label='New')
listone.add_command(label='Open...')
listone.add_command(label='Save')
listone.add_command(label='Save As...')
listone.add_command(label='Page Setup...')
listone.add_command(label='Print')

listtwo = Menu()
listtwo.add_command(label='Undo')
listtwo.add_command(label='Cut')
listtwo.add_command(label='Copy')
listtwo.add_command(label='Paste')
listtwo.add_command(label='Delete')
listtwo.add_command(label='Find...')
listtwo.add_command(label='Find Next')
listtwo.add_command(label='Replace...')
listtwo.add_command(label='Go To...')
listtwo.add_command(label='Select All')
listtwo.add_command(label='Time/Date')

listthree = Menu()
listthree.add_command(label='Word Wrap')
listthree.add_command(label='Font')

listfour = Menu()
listfour.add_command(label='Status Bar')

listfive = Menu()
listfive.add_command(label='View Help')
listfive.add_command(label='About Notepad')


menu1.add_cascade(label="File", menu=listone)
menu1.add_cascade(label="Edit", menu=listtwo)
menu1.add_cascade(label="Format", menu=listthree)
menu1.add_cascade(label="View", menu=listfour)
menu1.add_cascade(label="Help",menu=listfive)

gui.config(menu=menu1)

gui.mainloop()
