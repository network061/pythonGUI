import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("路由广域网端口状态")

tabControl = ttk.Notebook(win)
tab_gs = ttk.Frame(tabControl) # 广深通道
tabControl.add(tab_gs,text='广坪线')
tabControl.pack(expand=1,fill="both")

tab_gp = ttk.Frame(tabControl) # 广深通道
tabControl.add(tab_gp,text='广深线')
tabControl.pack(expand=1,fill="both")

monty_station1 =  ttk.LabelFrame(tab_gs,text='广州站')
monty_station1.grid(row=0,column=0,padx=8,pady=4)
ttk.Label(monty_station1,text='Serial0/0').grid(row=0,column=0,sticky='w')
ttk.Label(monty_station1,text='Serial0/1').grid(row=0,column=1,sticky='w')
ttk.Label(monty_station1,text='255/255').grid(row=1,column=0,sticky='w')
ttk.Label(monty_station1,text='255/255').grid(row=1,column=1,sticky='w')

win.mainloop()