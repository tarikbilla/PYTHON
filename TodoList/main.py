# import tkinter and all its functions
from tkinter import *
import tkinter as tk

root = Tk() # create root window
root.title("Basic GUI Layout") # title of the GUI window
root.maxsize(900, 600) # specify the max size the window can expand to
root.config(bg="#fff") # specify background color



# Creating Menubar
menubar = Menu(root) 
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File', command = None) 
file.add_command(label ='Open...', command = None) 
file.add_command(label ='Save', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None) 
edit.add_command(label ='Copy', command = None) 
edit.add_command(label ='Paste', command = None) 
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 
  
# display Menu 
root.config(menu = menubar) 

#End Menu




#Create left and right frames
left_frame = Frame(root, width=200, height=500, bg='#d7d7d7')
left_frame.grid(row=1, column=0, padx=5, pady=2)

left_head = Frame(left_frame, width=180, height=38, bg='#ffffff')
left_head.grid(row=0, column=0, padx=5, pady=2)

left_content = Frame(left_frame, width=180, height=418, bg='#ffffff')
left_content.grid(row=1, column=0, padx=5, pady=2)

left_footer = Frame(left_frame, width=180, height=38, bg='#ffffff')
left_footer.grid(row=2, column=0, padx=5, pady=2)



#Right Side
right_frame = Frame(root, width=650, height=500, bg='#d7d7d7')
right_frame.grid(row=1, column=1, padx=5, pady=2)

right_head = Frame(right_frame, width=600, height=38, bg='#ffffff')
right_head.grid(row=0, column=0, padx=5, pady=2)

right_content = Frame(right_frame, width=600, height=458, bg='#ffffff')
right_content.grid(row=1, column=0, padx=5, pady=2)





root.mainloop()
