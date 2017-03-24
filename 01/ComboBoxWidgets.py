import tkinter as tk
from tkinter import ttk

def showText():
    button.configure(text=textarea.get() + ' ' + numberChoosen.get())

win = tk.Tk()
win.title('Combo Box')

ttk.Label(win,text='Enter a name:').grid(row=0,column=0)
ttk.Label(win,text='Choose a number:').grid(row=0,column=1)

text = tk.StringVar()
textarea = ttk.Entry(win,width=12,textvariable=text)
textarea.grid(row=1,column=0)

number = tk.StringVar()
numberChoosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
numberChoosen['values'] = (1,3,5,7,11,13,17)
numberChoosen.current(0)
numberChoosen.grid(row=1,column=1)

button = ttk.Button(win,text='click me!',command=showText)
button.grid(row=1,column=2)
win.mainloop()