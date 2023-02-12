# -*- coding: utf-8 -*-
#!/usr/bin/python3

from Vokabel import Vokabel
import datetime

vk = list()
vk.append(Vokabel("Tisch", "table"))
vk.append(Vokabel("Stuhl", "chair"))
vk.append(Vokabel("Kleiderschrank", "cupboard"))

# Erste Möglichkeit der Auflistung
for vok in vk:
    print(vok.deutsch + ' - ' + vok.fremd)

# Zweite Möglichkeit der Auflistung
for i in range(len(vk)):
    print(vk[i].deutsch + ' - ' + vk[i].fremd)

# Vokabeln abspeichern in einer simplen Textdatei
datei = open('datenbank.txt', 'w')
for vok in vk:
    datei.write(vok.deutsch + ';')
    datei.write(vok.fremd + ';')
    datei.write(str(vok.kategorie) +';')
    datei.write(vok.next_quiz.isoformat() +';')
    datei.write('\n')
datei.close()


# Vokabeln aus der simplen Textdatei laden
vk2 = list()
datei = open('datenbank.txt', 'r')
for zeile in datei:
    temp_list = zeile.split(';')
    vk2.append(Vokabel(temp_list[0], temp_list[1]))
    vk2[-1].katgorie = int(temp_list[2])
    vk2[-1].next_quiz = datetime.date.fromisoformat(temp_list[3])
datei.close()

for vok in vk2:
    print(vok.deutsch + ' - ' + vok.fremd)