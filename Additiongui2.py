from tkinter import *
gui = Tk()
def all():
    e1 = Entry(gui)
    e2 = Entry(gui)
    l = Label(gui)
    b1= Button(gui, text="Subtract Them")
    b2= Button(gui, text="Add Them")
    switcher={0:b1,1:b2}
    if switcher==switcher[0]:
        subt = int(e1.get())-int(e2.get())
        l.config(text="answer = %s" % subt)
    if switcher==switcher[1]:
        subt = int(e1.get())-int(e2.get())
        l.config(text="answer = %s" % subt)
for widget in (e1, e2, l):
    widget.pack()
gui.mainloop()

