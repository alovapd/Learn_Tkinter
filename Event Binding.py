import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print('Return Key Pressed')

# Window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# Widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = tk.Button(window, text = 'A button')
button.pack()

# Events
window.bind('<Return>', return_pressed)

# run
window.mainloop()
