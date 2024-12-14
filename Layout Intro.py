import tkinter as tk
from tkinter import ttk

window_title = 'Layout Intro'
window_geometry = '500x500'

# Window Setup
window = tk.Tk()
window.title(window_title)
window.geometry(window_geometry)

#widgets
label1 = ttk.Label(window, text = 'label1', background = 'red')
label2 = ttk.Label(window, text = 'label2', background = 'blue')

#pack
#label1.pack(side = 'left', expand = True, fill = 'y')
#label2.pack(side = 'right', expand = True, fill = 'both')

#Grid
window.columnconfigure(0,weight = 1)
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 2)
window.rowconfigure(0, weight = 1)

label1.grid(row = 0, column = 1)

# run
window.mainloop()
