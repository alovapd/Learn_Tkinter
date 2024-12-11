import tkinter as tk
from tkinter import ttk

#Setup 
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

#button
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value = 'a button with string var')
button = ttk.Button(window, text = 'a simple button', command = button_func, textvariable = button_string)
button.pack()

#checkbutton
check_var = tk.IntVar(value = 10)
check1 = ttk.Checkbutton(
    window, 
    text = 'checkbox 1', 
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'Checkbox 2',
    command = lambda: print('test'))
check2.pack()

#radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window, 
    text = 'radiobutton 1', 
    value = 'radio 1', 
    variable = radio_var,
    command = lambda: print(radio_var.get()))    
radio1.pack()

radio2 = ttk.Radiobutton(window, text = 'radiobutton 2', value = 2, variable = radio_var)
radio2.pack()

#run
window.mainloop()