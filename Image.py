from tkinter import *

gui1 = Tk()

photo = PhotoImage(file="Map.png")
label = Label(gui1, image=photo)
label.pack()

gui1.mainloop()
