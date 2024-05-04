from a_gui import *
from db_insert import *


# anchor function - only func to be exposed outside of this file!
def display(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Button(text="Vonalak listája", width=20, height=2, command=lambda: list_Lines(root)).pack(expand=True)

    tk.Button(text="Városok listája", width=20, height=2, command=lambda: show_list_cities(True)).pack(expand=True)

    tk.Button(text="Felhasznalok listaja", width=20, height=2, command=list_users).pack(expand=True)

    tk.Button(text="Felhasznaló jelszó módosítása", width=20, height=2, command=lambda: update_user(root)).pack(
        expand=True)

    tk.Button(text="Felhasznaló törlése", width=20, height=2, command=show_delete_user).pack(expand=True)

    tk.Button(text="Város hozzáadása listaja", width=20, height=2, command=lambda: show_add_city(root)).pack(
        expand=True)

    tk.Button(text="Kijelentkezés", width=20, height=2, command=lambda: login.open_login(root)).pack(expand=True)


# --------------------------------------- IMPLEMENTATON (DO NOT EXPOSE OUTSIDE OF THIS SCOPE ---------------------------
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
    tk.Button(text="Vissza", width=20, height=2, command=lambda: display(root)).pack(expand=True)

    db.close()


def update_user(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Váltosztandó felhasználó email címe").pack(pady=10)

    userEmailEntry = tk.Entry(root, width=20)
    userEmailEntry.pack(pady=10)

    tk.Label(root, text="Váltosztandó felhasználó új jelszó").pack(pady=10)

    newPassword = tk.Entry(root, show='*')
    newPassword.pack(pady=10)

    tk.Label(root, text="Váltosztandó felhasználó új jelszó ismét").pack(pady=10)

    newPassword2 = tk.Entry(root, show='*')
    newPassword2.pack(pady=10)

    tk.Button(root, text="Jelszó frissítése", command=lambda: user_mod(userEmailEntry, newPassword, newPassword2),
              font=("Helvetica", 20)).pack(pady=10)
    tk.Button(root, text="Vissza", width=20, height=2, command=dp.admin_display).pack(pady=10)
    tk.Button(root, text="Vissza", width=20, height=2, command=dp.admin_display).pack(pady=10)


def user_mod(newMail, newPw, newPwConf):
    email = newMail.get()
    password = newPw.get()
    password2 = newPwConf.get()

    if password == password2:
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        password = hashedPassword

        db = connect.connect()
        cursor = db.cursor()

        try:
            cursor.execute('update felhasznalok set jelszo=:s  where email=:s', (password, email,))
            db.commit()
            MessageBox.showinfo("Done", "Felhasználó módosítva")

        except:
            MessageBox.showinfo("Hiba", "Ez nem jött be")

        cursor.close()

    else:
        MessageBox.showinfo("Hiba", "A két jelszó nem egyezik meg")


def show_delete_user(root):
    for widget in root.winfo_children():
        widget.destroy()

    userEmailLabel = tk.Label(root, text="Váltosztandó felhasználó email címe")
    userEmailLabel.pack(pady=10)

    global userEmailEntry
    userEmailEntry = tk.Entry(root, width=20)
    userEmailEntry.pack(pady=10)

    usersDeleteButton = tk.Button(root, text="Felhasználó törlése", width=20, height=2,
                                  command=lambda: delete_user(userEmailEntry), font=("Helvetica", 20))
    usersDeleteButton.pack(pady=10)

    tk.Button(root, text="Vissza", width=20, height=2, command=lambda: display(root)).pack(pady=10)


def delete_user(emailE):
    email = emailE.get()

    db = connect.connect()

    cursor = db.cursor()
    try:
        cursor.execute('delete from felhasznalok where email=:s', (email,))
        db.commit()
        MessageBox.showinfo("Done", "Felhasználó törölve")

    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Ez nem jött be és a következő a hiba: {}".format(err))

    cursor.close()


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

    tk.Button(text="Vissza", width=20, height=2, command=display).pack(expand=True)

    db.close()

