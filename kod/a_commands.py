import oracledb
import a_gui
import hashlib
from tkinter import messagebox as MessageBox, messagebox
import connect
import display_infos as dp
import tkinter as tk



def user_mod():
    email = gui.userEmailEntry.get()
    password = gui.userPasswordEntry.get()
    password2 = gui.userPassword2Entry.get()

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


def user_delete():
    email = gui.userEmailEntry.get()

    db = connect.connect()

    cursor = db.cursor()
    try:
        cursor.execute('delete from felhasznalok where email=:s', (email,))
        db.commit()
        MessageBox.showinfo("Done", "Felhasználó törölve")

    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Ez nem jött be és a következő a hiba: {}".format(err))

    cursor.close()




def facts():
    db = connect.connect()

    sql ="""SELECT V.nev, COUNT(A.id) AS allomasok_szama
                FROM Varosok V
                JOIN Allomasok A ON V.irsz = A.varos_irsz
                GROUP BY V.nev
                ORDER BY allomasok_szama DESC
                FETCH FIRST 1 ROW ONLY"""

    sql1 = """SELECT VV.nev, COUNT(M.id) AS megallok_szama
                FROM VonatVonalak VV
                JOIN Megallok M ON VV.id = M.vonal_id
                GROUP BY VV.nev
                ORDER BY megallok_szama DESC
                FETCH FIRST 1 ROW ONLY"""

    sql2 = """SELECT A.nev, COUNT(VV.id) AS vonatok_szama
                FROM Allomasok A
                JOIN VonatVonalak VV ON A.id = VV.honnan_id
                GROUP BY A.nev
                ORDER BY vonatok_szama DESC
                FETCH FIRST 1 ROW ONLY"""

    sql3 = """SELECT M.nev, COUNT(*) AS kesesek_szama
                    FROM Megallok M
                    JOIN Menetrendek Me ON M.id = Me.megallo_id
                    WHERE Me.erkezik_kovetkezo < Me.indul
                    GROUP BY M.nev
                    ORDER BY kesesek_szama DESC
                    FETCH FIRST 1 ROW ONLY"""

    cursor1 = db.cursor()
    cursor2 = db.cursor()
    cursor3 = db.cursor()
    cursor4 = db.cursor()
    try:
        cursor1.execute(sql)
        result1 = cursor1.fetchone()
        cursor2.execute(sql1)
        result2 = cursor2.fetchone()
        cursor3.execute(sql2)
        result3 = cursor3.fetchone()
        cursor4.execute(sql3)
        result4 = cursor4.fetchone()


    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Hiba történt a belépés során: {}".format(err))

    db.close()

    gui.facts(result1, result2, result3, result4)


