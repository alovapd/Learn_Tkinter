import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')
    
def button_func2():
    print('hello')

# Create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# tk text
text = tk.Text(master = window)
text.pack()

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

## ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# Label and button that prints hello. The label should say my label and be between the entry widget and the button
label2 = ttk.Label(master = window, text = 'my label')
label2.pack()


#ex button lambda
#excercise_button = ttk.Button(master = window, text = 'ex_button', command = button_func2)
excercise_button = ttk.Button(master = window, text = 'ex_button', command = lambda:print('hello'))
excercise_button.pack()

#ttk button
button = ttk.Button(master = window, text = "A button", command = button_func)
button.pack()


# run
window.mainloop()
