import tkinter as tk
from tkinter import ttk

## webpage Resource: https://www.tutorialspoint.com/python/tk_menu.htm

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

# Add another menu to this menu, this one should have a sub menu
exercise_menu = tk.Menu(menu, tearoff = False)
exercise_menu.add_command(label = 'exercise test 1')
menu.add_cascade(label = 'Exercise', menu = exercise_menu)

exercise_sub_menu = tk.Menu(menu, tearoff = False)
exercise_sub_menu.add_command(label = 'some more stuff')
exercise_menu.add_cascade(label = 'more stuff', menu = exercise_sub_menu)

window.configure(menu = menu)

#menu button
menu_button = ttk.Menubutton(window, text = 'Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label = 'entry 1', command = lambda:print('test 1'))
button_sub_menu.add_checkbutton(label = 'check 1')
menu_button.configure(menu = button_sub_menu)

#run
window.mainloop()