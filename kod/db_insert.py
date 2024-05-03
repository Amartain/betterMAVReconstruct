from a_commands import *

def add_city(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text='Állomás neve').pack(pady=10)
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

    backButton = tk.Button(root, text='Vissza', width=20, height=2, command=dp.admin_display).pack(pady=10)


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