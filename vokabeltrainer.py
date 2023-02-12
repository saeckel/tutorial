# -*- coding: utf-8 -*-
#!/usr/bin/python3

import tkinter as tk
import datetime
from datetime import date as dt

class Vokabel:
    def __init__(self, de, fr):
        self.deutsch = de
        self.fremd = fr
        self.nextQuiz = datetime.date.today()
        self.kategorie = 1
        self.anz_richtig = 0
        self.anz_falsch = 0

    def richtig(self):
        self.anz_richtig = self.anz_richtig + 1
        self.kategorie = self.kategorie + 1
        # How many days until next quiz? 
        int_next_quiz = 2**(self.kategorie-1)
        # Calc next quiz-date
        datediff = datetime.timedelta(days=int_next_quiz)
        self.nextQuiz = self.today() + datediff



window = tk.Tk()
frm_deutsch = tk.Frame(
    relief=tk.RIDGE,
    borderwidth=1,
    padx=5,
    pady=5,
)
frm_englisch = tk.Frame(
    relief=tk.RIDGE,
    borderwidth=1,
    padx=5,
    pady=5,
)

lbl_englisch = tk.Label(
    master=frm_englisch,
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
    text="Check answer",
#    width=25,
    height=2,
#    bg="blue",
#    fg="yellow"
)

lbl_result = tk.Label(
    font=("Arial", 25)
)

ent_englisch = tk.Entry(
    master=frm_englisch,
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
lbl_englisch.pack(side=tk.LEFT)
ent_englisch.pack()
lbl_deutsch.pack(side=tk.LEFT)
ent_deutsch.pack()
frm_englisch.pack()
frm_deutsch.pack()
btn_check.pack()
lbl_result.pack()

ent_englisch.delete(0,tk.END)           # delete everything
ent_englisch.insert(0, 'table')       
ent_englisch.config(state=tk.DISABLED)  # Disable English label

def spellcheck(event):
    answer = ent_deutsch.get() # ent_deutsch auslesen
    if answer == 'Tisch':
        lbl_result.config(text='Great! That was right!')
    else:
        lbl_result.config(text='Oh no, that was wrong!')
btn_check.bind("<Button-1>", spellcheck)


window.mainloop() # starting the eventloop

