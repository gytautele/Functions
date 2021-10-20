from tkinter import *
import time
import sqlite3
import random
import tempfile
import win32api
import win32print

f = ''
flag = ''
flags = ''

login = sqlite3.connect("admin.db")
l = login.cursor()

c = sqlite3.connect("medicine.db")
cur = c.cursor()

columns = ('Sl No', 'Name', 'Type', 'Quantity Left', 'Cost', 'Purpose', 'Expiry Date', 'Rack location', 'Manufacture')


def open_win():
    global apt, flag
    flag = 'apt'
    apt = Tk()
    apt.title("Interface")
    Label(apt, text="EVANZ MEDICAL STORE COMPANY").grid(row=0, column=0, columnspan=3)
    Label(apt, text='*' * 80).grid(row=1, column=0, columnspan=3)
    Label(apt, text='-' * 80).grid(row=3, column=0, columnspan=3)

    Label(apt, text="Stock Maintenance", bg='green', fg='white').grid(row=2, column=0)
    Button(apt, text='New V.C.', width=25, bg='green', fg='white', command=val_cus).grid(row=4, column=0)
    Button(apt, text='Add product to Stock', bg='green', fg='white', width=25, command=stock).grid(row=5, column=0)
    Button(apt, text='Delete product from Stock', bg='red', fg='white', width=25, command=delete_stock).grid(row=6,
                                                                                                             column=0)

    Label(apt, text="Access Database", bg='blue', fg='white').grid(row=2, column=1)
    Button(apt, text='Modify', width=15, bg='blue', fg='white', command=modify).grid(row=4, column=1)
    Button(apt, text='Search', width=15, bg='blue', fg='white', command=search).grid(row=5, column=1)
    Button(apt, text='Expiry Check', bg='red', fg='white', width=15, command=exp_date).grid(row=6, column=1)

    Label(apt, text="Handle Cash Flows", bg='skyblue', fg='black').grid(row=2, column=2)
    Button(apt, text="Check Today's Revenue", bg='skyblue', fg='black', width=20, command=show_rev).grid(row=5,
                                                                                                         column=2)
    Button(apt, text='Billing', width=20, bg='skyblue', fg='black', command=billing).grid(row=4, column=2)
    Button(apt, text='Logout', bg='red', fg='white', width=20, command=again).grid(row=6, column=2)
    apt.mainloop()
