# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

from damage_calc import damege_calc

root = Tk()
root.title("test app")
res = 0

def damege_calc_call(in_s):
	#global res
	in_d = int(in_s)
	res = damege_calc(in_d)
	result_label.config(text=str(res))

frame_basicdamage = ttk.Frame(root,padding=16)
label_basicdamage = ttk.Label(frame_basicdamage,text="basic damage")
input_basicdamage = StringVar(value="0")
entry_basicdamage = ttk.Entry(frame_basicdamage,textvariable=input_basicdamage)

frame_basicdamage.pack()
label_basicdamage.pack()
entry_basicdamage.pack()

frame_result = ttk.Frame(root,padding=8)
calc_button = ttk.Button(frame_result, text="calc", command=lambda: damege_calc_call(input_basicdamage.get()))
result_label = ttk.Label(frame_result,padding=8,text=str(res))

frame_result.pack()
calc_button.pack(side=LEFT)
result_label.pack(side=LEFT)


root.mainloop()