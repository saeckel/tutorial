# -*- coding: utf-8 -*-

import datetime

class Vokabel:
    def __init__(self, de, fr):
        self.deutsch = de
        self.fremd = fr
        self.next_quiz = datetime.date.today()
        self.kategorie = 1
        self.anz_richtig = 0
        self.anz_falsch = 0

    def richtig(self):
        self.anz_richtig = self.anz_richtig + 1
        self.kategorie = self.kategorie + 1
        self.calc_next_quiz_date()

    def falsch(self):
        self.anz_falsch = self.anz_falsch + 1
        self.kategorie = self.kategorie - 1
        self.calc_next_quiz_date()
    
    def calc_next_quiz_date(self):
        # How many days until next quiz? 
        int_next_quiz = 2**(self.kategorie-1)
        # Calc next quiz-date
        datediff = datetime.timedelta(days=int_next_quiz)
        self.nextQuiz = datetime.date.today() + datediff