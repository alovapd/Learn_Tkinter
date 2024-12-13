import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

#Menu
menu = tk.Menu(window)

#submenu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'New', command = lambda: print('New File'))
file_menu.add_command(label = 'Open', command = lambda: print('Open File'))
#file_menu.add_separator() ##This can add a seperator in the menu if desired.
menu.add_cascade(label = 'File', menu = file_menu)

# Another sub menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Help Entry', command = lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = 'check', onvalue = 'on', offvalue = 'off', variable = help_check_string)

menu.add_cascade(label = 'Help', menu = help_menu)

window.configure(menu = menu)

#run
window.mainloop()