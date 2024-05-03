import tkinter as tk
from tkinter import ttk
import oracle_fetch as fetch

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

   # maga a fetch hivasa

    # testre ilyen mock resultal
    def mock_search_jaratok(honnan, hova):
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
    results = mock_search_jaratok(honnan, hova)


    for result in results:
        train_list.insert('', 'end', values=(result['Indulás'], result['Érkezési idő'], result['Távolság'], result['Induló állomás'], result['Érkező állomás']))

    close_button = tk.Button(window, text="Kilépés", command=window.destroy)
    close_button.pack(pady=10)

    window.mainloop()


