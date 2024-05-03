import oracledb
import tkinter as tk
from tkinter import messagebox as MessageBox
def search_jaratok(honnan, hova, time, date):


    table = tk.Frame(list_project_participants_window)
    try:
        table.pack_forget()
        dsn = oracledb.makedsn("localhost", 1521, service_name="xe")
        connection = oracledb.connect(user="MATT", password="matt", dsn=dsn)

        cursor = connection.cursor()

        sql = """
            SELECT 
            M.indul AS "Indulás",
            M.erkezik_kovetkezo AS "Érkezés",
            COALESCE(MM.tav_kezdotol, 888) AS "Távolság",
            V1.nev AS "Honnan (városnév)",
            V2.nev AS "Hova (városnév)"
        FROM 
            Menetrendek M
        JOIN 
            Megallok MM ON M.megallo_id = MM.id
        JOIN 
            Allomasok A1 ON MM.allomasok_id = A1.id
        JOIN 
            Varosok V1 ON A1.varos_irsz = V1.irsz
        JOIN 
            Allomasok A2 ON MM.kovetkezo_id = A2.id
        JOIN 
            Varosok V2 ON A2.varos_irsz = V2.irsz
        WHERE 
            V1.nev = :s;

            """
        try:
            cursor.execute(sql, honnan)
        except Exception as e:
            print(e)

        result = cursor.fetchall()
        # tablazat ode

        table.pack()
        if (len(result) == 0):
            MessageBox.showinfo("Hiba", "Nincs projekt dolgozo!")
        for i in range(len(result)):
            for j in range(len(result[i])):
                e = tk.Entry(table, width=15, fg='black', font=('Arial', 12))
                e.grid(row=i, column=j)
                e.insert(tk.END, result[i][j])
    except Exception as err:
        MessageBox.showinfo("Hiba", "Hiba történt a lekérdezés során: {}".format(err))
        cursor.close()
        connection.close()


