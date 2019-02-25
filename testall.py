from tkinter import *
gui = Tk()


def allpro():
    e1 = Entry(gui)
    e2 = Entry(gui)
    l =  Label(gui)
    addt = int(e1.get())+int(e2.get())
    l.config(text="answer = %s" % addt)
    b = Button(gui, text="add Them", command= allpro)
    subt = int(e1.get())-int(e2.get())
    l.config(text="answer = %s" % subt)
    b1 = Button(gui, text="sub Them", command=allpro)
    mult = int(e1.get())*int(e2.get())
    l.config(text="answer = %s" % mult)
    b2 = Button(gui, text="mul Them", command=allpro)
    divt = int(e1.get())/int(e2.get())
    l.config(text="answer = %s" % divt)
    b3 = Button(gui, text="Dived Them", command=allpro)
for widget in (e1, e2, l, b,b1,b2,b3):
    widget.pack()
gui.mainloop()
