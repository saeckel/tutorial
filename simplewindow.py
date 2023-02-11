# -*- coding: utf-8 -*-
#!/usr/bin/python3

import tkinter as tk

window = tk.Tk()
frm_deutsch = tk.Frame(
    relief=tk.RIDGE,
    borderwidth=1,
)
frm_englisch = tk.Frame(
    relief=tk.RIDGE,
    borderwidth=1,
)

lbl_englisch = tk.Label(
    master=frmEnglisch,
    text="Englisch",
#    fg="white",
#    bg="black",
#    width=10,
#    height=10,
) # generating a new label

lbl_deutsch = tk.Label(
    master=frmDeutsch,
    text="Deutsch",
)

btn_button = tk.Button(
    text="Programm beenden",
#    width=25,
    height=2,
#    bg="blue",
#    fg="yellow"
)

ent_englisch = tk.Entry(
    master=frmEnglisch,
#    fg="yellow", 
#    bg="white", 
    width=50)
ent_deutsch = tk.Entry(
    master=frmDeutsch,
    width=50,
)



# the pack() command without master=
lbl_englisch.pack(side=tk.LEFT)
ent_englisch.pack()
lbl_deutsch.pack(side=tk.LEFT)
ent_deutsch.pack()
#lblHello.pack() # positioning the label in the window - which window?

frm_englisch.pack()
frm_deutsch.pack()

window.mainloop() # starting the eventloop

