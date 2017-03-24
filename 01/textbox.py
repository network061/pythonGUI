import tkinter as tk
from tkinter import ttk

def clickMe():
    button.configure(text='reliability:'+textEntry.get())

win = tk.Tk()
win.title('gui')

label = ttk.Label(win,text='文本框控件:')
label.grid(column=0,row=0)

button = ttk.Button(win,text='click me',command=clickMe)
button.grid(column=1,row=1)

text_variable = tk.StringVar()
textEntry = ttk.Entry(win,width=12,textvariable=text_variable)
textEntry.grid(row=0,column=1)

win.mainloop()