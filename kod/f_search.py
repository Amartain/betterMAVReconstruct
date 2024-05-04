from tkcalendar import DateEntry
import re
from a_gui import *
from tkinter import messagebox


# eventek lekezelese


def openSearchwindow():
    def handle_entry_click(event):
        # ha kattintva ne legyen default uzenet de csak az ne
        if time_entry.get() == "HH:mm":
            time_entry.delete(0, tk.END)

    def handle_entry_leave(event):
        # ha ures es nincs rakkatintva mar lost focus --> akkor .insertel lehet berakni default szoveget
        if not time_entry.get():
            time_entry.insert(0, "HH:mm")

    # ablak megnyitas
    window = tk.Tk()
    window.title("BetterMAV Menetrend")
    window.geometry('800x600')
    window.configure(bg='black')
    all_day_var = tk.StringVar()

    # INput mezok
    from_label = tk.Label(window, text="Honnan:", bg='black', fg='white', font=("Helvetica", 16))
    from_entry = tk.Entry(window, font=("Helvetica", 16), fg='black', bg='white')
    to_label = tk.Label(window, text="Hova:", bg='black', fg='white', font=("Helvetica", 16))
    to_entry = tk.Entry(window, font=("Helvetica", 16), fg='black', bg='white')
    date_label = tk.Label(window, text="Dátum:", bg='black', fg='white', font=("Helvetica", 16))
    date_entry = DateEntry(window, font=("Helvetica", 16), fg='black', bg='white', date_pattern='y-mm-dd')
    all_day_check = tk.Checkbutton(window, text="Egész napos keresés", variable=all_day_var, bg='black', fg='white', font=("Helvetica", 16))
    time_label = tk.Label(window, text="Idő:", bg='black', fg='white', font=("Helvetica", 16))
    time_entry = tk.Entry(window, font=("Helvetica", 16), fg='black', bg='white')
    time_entry.insert(0, "HH:mm")

    # INput kirakasa hogy szep legyen packel
    from_label.pack(pady=10)
    from_entry.pack(pady=10)
    to_label.pack(pady=10)
    to_entry.pack(pady=10)
    date_label.pack(pady=10)
    date_entry.pack(pady=10)
    time_label.pack(pady=10)
    time_entry.pack(pady=10)

    # time entry default szoveg, es kattintas bind kell kulonben nem fut le a default cucc
    # Bind events to handle default text behavior
    time_entry.bind("<FocusIn>", handle_entry_click)
    time_entry.bind("<FocusOut>", handle_entry_leave)

    # --------------------------------------- IMPLEMENTATON (DO NOT EXPOSE OUTSIDE OF THIS SCOPE ---------------------------

    # kereses funkcio
    def search_trains():
        from_city = from_entry.get()
        to_city = to_entry.get()
        date = date_entry.get_date()
        time = time_entry.get()
        all_day = all_day_var.get()

        # Itt kellene implementálni az Oracle adatbázisból történő lekérdezést
        # és a vonatjáratok listázását


    # validalasa az ido INputnak
        # Validate time format (HH:mm)
        time_pattern = r"^(?:[01]?[0-9]|2[0-3]):[0-5][0-9]$"
        if not re.match(time_pattern, time):
            messagebox.showerror("Hiba", "Érvénytelen idő formátum (HH:mm)!")
            return

        messagebox.showinfo("Keresés", "Keresés indítva a következő paraméterekkel:\nHonnan: {}\nHova: {}\nDátum: {}\nIdő: {}".format(from_city, to_city, date, time))
        open_results(from_city, to_city, date, time)


    search_button = tk.Button(window, text="Keresés", command=search_trains, font=("Helvetica", 16))
    search_button.pack(pady=10)

    close_button = tk.Button(window, text="Kilépés", command=window.destroy)
    close_button.pack(pady=10)

    window.mainloop()


def open_results(honnan, hova, time, date):
    #ablak alap
    window = tk.Tk()
    window.title("BetterMAV Menetrend")
    window.geometry('1000x800')
    window.configure(bg='black')

    style = ttk.Style(window)
    style.configure("Treeview", font=('Helvetica', 14), background='RoyalBlue', foreground='white')
   # style.configure("Treeview.Heading", font=('Helvetica', 14), background='Black', foreground='white')


    # base infok
    login_label = tk.Label(window, text="Jegyvásárláshoz kérjük jelentkezzen be!", bg='black', fg='white', font=("Helvetica", 16))
    login_label.pack(pady=10)

    # listazas
    train_list = ttk.Treeview(window, columns=("Indulás", "Érkezési idő", "Távolság", "Induló állomás", "Érkező állomás"), show='headings')
    train_list.heading("Indulás", text="Indulás")
    train_list.heading("Érkezési idő", text="Érkezési idő")
    train_list.heading("Távolság", text="Távolság")
    train_list.heading("Induló állomás", text="Induló állomás")
    train_list.heading("Érkező állomás", text="Érkező állomás")
    train_list.pack(pady=10)

    def show_searched(honnan, hova):
        # Mock data
        records = [
            {
                "Indulás": "2024-04-18 08:00:00",
                "Érkezési idő": "2024-04-18 10:00:00",
                "Távolság": 200,
                "Induló állomás": honnan,
                "Érkező állomás": hova
            },
            {
                "Indulás": "2024-04-18 09:00:00",
                "Érkezési idő": "2024-04-18 11:00:00",
                "Távolság": 200,
                "Induló állomás": honnan,
                "Érkező állomás": hova
            },
            # Add more records as needed
        ]

        return records
    # oraclelel
    #results = fetch.search_jaratok(honnan, hova, time, date)

    # oracle nelkuli teszt zumo
    results = show_searched(honnan, hova)


    for result in results:
        train_list.insert('', 'end', values=(result['Indulás'], result['Érkezési idő'], result['Távolság'], result['Induló állomás'], result['Érkező állomás']))

    close_button = tk.Button(window, text="Kilépés", command=window.destroy)
    close_button.pack(pady=10)

    window.mainloop()


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



