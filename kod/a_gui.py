import tkinter as tk
import oracledb
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import *
import db_connect
import a_commands
import f_user_main as dp
from f_user_main import *
import f_login as login
import f_register as reg
import f_facts as facts
from f_facts import *


def open_start():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Menetrend")
    root.configure(background="black")

    try:
        # A user-t meg a jelszo-t sajátra köll átállítani hogy működjön
        db = connect.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Felhasznalok")
        result = cursor.fetchall()
        print("Result:", result)
        if (result):
            MessageBox.showinfo("Siker", "Sikeres csatlakozás az adatbázishoz")
            main_window(root)
        else:
            MessageBox.showerror("Hiba", "Nem sikerült az adazbázishoz csatlakozni.")
            root.destroy()
        cursor.close()
        db.close()
        root.mainloop()
    except oracledb.Error as error:
        print("Error:", error)


def main_window(root):
    for widget in root.winfo_children():
        widget.destroy()

    login_button = tk.Button(
        root,
        text='Belépés',
        width=20, height=2,
        command=lambda: login.open_login(root),
        bg='white', fg='black'
    )
    login_button.pack(pady=10)

    register_button = tk.Button(
        root,
        text='Regisztráció',
        width=20, height=2,
        command=lambda: reg.open_registration(root),
        bg='white', fg='black'
    )
    register_button.pack(pady=10)


