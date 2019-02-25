from tkinter import *
import tkinter.messagebox

gui1 = Tk()

tkinter.messagebox.showinfo('Window Title', 'Hi I am in Messagebox.')
answer = tkinter.messagebox.askquestion('Question 1', 'R U Indian?')

if answer == 'yes':
    print(' 8==D~~ ')

gui1.mainloop()
