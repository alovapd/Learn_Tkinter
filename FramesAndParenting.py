import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Frames and Paretning')

# frame
frame = ttk.Frame(window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack()

# master setting
label = ttk.Label(frame, text = 'label in frame')
label.pack()

button = ttk.Button(frame, text = 'button in a frame')
button.pack()

#example
label2 = ttk.Label(window, text = 'LAbel outside frame')
label2.pack()

#rum
window.mainloop()