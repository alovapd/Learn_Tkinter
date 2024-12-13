import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('a button was presed')
    print(entry_string.get())

# Setup
window = tk.Tk()
window.title('buttons, functions and arguments')

# Widgets
entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

button = ttk.Button(window, text = 'button', command = lambda: button_func(entry_string))
button.pack()

# run
window.mainloop()
