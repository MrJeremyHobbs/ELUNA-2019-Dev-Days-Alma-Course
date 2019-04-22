#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import configparser
import requests
import xmltodict

# configurations ##############################################################
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['misc']['api_key']
set_id = config['misc']['set_id']


# main program ################################################################
def main(*args):
    # barcode
    barcode = gui.get_barcode()
    if barcode == "":
        gui.msgbox(barcode, "Bad barcode.")
        return
    gui.clear_barcode()
    
    # get item record
    r = requests.get(f"https://api-na.hosted.exlibrisgroup.com/almaws/v1/items?item_barcode={barcode}&apikey={api_key}")
    
    # check for errors
    errors_exist = check_errors(r)
    if errors_exist[0] == True:
        error = errors_exist[1]
        gui.msgbox(barcode, error)
        return
        
# functions ###################################################################
def check_errors(r):
    if r.status_code != 200:
        errors = xmltodict.parse(r.text)
        error = errors['web_service_result']['errorList']['error']['errorMessage']
        return True, error
    else: 
        return False, "OK"


# gui #########################################################################
class gui:
    def __init__(self, master):
        self.master = master
        master.title(f"LazyLists v2.5")
        master.resizable(0, 0)
        master.minsize(width=600, height=100)
        master.iconbitmap("images\\logo_small.ico")

        logo = PhotoImage(file="images\\logo_large.png")
        self.logo = Label(image=logo)
        self.logo.image = logo
        self.logo.pack()

        self.status_title = Label(height=1, text="Scan barcode to begin.", font="Consolas 12 italic")
        self.status_title.pack(fill="both", side="top")

        self.status_added = Label(height=1, text="READY", font="Consolas 12 bold", fg="green")
        self.status_added.pack(fill="both", side="top")

        self.barcode_entry_field = Entry(font="Consolas 16")
        self.barcode_entry_field.focus()
        self.barcode_entry_field.bind('<Key-Return>', main)
        self.barcode_entry_field.pack(fill="both", side="top")
        
        self.scan_button = Button(text="SCAN", font="Arial 16", command=main)
        self.scan_button.pack(fill="both", side="top")
        
    def msgbox(self, title, msg):
        messagebox.showerror("Attention", msg)
        gui.update_status_failure(title, msg)
        
    def get_barcode(self):
        barcode = self.barcode_entry_field.get()
        barcode = barcode.replace(" ", "")
        return barcode
        
    def clear_barcode(self):
        self.barcode_entry_field.delete(0, END)
        self.status_title.config(text="")
        self.status_added.config(text="")
        
    def update_status_success(self, title):
        self.status_title.config(text=title)
        self.status_added.config(text="SUCCESSFULLY ADDED TO SET", fg="green")
        
    def update_status_failure(self, title, msg):
        self.status_title.config(text=title)
        self.status_added.config(text=msg, fg="red")
        
        
# top-level ###################################################################        
root = Tk()
gui = gui(root)
root.mainloop()