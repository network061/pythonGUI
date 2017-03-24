import tkinter as tk
from tkinter import ttk

def clickBtn():
    button.configure(text='change color')
    aLabel.configure(foreground='green')

win = tk.Tk()
win.title("python GUI")

#win.resizable(0,0)
aLabel = ttk.Label(win,text='标签控件')
aLabel.grid(column=0,row=0)
button = ttk.Button(win,text='click me',command=clickBtn)
button.grid(column=1,row=0)
text = tk.StringVar()
textEntered = ttk.Entry(win,width=12,textvariable=text)
textEntered.grid(column=0,row=1)

win.mainloop() # Start GUI

