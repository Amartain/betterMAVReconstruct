import tkinter
from oracledb import *
from a_commands import *
import db_connect as connect
import f_admin as admin
from a_gui import *
import random
import GUI_factory as Maker


def returnTo(root):
    admin.display(root)


# City
def show_add_city(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text='Város neve').pack(pady=10)
    global nevE
    nevE = tk.Entry(root)
    nevE.pack(pady=10)
    tk.Label(root, text='Irányítószám').pack(pady=10)
    global irszE
    irszE = tk.Entry(root)
    irszE.pack(pady=10)
    tk.Label(root, text='Régió').pack(pady=10)
    global regioE
    regioE = tk.Entry(root)
    regioE.pack(pady=10)
    tk.Label(root, text='Orszag').pack(pady=10)
    global orszagE
    orszagE = tk.Entry(root)
    orszagE.pack(pady=10)

    okAE = tk.Button(root, text='INSERT', width=20, height=2, command=insert_city)
    okAE.pack()

    backButton = tk.Button(root, text='Vissza', width=20, height=2, command=lambda: returnTo(root)).pack(pady=10)


def insert_city():
    nev = nevE.get()
    irsz = irszE.get()
    regio = regioE.get()
    orszag = orszagE.get()
    db = connect.connect()

    print(nev)

    if not (irszE and nevE and regioE and orszagE):
        MessageBox.showinfo("Hiba", "Minden mező kitöltése kötelező!")
        return

    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (:s, :s, :s, :s)",
            (irsz, nev, regio, orszag))
        db.commit()
        MessageBox.showinfo("Siker", "Sikeresen hozzáadva!")
        nevE.delete(0, 'end')
        irszE.delete(0, 'end')
        regioE.delete(0, 'end')
        orszagE.delete(0, 'end')
    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Hiba történt a regisztráció során: {}".format(err))
        db.rollback()

    db.close()


# insert station
def show_add_station(root):
    for widget in root.winfo_children():
        widget.destroy()

    Maker.labelMaker(root, "Állomásnév")
    nev = (tk.Entry(root))
    nev.pack(expand=10)

    Maker.labelMaker(root, "Cím")
    cim = tk.Entry(root)
    cim.pack(expand=10)

    Maker.labelMaker(root, "Város irányítószáma")
    irsz = tk.Entry(root)
    irsz.pack(expand=10)

    tk.Button(root, text="Hozzáad", command=lambda: insert_station(root, nev.get(), cim.get(), irsz.get())).pack()


def insert_station(root, name, address, postCode):
    db = connect.connect()
    cursor = db.cursor()

    id = random.randrange(0, 10000)

    try:
        cursor.execute("INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (:s, :s, :s, :s)",
                       (id, postCode, name, address))
        db.commit()
        MessageBox.showinfo("Siker", "Sikeresen hozzáadva!")
        show_add_station(root)
    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Hiba történt a hozzáadás során: {}".format(err))
        db.rollback()

    db.close()


# insert train line

def show_add_Trainline(root):
    for widget in root.winfo_children():
        widget.destroy()

    Maker.labelMaker(root, "Vonalnév")
