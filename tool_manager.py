from asyncio.windows_events import NULL
import string
from tkinter import *
from tkinter import messagebox
from db import Database

db = Database("tools.db")
global selected_item

def get_item_list():
    tool_list.delete(0, END)
    for row in db.fetch():
        tool_list.insert(END, row)
        
def clear_fields():
    tool_entry.delete(0, END)
    price_entry.delete(0, END)
    time_entry.delete(0, END)
    shop_entry.delete(0, END)
    borrow_entry.delete(0, END)
    btime_entry.delete(0, END)

# Kun listalta valitaan jokin tavara
def select_item(event):
    # Haetaan valitun tavaran tiedot
    global selected_item
    index = tool_list.curselection()[0]
    selected_item = tool_list.get(index)
    
    # Tuodaan valitun tavaran tiedot syöte kenttiin
    clear_fields()
    tool_entry.insert(END, selected_item[1])
    price_entry.insert(END, selected_item[2])
    time_entry.insert(END, selected_item[3])
    shop_entry.insert(END, selected_item[4])
    borrow_entry.insert(END, selected_item[5])
    btime_entry.insert(END, selected_item[6])
        

def remove():
    if messagebox.askokcancel("Poisto", f"Valitse ok jos todella haluat poistaa tavaran: {selected_item[1]}") == True:
        db.remove(selected_item[0])
        clear_fields()
        get_item_list()


def add_new():
    if tool_text.get() == '':
        messagebox.showerror('Virhe', 'Tavaran nimi on pakollinen tieto.')
    else:
        db.insert(tool_text.get(), price_text.get(), time_text.get(), shop_text.get(), borrow_text.get(), btime_text.get())
        clear_fields()
        get_item_list()


def edit():
    db.update(selected_item[0], tool_text.get(), price_text.get(), time_text.get(), shop_text.get(), borrow_text.get(), btime_text.get())
    get_item_list()


### Sovellusikkuna ###
app = Tk()
app.title('Kalustoluettelo')
app.geometry('650x550')


### Tavaralista ###
tool_list = Listbox(app, width=100, height=20, border=1)
tool_list.grid(column=0, row=0, columnspan=5, rowspan=6, pady=20, padx=10)
tool_list.bind('<<ListboxSelect>>', select_item)


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
