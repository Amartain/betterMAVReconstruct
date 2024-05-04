from a_commands import *
from a_gui import *
import db_connect as connect
import f_user_main as user
import f_GUI_factory as Maker


def db_facts():
    db = connect.connect()

    sql = """SELECT V.nev, COUNT(A.id) AS allomasok_szama
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

    return result1, result2, result3, result4

  #  show_facts(root, result1, result2, result3, result4)


def returnTo(window):
    user.display(window)


def show_facts(root):
    for widget in root.winfo_children():
        widget.destroy()

    result1, result2, result3, result4 = db_facts()

    text0 = "Melyik városban található a legtöbb állomás?"
    Maker.labelMaker(root,text0)

    if result1 != None:
        text1 = result1[0] + ". Állomások száma: " + str(result1[1])
        Maker.labelMaker(root,text1)
    else:
        tk.Label(root, text="Mind egyforma").pack(pady=10)

        text3="Melyik vonal érinti a legtöbb állomást?"
        Maker.labelMaker(root,text3)
    if result2 != None:
        text4=result2[0] + ". Vonalak száma: " + str(result2[1])
        Maker.labelMaker(root,text4)
    else:
        text4="Egyforma a vonalak száma"
        Maker.labelMaker(root,text4)

    text5="Melyik állomásról indul a legtöbb vonat?"
    Maker.labelMaker(root, text5)
    if result3 != None:
        text6=result3[0] + ". Induló vonatok száma: " + str(result3[1])
        Maker.labelMaker(root,text6)
    else:
        text6="Minden állomásról ugyan annyi indul"
        Maker.labelMaker(root, text6)

    text7="Melyik állomáson van a legtöbb késés?"
    Maker.labelMaker(root,text7)
    if result4 != None:
        text8=result4[0] + ". Átlagos késés: " + str(result4[1])
        Maker.labelMaker(root,text8)
    else:
        text8="Az adatbázisunk jelenlegi adatai alapján egy vonatunk se késik :D"
        Maker.labelMaker(root, text8)

    tk.Button(root, text="Vissza", width=20, height=2, command=lambda: returnTo(root)).pack(pady=10)
