from tkinter import *

app = Tk()
app.title('Kalustoluettelo')
app.geometry('800x500')

# Tavara
tool_text = StringVar()
tool_label = Label(app, text='Tavara', font=('bold', 14), pady=5)
tool_label.grid(row=0, column=0, sticky=W)
tool_entry = Entry(app, textvariable=tool_text)
tool_entry.grid(row=1, column=0)

# Hankintahinta
price_text = StringVar()
price_label = Label(app, text='Hankintahinta', font=('bold', 14), pady=5)
price_label.grid(row=2, column=0, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=3, column=0)

# Hankinta-ajankohta
time_text = StringVar()
time_label = Label(app, text='Hankinta-aika', font=('bold', 14), pady=5)
time_label.grid(row=4, column=0, sticky=W)
time_entry = Entry(app, textvariable=time_text)
time_entry.grid(row=5, column=0)

# Hankintapaikka
shop_text = StringVar()
shop_label = Label(app, text='Hankintapaikka', font=('bold', 14), pady=5)
shop_label.grid(row=6, column=0, sticky=W)
shop_entry = Entry(app, textvariable=shop_text)
shop_entry.grid(row=7, column=0)

# Kenellä nyt lainassa / ei lainassa
borrow_text = StringVar()
borrow_label = Label(app, text='Lainaaja', font=('bold', 14), pady=5)
borrow_label.grid(row=8, column=0, sticky=W)
borrow_entry = Entry(app, textvariable=borrow_text)
borrow_entry.grid(row=9, column=0)

# Lainausajankohta
btime_text = StringVar()
btime_label = Label(app, text='Laina alkanut', font=('bold', 14), pady=5)
btime_label.grid(row=10, column=0, sticky=W)
btime_entry = Entry(app, textvariable=btime_text)
btime_entry.grid(row=11, column=0)

# Start app
app.mainloop()
