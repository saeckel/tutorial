# -*- coding: utf-8 -*-
#!/usr/bin/python3

import tkinter as tk
import Vokabel

window = tk.Tk()
frm_deutsch = tk.Frame(
    relief=tk.RIDGE,
    borderwidth=1,
    padx=5,
    pady=5,
)
frm_fremd = tk.Frame(
    relief=tk.RIDGE,
    borderwidth=1,
    padx=5,
    pady=5,
)
frm_buttons = tk.Frame(
    relief=tk.RIDGE,
    borderwidth=1,
    padx=5,
    pady=5,    
)

lbl_fremd = tk.Label(
    master=frm_fremd,
    text="Englisch: ",
#    fg="white",
#    bg="black",
#    width=10,
#    height=10,
) # generating a new label

lbl_deutsch = tk.Label(
    master=frm_deutsch,
    text="Deutsch: ",
)

btn_check = tk.Button(
    master = frm_buttons,
    text="Check answer",
#    width=25,
    height=2,
#    bg="blue",
#    fg="yellow"
)
btn_load = tk.Button(
    master=frm_buttons,
    text="Laden",
    height=2,
)
btn_save = tk.Button(
    master=frm_buttons,
    text="Speichern",
    height=2,
)

lbl_result = tk.Label(
    font=("Arial", 25)
)

ent_fremd = tk.Entry(
    master=frm_fremd,
    disabledforeground='black',
#    state=tk.DISABLED,
#    fg="yellow", 
#    bg="white", 
    width=50)
ent_deutsch = tk.Entry(
    master=frm_deutsch,
    width=50,
)

# Building the window
lbl_fremd.pack(side=tk.LEFT)
ent_fremd.pack()
lbl_deutsch.pack(side=tk.LEFT)
ent_deutsch.pack()
frm_fremd.pack()
frm_deutsch.pack()
lbl_result.pack()
btn_load.pack(side=tk.LEFT)
btn_check.pack(side=tk.LEFT)
btn_save.pack(side=tk.LEFT)
frm_buttons.pack()


ent_fremd.delete(0,tk.END)           # delete everything
ent_fremd.insert(0, 'table')       
ent_fremd.config(state=tk.DISABLED)  # Disable English label

def spellcheck(event):
    answer = ent_deutsch.get() # ent_deutsch auslesen
    if answer == 'Tisch':
        lbl_result.config(text='Great! That was right!')
    else:
        lbl_result.config(text='Oh no, that was wrong!')
btn_check.bind("<Button-1>", spellcheck)


window.mainloop() # starting the eventloop

