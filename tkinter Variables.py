import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')
     
#window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('300x500')

#tkinter VCAriable
string_var = tk.StringVar()

#lWidgets
label = ttk.Label(master = window, text = "label", textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

#run
window.mainloop()
