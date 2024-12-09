import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()   
   
   # update the label
    #label.configure(text = "Some Other Text") ** older method**
    label['text'] = entry_text
    #entry['state'] = 'disabled'
    #print(label.configure())

#window
window = tk.Tk()
window.title('Getting and Setting Widgets')
window.geometry('800x500')

#widgets
label = ttk.Label(master = window, text = 'Some Text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The Button', command = button_func)
button.pack()

#run
window.mainloop()