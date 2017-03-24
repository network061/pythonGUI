import tkinter as tk
from tkinter import ttk

def disableBtn():
    button.configure(state='disabled')
def enableBtn():
    button.configure(state='enable')

win = tk.Tk()
win.title("设置焦点 禁用控件")

textarea = tk.StringVar()

label = ttk.Label(win,text = '禁用控件')
label.grid(row=0,column=0)
button = ttk.Button(win,text = 'disable btn',command=disableBtn)
button.grid(row=0,column=1)
button1 = ttk.Button(win,text = 'enable btn',command=enableBtn)
button1.grid(row=0,column=2)

win.mainloop()