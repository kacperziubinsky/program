from db import data
from db import hour
from db import answear
from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Program księgowy")
win.geometry("1040x350")


def oblicz():
    y=entry.get()
    label5 = ttk.Label(win, text="Dane Pracowników", font=('Arial', 25)).grid(column=2, row=2)
    wynik = ttk.Treeview(win, column=("Miesiąc", "Wypłata"), height=2, show='headings')
    wynik.column("# 1", anchor=CENTER)
    wynik.heading("# 1", text="Miesiąc")
    wynik.column("# 2", anchor=CENTER)
    wynik.heading("# 2", text="Wypłata")

    u = answear(y)

    for x in u:
        wynik.insert('', 'end', values=(x[3], x[4]))
    wynik.grid(column=2, row=3)



label1=ttk.Label(win, text="Dane Pracowników", font=('Arial', 25)).grid(column=1, row=0)

tree = ttk.Treeview(win, column=("ID.", "Stawka godzinowa"), height=5, show='headings')
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID.")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Stawka godzinowa")


l=data()

for i in l:
    tree.insert('', 'end', text="1", values=(i[0], i[1]))

tree.grid(column=1, row=1, padx=10, pady=10)



label2=ttk.Label(win, text="Przepracowane godziny", font=('Arial', 25)).grid(column=2, row=0)
treel=ttk.Treeview(win, columns=("Miesiąc", "Godziny", "ID Pracownika"), show='headings', height=5)
treel.column("#1", anchor=CENTER)
treel.heading("#1", text="Miesiąc")
treel.column("#2", anchor=CENTER)
treel.heading("#2", text="Godziny")
treel.column("#3", anchor=CENTER)
treel.heading("#3", text="ID pracownika")

z=hour()

for x in z:
    treel.insert('', 'end', text="1", values=(x[0], x[1], x[2]))

treel.grid(column=2, row=1, padx=10, pady=10)




label3=ttk.Label(win, text="Obliczanie wypłat", font=('Arial', 25)).grid(column=1, row=2)
label4=ttk.Label(win, text="Podaj numer ID pracownika:", font=('Arial', 15)).grid(column=1,row=3)
entry=ttk.Entry(win)
entry.grid(column=1,row=4)
button=ttk.Button(win, text="Oblicz!", command=oblicz).grid(column=1,row=5)





win.mainloop()