

from tkinter import *

gui = Tk()

w = Label( text="Red Sun", bg="red", fg="white")
w.pack(fill=X)
w = Label( text="Green Grass", bg="green", fg="black")
w.pack(fill=X)
w = Label( text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X)

gui.mainloop()



from tkinter import *
root = Tk()
w = Label( text="Red Sun", bg="red", fg="white")
w.pack(fill=X,padx=10)
w = Label( text="Green Grass", bg="green", fg="black")
w.pack(fill=X,padx=10)
w = Label( text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X,padx=10)
mainloop()

from tkinter import *
gui = Tk()
w = Label( text="Red Sun", bg="red", fg="white")
w.pack(fill=X,pady=10)
w = Label( text="Green Grass", bg="green", fg="black")
w.pack(fill=X,pady=10)
w = Label( text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X,pady=10)
mainloop()

from tkinter import *

gui = Tk()

w = Label( text="red", bg="red", fg="white")
w.pack(padx=5, pady=10, side=LEFT)
w = Label(gui, text="green", bg="green", fg="black")
w.pack(padx=5, pady=20, side=LEFT)
w = Label(gui, text="blue", bg="blue", fg="white")
w.pack(padx=5, pady=20, side=LEFT)

mainloop()
