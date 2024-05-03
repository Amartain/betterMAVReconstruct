import tkinter as tk
import oracledb
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import *
import connect
import a_commands
import display_infos as dp
import f_login as login
import f_register as reg


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







def facts(root, result1, result2, result3, result4):
    for widget in root.winfo_children():
        widget.destroy()

    mostStationsLabel = tk.Label(root, text="Melyik városban található a legtöbb állomás?")
    mostStationsLabel.pack(pady=10)
    if result1 != None:
        mostStationsNameLabel = tk.Label(root, text=result1[0] + ". Állomások száma: " + str(result1[1]))
        mostStationsNameLabel.pack(pady=10)
    else:
        mostStationsNameLabel = tk.Label(root, text="Mind egyforma")
        mostStationsNameLabel.pack(pady=10)

    mostLinesLabel = tk.Label(root, text="Melyik vonal érinti a legtöbb állomást?")
    mostLinesLabel.pack(pady=10)
    if result2 != None:
        mostLinesNameLabel = tk.Label(root, text=result2[0] + ". Vonalak száma: " + str(result2[1]))
        mostLinesNameLabel.pack(pady=10)
    else:
        mostLinesNameLabel = tk.Label(root, text="Egyforma a vonalak száma")
        mostLinesNameLabel.pack(pady=10)

    mostTrainLabel = tk.Label(root, text="Melyik állomásról indul a legtöbb vonat?")
    mostTrainLabel.pack(pady=10)
    if result3 != None:
        mostTrainNameLabel = tk.Label(root, text=result3[0] + ". Induló vonatok száma: " + str(result3[1]))
        mostTrainNameLabel.pack(pady=10)
    else:
        mostTrainNameLabel = tk.Label(root, text="Minden állomásról ugyan annyi indul")
        mostTrainNameLabel.pack(pady=10)

    mostDelayLabel = tk.Label(root, text="Melyik állomáson van a legtöbb késés?")
    mostDelayLabel.pack(pady=10)
    if result4 != None:
        mostDelayNameLabel = tk.Label(root, text=result4[0] + ". Átlagos késés: " + str(result4[1]))
        mostDelayNameLabel.pack(pady=10)
    else:
        mostDelayNameLabel = tk.Label(root, text="Az adatbázisunk jelenlegi adatai alapján egy vonatunk se késik :D")
        mostDelayNameLabel.pack(pady=10)

    tk.Button(root, text="Vissza", width=20, height=2, command=dp.display).pack(pady=10)


def update_user(root):
    for widget in root.winfo_children():
        widget.destroy()

    userEmailLabel = tk.Label(root, text="Váltosztandó felhasználó email címe")
    userEmailLabel.pack(pady=10)

    global userEmailEntry
    userEmailEntry = tk.Entry(root, width=20)
    userEmailEntry.pack(pady=10)

    usernewPassLabel = tk.Label(root, text="Váltosztandó felhasználó új jelszó")
    usernewPassLabel.pack(pady=10)

    global newUserPasswordEntry
    newPassword = tk.Entry(root, show='*')
    newPassword.pack(pady=10)

    usernewPassLabel2 = tk.Label(root, text="Váltosztandó felhasználó új jelszó ismét")
    usernewPassLabel2.pack(pady=10)

    global newUserPasswordEntry2
    newPassword2 = tk.Entry(root, show='*')
    newPassword2.pack(pady=10)

    usersUpdateButton = tk.Button(root, text="Jelszó frissítése", command=commands.user_mod,
                                  font=("Helvetica", 20), )
    usersUpdateButton.pack(pady=10)
    tk.Button(root, text="Vissza", width=20, height=2, command=dp.admin_display).pack(pady=10)
    tk.Button(root, text="Vissza", width=20, height=2, command=dp.admin_display).pack(pady=10)


def delete_user(root):
    for widget in root.winfo_children():
        widget.destroy()

    userEmailLabel = tk.Label(root, text="Váltosztandó felhasználó email címe")
    userEmailLabel.pack(pady=10)

    global userEmailEntry
    userEmailEntry = tk.Entry(root, width=20)
    userEmailEntry.pack(pady=10)

    usersDeleteButton = tk.Button(root, text="Felhasználó törlése", width=20, height=2, command=commands.user_delete,
                                  font=("Helvetica", 20))
    usersDeleteButton.pack(pady=10)

    backButton = tk.Button(root, text="Vissza", width=20, height=2, command=dp.admin_display).pack(pady=10)
