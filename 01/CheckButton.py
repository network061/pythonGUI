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

# Creating three check buttons
chVarDis = tk.IntVar()
check1 =tk.Checkbutton(win,text='Disabled',variable=chVarDis,state='disabled')
check1.select()
check1.grid(row=2,column=0)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(row=2,column=1)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(row=2,column=2)

# Create a container to hold labels
labelsFrame =ttk.LabelFrame(win,text=' Labels in a Frame ')
labelsFrame.grid(row=5,column=0)
# Place labels into the container element
ttk.Label(labelsFrame,text="Label 1").grid(row=0,column=0)
ttk.Label(labelsFrame,text="Label 2").grid(row=0,column=1)
ttk.Label(labelsFrame,text="Label 3").grid(row=0,column=2)
# Place cursor into name Entry
textarea.focus()
win.mainloop()