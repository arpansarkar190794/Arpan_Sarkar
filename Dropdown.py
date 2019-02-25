from tkinter import *

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

mainloop()
#To get the selected option, use get on the variable:


from tkinter import *

master = Tk()

var = StringVar(master)
var.set("one") # initial value

option = OptionMenu(master, var, "one", "two", "three", "four")
option.pack()

#
# test stuff

def ok():
    print ("value is", var.get())
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()
