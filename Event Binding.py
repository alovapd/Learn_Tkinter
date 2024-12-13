import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# Widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = 'A button')
btn.pack()

# run
window.mainloop()
