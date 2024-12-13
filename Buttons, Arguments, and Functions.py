import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('a button was presed')
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print('a button was pressed')
        print(parameter.get())
    return inner_func 

# Setup
window = tk.Tk()
window.title('buttons, functions and arguments')

# Widgets
entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

button = ttk.Button(window, text = 'button', command = outer_func(entry_string))
button.pack()

# run
window.mainloop()
