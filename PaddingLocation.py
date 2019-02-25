from tkinter import *

gui = Tk()

w = Label( text="Bangalore", bg="red", fg="white")
w.pack(fill=X)
w = Label( text="Karnataka", bg="green", fg="black")
w.pack(fill=X)


gui.mainloop()



from tkinter import *
root = Tk()
w = Label( text="Bangalore", bg="red", fg="white")
w.pack(fill=X,padx=10)
w = Label( text="Karnataka", bg="green", fg="black")
w.pack(fill=X,padx=10)

mainloop()

from tkinter import *
gui = Tk()
w = Label( text="Bangalore", bg="red", fg="white")
w.pack(fill=X,pady=10)
w = Label( text="Karnataka", bg="green", fg="black")
w.pack(fill=X,pady=10)

mainloop()

from tkinter import *

gui = Tk()

w = Label( text="Bangalore", bg="red", fg="white")
w.pack(padx=5, pady=10, side=LEFT)
w = Label(gui, text="Karnataka", bg="green", fg="black")
w.pack(padx=5, pady=20, side=LEFT)


mainloop()
