import tkinter as tk
import kod.connect as conn
from a_commands import *
from a_gui import *
import f_register as reg

global login_id_entry
global login_password_entry


def open_login(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("800x600")
    root.title("Menetrend")

    login_lable = tk.Label(root, text='Belépés', font=('bold', 20), bg='black', fg='white')
    login_lable.pack(pady=10)

    id_label = tk.Label(root, text='Email cím', font=('bold', 12), bg='black', fg='white')
    id_label.pack(pady=10)

    global login_id_entry
    login_id_entry = tk.Entry(root)
    login_id_entry.pack(pady=10)

    password_label = tk.Label(root, text='Jelszó', font=('bold', 12), bg='black', fg='white')
    password_label.pack(pady=10)

    global login_password_entry
    login_password_entry = tk.Entry(root, show='*')
    login_password_entry.pack(pady=10)

    login_button = tk.Button(root, text='Belépés', width=20, height=2, command=login)
    login_button.pack(pady=10)

    register_button = tk.Button(root, text='Regisztráció', width=20, height=2,
                                command=lambda: reg.open_registration(root))
    register_button.pack(pady=10)


def lerr(lineNum):
    print("line: " + str(lineNum) + "f_login.py")


def hello():
    print("Hello Arda")


def login():
    email = login_id_entry.get()
    jelszo = login_password_entry.get()
    if email[len(email) - 1] == ";":
        messagebox.showinfo("NOPE", "Try again sweaty!")

    jelszo_hash = hashlib.sha3_256(jelszo.encode()).hexdigest()
    jelszo = jelszo_hash

    db = conn.connect()

    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM felhasznalok WHERE email = :s", (email,))
        result = cursor.fetchone()

        if result is None:
            MessageBox.showinfo("Hiba", "Nincs ilyen ceges_ID!")
        elif result[2] != jelszo:
            MessageBox.showinfo("Hiba", "Hibás jelszó!")
        else:
            global Email
            Email = result[0]
            if result[1] == 'admin':
                MessageBox.showinfo("Info", "Üdvözöljük {} adminunk!".format(result[1]))
                global felhasznalo_email
                dp.admin_display()
            else:
                MessageBox.showinfo("Info", "Üdvözöljük {}!".format(result[1]))
                dp.display()
    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Hiba történt a belépés során: {}".format(err))

    db.close()
