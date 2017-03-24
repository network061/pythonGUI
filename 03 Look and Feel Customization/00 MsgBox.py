import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title("python 图形界面")
menuBar = Menu(win)
win.config(menu=menuBar)

def _quit():
    win.quit()
    win.destroy()
    exit()
fileMenu = Menu(menuBar,tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=_quit)
menuBar.add_cascade(label='File',menu=fileMenu)

def _msgBox():
    mBox.showinfo('Serial0/0/0','\nstatus is up\nline protocol is up\nreliability is 255/255')
    
helpMenu = Menu(menuBar,tearoff=0)
helpMenu.add_command(label='About',command=_msgBox)
menuBar.add_cascade(label='Help',menu=helpMenu)

# We are creating a container frame to hold all other widgets
monty = ttk.LabelFrame(win,text=' Monty Python ')
monty.grid(row=0,column=0)

ttk.Label(monty,text='Enter a name:').grid(row=0,column=0)
ttk.Label(monty, text='Choose a number:').grid(row=0, column=1)

text = tk.StringVar()
textarea = ttk.Entry(monty,width=12,textvariable=text)
textarea.grid(row=1,column=0)

number = tk.StringVar()
numberChoosen = ttk.Combobox(monty,width=12,textvariable=number)
numberChoosen['values'] = (1,3,5,7,11,13,17)
numberChoosen.current(0)
numberChoosen.grid(row=1,column=1)

def showText():
    button.configure(text=textarea.get() + ' ' + numberChoosen.get())

button = ttk.Button(monty,text='Click me!',command=showText)
button.grid(row=1,column=2)

# Creating three check buttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty,text='Disabled',variable=chVarDis,state='disabled')
check1.select()
check1.grid(row=2,column=0)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(row=2,column=1)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(row=2,column=2)

ttk.Label(monty,text="Label 1").grid(row=3,column=0)
ttk.Label(monty,text="Label 2").grid(row=3,column=1)
ttk.Label(monty,text="Label 3").grid(row=3,column=2)

textarea.focus()

for child in monty.winfo_children():
    child.grid_configure(padx=8,pady=4)

win.mainloop()
