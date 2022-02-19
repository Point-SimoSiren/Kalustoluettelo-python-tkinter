from concurrent.futures import process
from tkinter import *
from tkinter import messagebox
from db import Database

db = Database("tools.db")

def get_item_list():
    tool_list.delete(0, END)
    for row in db.fetch():
        tool_list.insert(END, row)
        
def clear_fields():
    print('clr')

def remove():
    print('removed')

def add_new():
    if tool_text.get() == '':
        messagebox.showerror('Virhe', 'Tavaran nimi on pakollinen tieto.')
    else:
        db.insert(tool_text.get(), price_text.get(), time_text.get(), shop_text.get(), borrow_text.get(), btime_text.get())
        get_item_list()

def edit():
    print('updated')

app = Tk()
app.title('Kalustoluettelo')
app.geometry('650x550')


### Tavaralista ###
tool_list = Listbox(app, width=100, height=20, border=1)
tool_list.grid(column=0, row=0, columnspan=5, rowspan=6, pady=20, padx=10)

scrollbar = Scrollbar(app)
scrollbar.grid(row=0, column=5)

tool_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command=tool_list.yview)


### Napit ###
#Syötekenttien tyhjennys
clr_btn = Button(app, text='Tyhjennä kentät', width=12, command=clear_fields)
clr_btn.grid(row=12, column=1)

add_btn = Button(app, text='Luo uusi', width=12, command=add_new)
add_btn.grid(row=12, column=2)

edit_btn = Button(app, text='Tallenna', width=12, command=edit)
edit_btn.grid(row=12, column=3)

remove_btn = Button(app, text='Poista', width=12, command=remove)
remove_btn.grid(row=12, column=0)

separator = Label(app, text='____________________________________________________', font=('bold', 14), pady=10)
separator.grid(row=11, column=0, columnspan=5)


### Syötekentät ###

# Tavara
tool_text = StringVar()
tool_label = Label(app, text='Tavara', font=('bold', 14), pady=5)
tool_label.grid(row=7, column=0, sticky=W)
tool_entry = Entry(app, textvariable=tool_text)
tool_entry.grid(row=8, column=0, sticky=W)

# Hankintahinta
price_text = StringVar()
price_label = Label(app, text='Hankintahinta', font=('bold', 14), pady=5)
price_label.grid(row=7, column=1, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=8, column=1, sticky=W)

# Hankinta-ajankohta
time_text = StringVar()
time_label = Label(app, text='Hankinta-aika', font=('bold', 14), pady=5)
time_label.grid(row=7, column=2, sticky=W)
time_entry = Entry(app, textvariable=time_text)
time_entry.grid(row=8, column=2, sticky=W)

# Hankintapaikka
shop_text = StringVar()
shop_label = Label(app, text='Hankintapaikka', font=('bold', 14), pady=5)
shop_label.grid(row=7, column=3, sticky=W)
shop_entry = Entry(app, textvariable=shop_text)
shop_entry.grid(row=8, column=3, sticky=W)

# Kenellä nyt lainassa / ei lainassa
borrow_text = StringVar()
borrow_label = Label(app, text='Lainaaja', font=('bold', 14), pady=5)
borrow_label.grid(row=9, column=0, sticky=W)
borrow_entry = Entry(app, textvariable=borrow_text)
borrow_entry.grid(row=10, column=0, sticky=W)

# Lainausajankohta
btime_text = StringVar()
btime_label = Label(app, text='Laina alkanut', font=('bold', 14), pady=5)
btime_label.grid(row=9, column=1, sticky=W)
btime_entry = Entry(app, textvariable=btime_text)
btime_entry.grid(row=10, column=1, sticky=W)

### Start app  ###
get_item_list()
app.mainloop()
