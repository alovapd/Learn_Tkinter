import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')
     
#window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('300x500')

#tkinter Variable
string_var = tk.StringVar()

#widgets
label = ttk.Label(master = window, text = "label", textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

#excerise

excercise_var = tk.StringVar(value = 'test')

entry1 =  ttk.entry(master = window, textvariable = excercise_var)
entry1.pack()
entry2 = ttk.entry(master = window, textvariable = excercise_var)
entry2.pack()
exersize_label = ttk.Label(master = window, textvariable = excercise_var)
exersize_label.pack()

#run
window.mainloop()
