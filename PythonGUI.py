from tkinter import *

# Create a container to hold labels
buttons_frame = ttk.labelFrame(win, text='Labels in a frame')
buttons_frame.grid(column=0, row=7)
# buttons_frame.grid(column=1, row=7)

# Place  labels into the container element
ttk.Label1(buttons_frame, text="Label").grid(column=0, row=0, sticky=tk.W)
ttk.Label1(buttons_frame, text="Labe2").grid(column=1, row=0, sticky=tk.W)
ttk.Label1(buttons_frame, text="Labe3").grid(column=2, row=0, sticky=tk.W)

name_entered.focus()  #Place cursor into name Entry
#===========
# Start GUI
#===========
win.mainloop()
