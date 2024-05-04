from tkinter import *
from tkinter import ttk
import a_commands
import db_connect
import a_gui
from a_gui import *
import f_login as login
import tkinter as tk
import f_facts as facts
import f_search as search


def display(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Button(text="Városok listája", width=20, height=2, command=lambda: show_list_cities(root)).pack(expand=True)

    tk.Button(text="Vonalak listája", width=20, height=2, command=lambda: list_Lines(root)).pack(expand=True)

    tk.Button(text="Menetrendek keresővel", width=20, height=2, command=search.openSearchwindow).pack(expand=True)

    tk.Button(text="Érdekességek", width=20, height=2, command=lambda: facts.show_facts(root)).pack(expand=True)

    tk.Button(text="Kijelentkezés", width=20, height=2, command=lambda: login.open_login(root)).pack(expand=True)


# --------------------------------------- IMPLEMENTATON (DO NOT EXPOSE OUTSIDE OF THIS SCOPE ---------------------------

def returnTo(root):
    display(root)



def show_list_cities(root):
    for widget in root.winfo_children():
        widget.destroy()
    db = connect.connect()
    cursor = db.cursor()

    result = cursor.execute("SELECT * FROM varosok")

    tree = ttk.Treeview(root, columns=("Column1", "Column2", "Column3", "Column4"), show="headings")
    tree.heading("#1", text="Irányítószám")
    tree.heading("#2", text="Név")
    tree.heading("#3", text="Régió")
    tree.heading("#4", text="Ország")

    # Adatok hozzáadása a Treeview-hoz
    for row in result:
        tree.insert("", "end", values=row)

    # Treeview hozzáadása a Tkinter ablakhoz
    tree.pack(expand=True, fill="both", pady=10)

    tk.Button(text="Vissza", width=20, height=2, command=lambda: returnTo(root)).pack(expand=True)

    db.close()



def list_Lines(root):
    for widget in root.winfo_children():
        widget.destroy()

    db = connect.connect()
    cursor = db.cursor()

    cursor.execute("SELECT nev FROM vonatvonalak")

    result = cursor.fetchall()

    print(result)

    tree = ttk.Treeview(root, columns=("c1"), show="headings")
    tree.heading("#1", text="Vonalnév")

    for row in result:
        tree.insert("", "end", values=row)

    tree.pack(expand=True)

    tk.Button(text="Vissza", width=20, height=2, command=lambda: returnTo(root)).pack(expand=True)

    db.close()



