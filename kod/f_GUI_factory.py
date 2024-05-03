import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox, messagebox


def labelMaker(window,text):
    tk.Label(window,text=text, font=('bold', 20), bg='black', fg='white').pack(expand=True)

