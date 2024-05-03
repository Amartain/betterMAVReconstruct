import a_gui
from a_gui import *
import a_commands
from a_commands import *
import f_login as login



def open_registration(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("800x600")
    root.title("Menetrend")
    
    root.geometry("800x600")
    root.title("Regisztráció")
    root.configure(background="black")

    welcome_label = tk.Label(root, text='Regisztráció', font=('bold', 20))
    welcome_label.pack(pady=10)

    name_label = tk.Label(root, text='Név', font=('bold', 12))
    name_label.pack(pady=5)
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.pack(pady=10)

    password_label = tk.Label(root, text='Jelszó', font=('bold', 12))
    password_label.pack(pady=5)
    global password_entry
    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=10)

    password_confirm_label = tk.Label(root, text='Jelszó megerősítése', font=('bold', 12))
    password_confirm_label.pack(pady=5)
    global password_confirm_entry
    password_confirm_entry = tk.Entry(root, show='*')
    password_confirm_entry.pack(pady=10)

    email_label = tk.Label(root, text='E-mail', font=('bold', 12), bg='black', fg='white')
    email_label.pack(pady=5)
    global email_entry
    email_entry = tk.Entry(root)
    email_entry.pack(pady=10)

    global tipusE
    tipusE = StringVar(root)
    tipusE.set("Felnőtt")

    tk.Label(root, text='Utastípus', font=('bold', 12), bg='black', fg='white').pack()
    OptionMenu(root, tipusE, 'Felnőtt', 'Tanuló', 'Gyermek', 'Nyugdíjas', 'Kedvezményes', 'Admin').pack(
        expand=True)


    login_button = tk.Button(root, text='Belépés', width=20, height=2, command=lambda: login.open_login(root))
    login_button.pack(pady=10)

    registrate_button = tk.Button(root, text='Regisztráció', width=20, height=2, command=register)
    registrate_button.pack(pady=10)


def register():
    nev = name_entry.get()
    jelszo = password_entry.get()
    jelszo_megerosites = password_confirm_entry.get()
    email = email_entry.get()
    tipus = tipusE.get()

    if email[len(email) - 1] == ";":
        messagebox.showinfo("NOPE", "Try again sweaty!")

    if not (nev and jelszo and email):
        MessageBox.showinfo("Hiba", "Minden mező kitöltése kötelező!")
        return

    if jelszo != jelszo_megerosites:
        MessageBox.showinfo("Hiba", "A jelszavak nem egyeznek!")
        return

    jelszo_hash = hashlib.sha3_256(jelszo.encode()).hexdigest()
    jelszo = jelszo_hash
    password_entry.delete(0, 'end')
    password_confirm_entry.delete(0, 'end')
    jelszo_megerosites = ""

    db = connect.connect()

    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO Felhasznalok (email, nev, jelszo, utastipus) VALUES (:s, :s, :s, :s)",
            (email, nev, jelszo, tipus))
        db.commit()
        MessageBox.showinfo("Siker", "Sikeres regisztráció!")
        MessageBox.showinfo("Siker", "A ceges_ID: {}".format(email))
    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Hiba történt a regisztráció során: {}".format(err))
        db.rollback()

    db.close()
