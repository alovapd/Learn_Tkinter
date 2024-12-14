import tkinter as tk
from tkinter import ttk

window_title = 'More on Windows'
window_geometry = '600x400'
##window.iconbitmap('file path or file name')

# Window Setup
window = tk.Tk()
window.title(window_title)
window.geometry(window_geometry)

#Security Event
window.bind('<Escape>', lambda event: window.quit())

#title bar
window.overrideredirect(True) #hiddes the title bar
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

# run
window.mainloop()
