def modify():
    global cur, c, accept, flag, att, up, n, name_, apt, st, col, col_n
    col = ('', '', 'type', 'qty_left', 'cost', 'purpose', 'expdt', 'loc', 'mfg')
    col_n = ('', '', 'Type', 'Quantity Left', 'Cost', 'Purpose', 'Expiry Date', 'Rack location', 'Manufacture')
    flag = 'st'
    name_ = ''
    apt.destroy()
    n = []
    cur.execute("select * from med")
    for i in cur:
        n.append(i[1])
    c.commit()
    st = Tk()
    st.title('MODIFY')
    Label(st, text='-' * 48 + ' MODIFY DATABASE ' + '-' * 48).grid(row=0, column=0, columnspan=6)

    def onvsb(*args):
        name_.yview(*args)

    def onmousewheel():
        name_.ywiew = ('scroll', event.delta, 'units')
        return 'break'

    cx = 0
    vsb = Scrollbar(orient='vertical', command=onvsb)
    vsb.grid(row=1, column=3, sticky=N + S)
    name_ = Listbox(st, width=43, yscrollcommand=vsb.set)
    cur.execute("select *from med")
    for i in cur:
        cx += 1
        name_.insert(cx, (str(i[0]) + '.  ' + str(i[1])))
        name_.grid(row=1, column=1, columnspan=2)
    c.commit()
    name_.bind('<MouseWheel>', onmousewheel)
    name_.bind('<<ListboxSelect>>', sel_mn)

    Label(st, text='Enter Medicine Name: ').grid(row=1, column=0)
    Label(st, text='Enter changed Value of: ').grid(row=2, column=0)
    att = Spinbox(st, values=col_n)
    att.grid(row=2, column=1)
    up = Entry(st)
    up.grid(row=2, column=2)
    Button(st, width=10, text='Submit', bg='green', fg='white', command=save_mod).grid(row=2, column=4)
    Button(st, width=10, text='Reset', bg='red', fg='white', command=res).grid(row=2, column=5)
    Button(st, width=10, text='Show data', bg='blue', fg='white', command=show_val).grid(row=1, column=4)
    Label(st, text='-' * 120).grid(row=3, column=0, columnspan=6)
    Button(st, width=10, text='Main Menu', bg='green', fg='white', command=main_menu).grid(row=5, column=5)
    st.mainloop()
