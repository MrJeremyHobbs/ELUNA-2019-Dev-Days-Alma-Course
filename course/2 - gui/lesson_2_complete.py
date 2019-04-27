#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import configparser


# configurations ##############################################################
config = configparser.ConfigParser()
config.read('config.ini')

apikey = config['misc']['apikey']
set_id = config['misc']['set_id']
operating_system = config['misc']['os']


# main program ################################################################
def main(*args):
    # barcode
    barcode = gui.get_entry_field_data()
    gui.clear_entry_field()
	
    
# functions ###################################################################
    
        
# gui #########################################################################
class gui:
    def __init__(self, master):
        self.master = master
        master.title("LazyLists v2.5")
        master.resizable(0, 0)
        master.minsize(width=600, height=100)
        
        # icon file
        if operating_system.upper() == "PC":
            master.iconbitmap("images\\logo_small.ico")
        elif operating_system.upper() == "MAC":
            master.iconbitmap("images//logo_small.icns")
        else:
            gui.msgbox(self, title="Attention", message='OS must be set to "MAC" or "PC" in config.ini')

        # top
        if operating_system.upper() == "PC":
            logo_file = PhotoImage(file="images\\logo_large.png")
        if operating_system.upper() == "MAC":
            logo_file = PhotoImage(file="images//logo_large.pgm")
        
        self.top = Label(image=logo_file)
        self.top.image = logo_file
        self.top.pack()
        
        # status top
        self.status_top = Label(height=1, text="Scan barcode to begin.", 
                                          font="Consolas 12 italic")
        self.status_top.pack(fill="both", side="top")

        # status bottom
        self.status_bottom = Label(height=1, text="READY", 
                                             font="Consolas 12 bold", 
                                             fg="green")
        self.status_bottom.pack(fill="both", side="top")
        
        # entry field
        self.entry_field = Entry(font="Consolas 16")
        self.entry_field.focus()
        self.entry_field.bind('<Key-Return>', main)
        self.entry_field.pack(fill="both", side="top")
        
        # submit button
        self.submit_button = Button(text="SCAN", font="Arial 16", command=main)
        self.submit_button.pack(fill="both", side="top")
        
    def msgbox(self, title, message):
        messagebox.showerror(title=title, message=message)
        
    def get_entry_field_data(self):
        data = self.entry_field.get()
        return data
        
    def clear_entry_field(self):
        self.entry_field.delete(0, END)
        
    def update_status(self, status_top, status_bottom, color):
        self.status_top.config(text=status_top)
        self.status_bottom.config(text=status_bottom, fg=color)

        
# top-level ###################################################################        
root = Tk()
gui = gui(root)
root.mainloop()