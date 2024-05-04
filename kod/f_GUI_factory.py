import tkinter as tk

def labelMaker(window,text):
    tk.Label(window,text=text, font=('bold', 20), bg='black', fg='white').pack(expand=True)

