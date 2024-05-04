from a_commands import *
from a_gui import *


def list_city(root, result):
    for widget in root.winfo_children():
        widget.destroy()
    searchLabel = tk.Label(root, text="Keresés")

    searchLabel.pack(pady=10)
    global searchBar
    searchBar = tk.Entry(root)
    searchBar.pack(pady=10)
    searchButton = tk.Button(root, text="Keresés", width=20, height=2, command=search_by_city)
    searchButton.pack(pady=10)

    factsButton = tk.Button(root, text="érdekességek", width=20, height=2, command=facts.fetch_facts)
    factsButton.pack(pady=10)

    schedualLabel = tk.Label(root, text="Menetrendek")
    schedualLabel.pack(pady=10)

    tree = ttk.Treeview(root, columns=("Column1", "Column2", "Column3", "Column4", "Column5"), show="headings")
    tree.heading("#1", text="Honnan")
    tree.heading("#2", text="Hova")
    tree.heading("#3", text="Indulás")
    tree.heading("#4", text="Érkezés")
    tree.heading("#5", text="Peron")

    # Adatok hozzáadása a Treeview-hoz
    for row in result:
        tree.insert("", "end", values=row)

    # Treeview hozzáadása a Tkinter ablakhoz
    tree.pack(expand=True, fill="both", pady=10)

    backButton = tk.Button(root, text="Kijelentkezés", width=20, height=2, command=dp.display)
    backButton.pack(pady=10)

def fetch_city(root):
    db = connect.connect()

    sql = """SELECT 
    v1.nev AS indulas_varos,
    v2.nev AS kovetkezo_megallo_varos,
    me.indul AS indul,
    me.erkezik_kovetkezo AS erkezik,
    me.peron
FROM 
    Menetrendek me
JOIN 
    Megallok m ON me.megallo_id = m.id
JOIN 
    Allomasok a1 ON m.allomasok_id = a1.id
JOIN 
    Varosok v1 ON a1.varos_irsz = v1.irsz
JOIN 
    Allomasok a2 ON m.kovetkezo_id = a2.id
JOIN 
    Varosok v2 ON a2.varos_irsz = v2.irsz
"""
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()


    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Hiba történt a belépés során: {}".format(err))

    db.close()

    list_city(root, result)

def search_by_city():
    city = searchBar.get()
    print(searchBar.get())

    if city == "":
        list_city()
    else:

        db = connect.connect()

        sql = """SELECT 
            v1.nev AS indulas_varos,
            v2.nev AS kovetkezo_megallo_varos,
            me.indul AS indul,
            me.erkezik_kovetkezo AS erkezik,
            me.peron
        FROM 
            Menetrendek me
        JOIN 
            Megallok m ON me.megallo_id = m.id
        JOIN 
            Allomasok a1 ON m.allomasok_id = a1.id
        JOIN 
            Varosok v1 ON a1.varos_irsz = v1.irsz
        JOIN 
            Allomasok a2 ON m.kovetkezo_id = a2.id
        JOIN 
            Varosok v2 ON a2.varos_irsz = v2.irsz
            WHERE v1.nev = :s
        """
        cursor = db.cursor()
        try:
            cursor.execute(sql, (city,))
            result = cursor.fetchall()


        except oracledb.Error as err:
            MessageBox.showinfo("Hiba", "Hiba történt a belépés során: {}".format(err))

        db.close()

        list_city(tuple(result))


