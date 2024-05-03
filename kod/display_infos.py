from tkinter import *
from tkinter import ttk
import a_commands
import connect
import a_gui
import tkinter as tk


def display(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Button(text="Városok listája", width=20, height=2, command=list_cities).pack(expand=True)

    tk.Button(text="Vonalak listája", width=20, height=2, command=list_Lines).pack(expand=True)

    tk.Button(text="Menetrendek keresővel", width=20, height=2, command=commands.list_city).pack(expand=True)

    tk.Button(text="Érdekességek", width=20, height=2, command=commands.facts).pack(expand=True)

    tk.Button(text="Kijelentkezés", width=20, height=2, command=gui.open_login).pack(expand=True)


def admin_display(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Button(text="Vonalak listája", width=20, height=2, command=list_Lines_admin).pack(expand=True)

    tk.Button(text="Városok listája", width=20, height=2, command=lambda: list_cities(True)).pack(expand=True)

    tk.Button(text="Felhasznalok listaja", width=20, height=2, command=list_users).pack(expand=True)

    tk.Button(text="Felhasznaló jelszó módosítása", width=20, height=2, command=gui.update_user).pack(expand=True)

    tk.Button(text="Felhasznaló törlése", width=20, height=2, command=gui.delete_user).pack(expand=True)

    tk.Button(text="Város hozzáadása listaja", width=20, height=2, command=gui.add_city).pack(expand=True)

    tk.Button(text="Kijelentkezés", width=20, height=2, command=gui.open_login).pack(expand=True)


def list_cities(root, isAdmin=False):
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

    if (isAdmin):
        tk.Button(text="Vissza", width=20, height=2, command=admin_display).pack(expand=True)
    else:
        tk.Button(text="Vissza", width=20, height=2, command=display).pack(expand=True)

    db.close()


def list_Lines():
    for widget in gui.root.winfo_children():
        widget.destroy()

    db = connect.connect()
    cursor = db.cursor()

    cursor.execute("SELECT nev FROM vonatvonalak")

    result = cursor.fetchall()

    print(result)

    tree = ttk.Treeview(gui.root, columns=("c1"), show="headings")
    tree.heading("#1", text="Vonalnév")

    for row in result:
        tree.insert("", "end", values=row)

    tree.pack(expand=True)

    tk.Button(text="Vissza", width=20, height=2, command=display).pack(expand=True)

    db.close()


def list_Lines_admin():
    for widget in gui.root.winfo_children():
        widget.destroy()

    db = connect.connect()
    cursor = db.cursor()

    cursor.execute("SELECT nev FROM vonatvonalak")

    result = cursor.fetchall()

    print(result)

    tree = ttk.Treeview(gui.root, columns=("c1"), show="headings")
    tree.heading("#1", text="Vonalnév")

    for row in result:
        tree.insert("", "end", values=row)

    tree.pack(expand=True)
    tk.Button(text="Vissza", width=20, height=2, command=admin_display).pack(expand=True)

    db.close()


def list_users():
    for widget in gui.root.winfo_children():
        widget.destroy()

    db = connect.connect()
    cursor = db.cursor()

    cursor.execute("Select email, nev, utastipus FROM felhasznalok")
    result = cursor.fetchall()

    print(result)

    tree = ttk.Treeview(gui.root, columns=("C1", "C2", "C3"), show="headings")
    tree.heading("#1", text="E-mail")
    tree.heading("#2", text="Név")
    tree.heading("#3", text="Utastípus")

    for row in result:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both", pady=10)

    tk.Button(text="Vissza", width=20, height=2, command=admin_display).pack(expand=True)

    db.close()
