import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import re
import displayResults as dr


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
        dr.open_results(from_city, to_city, date, time)


    search_button = tk.Button(window, text="Keresés", command=search_trains, font=("Helvetica", 16))
    search_button.pack(pady=10)

    close_button = tk.Button(window, text="Kilépés", command=window.destroy)
    close_button.pack(pady=10)

    window.mainloop()
