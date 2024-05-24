"""# Creating button using Tkinter.
# import everything from tkinter module
from tkinter import *
# create a tkinter window
root = Tk()
# Open window having dimension 100x100
root.geometry('100x100')
# Create a Button
btn = Button(root, text = 'Click me !', bd = '5',
                          command = root.destroy)

# Set the position of button on the top of window.
btn.pack(side = 'top')
root.mainloop()"""

"""# Import Module
from tkinter import *
# create root window
root = Tk()
# root window title and dimension
root.title("Welcome ")
# Set geometry (widthxheight)
root.geometry('350x200')
# all widgets will be here
# Execute Tkinter
root.mainloop()"""


"""# -----------Checkbutton Widget------------------
from tkinter import *
root = Tk()
root.geometry("300x200")
w = Label(root, text ='SMEC', font = "50")
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(root, text = "Tutorial",
                      variable = Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button2 = Checkbutton(root, text = "Student",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button3 = Checkbutton(root, text = "Courses",
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button1.pack()
Button2.pack()
Button3.pack()
mainloop()"""


# Combobox Widget in tkinter
# python program demonstrating
# Combobox widget using tkinter
import tkinter as tk
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

# label text for title
ttk.Label(window, text = "GFG Combobox Widget",
          background = 'green', foreground ="white",
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# label
ttk.Label(window, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)

# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
window.mainloop()