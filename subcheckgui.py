from tkinter import *
gui = Tk()

e1 = Entry(gui)
e2 = Entry(gui)
l = Label(gui)
def callback():
    sub=e1-e2
    total = sub(int(e.get()) for e in (e1, e2))
    l.config(text="answer = %s" % total)
b = Button(gui, text="add them", command=callback)
for widget in (e1, e2, l, b):
    widget.pack()
b.mainloop()
