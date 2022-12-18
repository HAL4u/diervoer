# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:38:06 2022
@author: HAL
"""


import os
from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_b


root = tk.Tk()
root.attributes('-fullscreen', False)
root.title("Voer calculator van hal.berkers@gmail.com.")


save_pad = "c:/users/public/diervoer/"
file_ = "_diervoer_" + str(date.today()) + ".csv"


def f_error(v_):                                    # v_ = Fn_ = foutnummer als getal
    """ error messages """
    if v_ == 1:
        m_b.showinfo("Fout", "geef een naam")
    if v_ == 2:
        m_b.showinfo("Fout", "waarde tussen 0 en 5000 invoeren")
    if v_ == 3:
        m_b.showinfo("Fout", "waarde tussen 0 en 100 invoeren")
    if v_ == 4:
        m_b.showinfo("Fout", "verkeerde invoer")


info_tekst = ("-----------------------------------------------------------\n" +
              "Lees op de verpakking van het droogvoer hoeveel procent\n" +
              "droge voedingstoffen het heeft.\n" +
              "Vermenigvuldig dit percentage met het gewicht (in gram)\n" +
              "droogvoer dat de hond dagelijks krijgt.\n" +
              "Doe dit ook voor het natvoer.\n" +
              "Tel beide gewichten (nat en droog) op, dit is het\n" +
              "totale gewicht droge voedingsstoffen per dag in gram.\n" +
              "Met dit programma kun je berekenen hoeveel nat en droogvoer\n" +
              "per dag de hond kan hebben.\n" +
              "Weeg de hond maandelijks en kijk of de totale hoeveelheid\n" +
              "droge voedingsstoffen minder moet.\n" +
              "-----------------------------------------------------------\n")


def f_input_test(h, c, n, d):                       # Ip_1, Ip_2, Ip_3, Ip_4
    """ input test """
    Fn_ = 0                                         # foutnummer
    ib = 0                                          # locale teller
    global H_                                       # naam dier
    global C_                                       # de voedingsconstante, gram droge bestandelen
    global Vn_                                      # gram droge voedingsdelen in natvoer
    global Vd_                                      # gram droge voedingsdelen in droogvoer

    try:
        ib = 1
        if h == "":                                 # test naam
            Fn_ = 1
            inputbox_1.focus()
            raise TypeError
        else:
            H_ = h

        ib = 2
        if int(c) <= 0 or int(c) > 5000:            # test C_
            Fn_ = 2
            inputbox_2.focus()
            raise TypeError
        else:
            C_ = int(c)

        ib = 3
        if int(n) < 0 or int(n) > 100:              # test Vn_
            Fn_ = 3
            inputbox_3.focus()
            raise TypeError
        else:
            Vn_ = int(n)

        ib = 4
        if int(d) <= 0 or int(d) > 100:             # test Vd_
            Fn_ = 3
            inputbox_4.focus()
            raise TypeError
        else:
            Vd_ = int(d)

    except ValueError:                              # verkeerde type invoer
        if ib == 1:
            inputbox_1.focus()
        if ib == 2:
            inputbox_2.focus()
        if ib == 3:
            inputbox_3.focus()
        if ib == 4:
            inputbox_4.focus()
        f_error(4)
    except TypeError:                               # test niet geslaagd
        f_error(Fn_)


def f_berekening(h, c, n, d):                       # H_, C_, Vn_, Vd_
    """ calculation """
    Nmax_ = 0                                       # maximale gewicht natvoer in gram
    Dmax_ = 0                                       # maximale gewicht droogvoer in gram
    # van procenten naar factor
    Nmax_ = int(c / (n / 100))
    Dmax_ = int(c / (d / 100))
    # afronden op tientallen
    Dmax_ = 10 * round(Dmax_ / 10)
    Nmax_ = 10 * round(Nmax_ / 10)

    # tekst samenstellen
    TB.delete("1.0", "end")
    TB.insert("end", "       " + h + "\n")
    TB.insert("end", "       -----------------------------------------" + "\n")
    TB.insert("end", "       Dagratsoen droge bestanddelen (gram): " + str(c) + "\n")
    TB.insert("end", "       Maximaal dagratsoen droogvoer (gram): " + str(Dmax_) + "\n")
    TB.insert("end", "       Maximaal dagratsoen natvoer (gram):   " + str(Nmax_) + "\n\n")
    TB.insert("end", "                    droog     nat\n")
    TB.insert("end", "                    =============\n")

    # waarden berekenen
    for i_ in range(11):
        # bepaal de stapgrootte
        stap_ = Dmax_ - (i_ * int(round(Dmax_ / 10)))
        nat_ = Nmax_ - (stap_*(Nmax_/Dmax_))
        nat_ = int(round(nat_))
        # afronden op tientallen
        stap_ = 10 * round(stap_ / 10)
        nat_ = 10 * round(nat_ / 10)
        # uitvoer centreren
        droog_ = str(stap_)
        while len(droog_) < 25:
            droog_ = " " + droog_
        # uitvoer
        TB.insert("end", droog_ + " --- " + str(nat_) + "\n")
        bt_save.state(["!disabled"])


def to_csv():
    """ store the content of the text box in a csv file """

    folder_ = os.path.exists(save_pad)
    # flag for existence folder

    if not folder_:
        os.makedirs(save_pad)

    text_TB = TB.get("1.0", "end-1c")
    with open(save_pad + H_ + file_, 'w') as f:
        for i_ in text_TB:
            f.write(str(i_))


def start_click():                                              # program flow
    Ip_1 = input_1.get()
    Ip_2 = input_2.get()
    Ip_3 = input_3.get()
    Ip_4 = input_4.get()
    f_input_test(Ip_1, Ip_2, Ip_3, Ip_4)
    f_berekening(H_, C_, Vn_, Vd_)


def save_click():                                               # program flow
    to_csv()
    m_b.showinfo("Info:", "Saved as: " + save_pad + H_ + file_)


def stop_click():                                               # program flow
    os.abort()


frame_1 = tk.Frame(root)
frame_1.pack()
frame_2 = tk.Frame(root)
frame_2.pack()
frame_3 = tk.Frame(root)
frame_3.pack()
frame_4 = tk.Frame(root)
frame_4.pack()
frame_5 = tk.Frame(root)
frame_5.pack()
frame_6 = tk.Frame(root)
frame_6.pack()
frame_7 = tk.Frame(root)
frame_7.pack()


label_1 = tk.Label(frame_1)                                 # label page, frame 1
label_1.config(
    text='-Diervoer Calculator-',
    font=('Helvetica 16 bold'), bg="light green")
label_1.pack(ipadx=0, ipady=10)


separator = ttk.Separator(                                  # separation line, frame 1
    frame_1,
    orient='horizontal')
separator.pack(fill='x', ipady=5)


lb_in = tk.Label(frame_2)                                   # label input box 1, frame 2
lb_in.config(
    text="naam dier:",
    font=('Helvetica 10 bold'))
lb_in.pack(side=tk.TOP)


input_1 = tk.StringVar()                                    # input box 1, frame 2
inputbox_1 = ttk.Entry(
    frame_2,
    textvariable=input_1,
    justify='center')
inputbox_1.pack(side=tk.BOTTOM)


lb_in = tk.Label(frame_3)                                   # label input box 2, frame 3
lb_in.config(
    text="gewicht droge voedingsstoffen per dag in gram:           ",
    font=('Helvetica 10 bold'))
lb_in.pack(side=tk.LEFT, ipady=3)


input_2 = tk.StringVar()                                    # input box 2, frame 3
inputbox_2 = ttk.Entry(
    frame_3,
    textvariable=input_2,
    justify='center')
inputbox_2.pack(side=tk.LEFT)


lb_in = tk.Label(frame_4)                                   # label input box 3, frame 4
lb_in.config(
    text="% droge voedingsstoffen in natvoer, gemiddeld 25%:    ",
    font=('Helvetica 10 bold'))
lb_in.pack(side=tk.LEFT, ipady=3)


input_3 = tk.StringVar()                                    # input box 3, frame 4
inputbox_3 = ttk.Entry(
    frame_4,
    textvariable=input_3,
    justify='center')
inputbox_3.pack(side=tk.LEFT)


lb_in = tk.Label(frame_5)                                   # label input box 4, frame 5
lb_in.config(
    text="% droge voedingsstoffen in droogvoer, gemiddeld 60%:",
    font=('Helvetica 10 bold'))
lb_in.pack(side=tk.LEFT, ipady=3)


input_4 = tk.StringVar()                                    # input box 4, frame 5
inputbox_4 = ttk.Entry(
    frame_5,
    textvariable=input_4,
    justify='center')
inputbox_4.pack(side=tk.LEFT)


bt_show = ttk.Button(                                       # button start, frame 6
    frame_6,
    text="start",
    command=start_click)
bt_show.pack(side=tk.LEFT, ipady=3)


bt_save = ttk.Button(                                       # button save, frame 6
    frame_6,
    text='save',
    command=save_click)
bt_save.pack(side=tk.LEFT, ipady=3)


bt_stop = ttk.Button(                                       # button STOP, frame 6
    frame_6,
    text='STOP',
    command=stop_click)
bt_stop.pack(side=tk.LEFT, ipady=3)


separator = ttk.Separator(                                  # empty line frame 6
    frame_6,
    orient='horizontal')
separator.pack(ipady=25)


TB = tk.Text(                                              # text box, frame 7
    frame_7,
    width=60, height=20, bd=12,
    relief="groove")


TB.pack(                                                   # text box, location
    side=tk.TOP, expand=False)


TB.insert("1.0", info_tekst)
inputbox_1.focus()
bt_save.state(["disabled"])

root.mainloop()
