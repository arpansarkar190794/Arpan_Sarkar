from tkinter import *
gui = Tk()

e1 = Entry(gui)
e2 = Entry(gui)
l = Label(gui)
f = Label(gui)

def callback():
    total = sum(int(e.get()) for e in (e1, e2))
    l.config(text="answer = %s" % total)
b = Button(gui, text="add them", command=callback)    
def sub():
    subt=int(e1.get())-int(e2.get())
    l.config(text="answer = %s" % subt)
c = Button(gui, text="sub them", command=sub)
for widget in (e1, e2, l, b,c):
    widget.pack()
gui.mainloop()
