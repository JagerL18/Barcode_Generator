from barcode import Code128
from barcode.writer import ImageWriter
import tkinter as tk
from tkinter import PhotoImage, StringVar
from tkinter import Entry
from tkinter import ttk
import os
from matplotlib import image

save_path = "/Users/lukasjagerneu/Desktop/Barcodes"


#Daten eingeben
def barcode_generation():

    username = str(username_entry.get())
    password = str(password_entry.get())
    barcodename = str(barcodename_entry.get())

    my_code = Code128(username + ' ' + password, writer=ImageWriter())

    complete_filepath = os.path.join(save_path, barcodename)

    my_code.save(complete_filepath)

#UI erstellen
user_input = tk.Tk()
label_01 = tk.Label(user_input, text="Barcode Generator")

label_username = tk.Label(user_input,text="Username")
label_username.pack()

username = tk.StringVar()
username_entry = ttk.Entry(user_input, textvariable=username)
username_entry.pack()

label_password = tk.Label(user_input,text="Password")
label_password.pack()

password = tk.StringVar()
password_entry = ttk.Entry(user_input,textvariable=password)
password_entry.pack()

label_barcode = tk.Label(user_input,text="Barcode")
label_barcode.pack()

barcodename= tk.StringVar()
barcodename_entry = ttk.Entry(user_input, textvariable=barcodename)
barcodename_entry.pack()

start_generation = tk.Button(label_01, text= 'Generate', command=lambda:barcode_generation())

label_01.pack()
start_generation.pack()

user_input.mainloop()
