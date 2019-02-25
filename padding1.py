from tkinter import *
gui = Tk()
btn_column = Button(text="I'm in column 3")
btn_column.grid(column=3)

btn_columnspan = Button(text="I have a columnspan of 3")
btn_columnspan.grid(columnspan=4)

btn_ipadx = Button(text="ipadx of 4")
btn_ipadx.grid(ipadx=4)

btn_ipady = Button(text="ipady of 4")
btn_ipady.grid(ipady=4)

btn_padx = Button(text="padx of 4")
btn_padx.grid(padx=4)

btn_pady = Button(text="pady of 4")
btn_pady.grid(pady=4)

btn_row = Button(text="I'm in row 2")
btn_row.grid(row=2)

btn_rowspan = Button(text="Rowspan of 2")
btn_rowspan.grid(rowspan=2)

btn_sticky = Button(text="north")
btn_sticky1 = Button(text="West")
btn_sticky.grid(sticky=NE)
btn_sticky1.grid(sticky=SW)

gui.mainloop()
