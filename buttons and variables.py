import tkinter as tk
from tkinter import ttk

#Setup 
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

#button
def button_func():
    print('a basic button')

button_string = tk.StringVar(value = 'a button with string var')
button = ttk.Button(window, text = 'a simple button', command = button_func, textvariable = button_string)
button.pack()

#checkbutton
check_var = tk.IntVar(value = 10)
check = ttk.Checkbutton(
    window, 
    text = 'checkbox 1', 
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check.pack()

#radio buttons
radio1 = ttk.Radiobutton(window, text = 'radio button 1', value = 'radio 1')
radio1.pack()
radio2 = ttk.Radiobutton(window, text = 'radio button 2', value = 2)
radio2.pack()

#run
window.mainloop()