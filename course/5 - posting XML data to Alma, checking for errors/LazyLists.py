#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import requests
import configparser
import xmltodict


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
	
    # get item record
    r = requests.get(f"https://api-na.hosted.exlibrisgroup.com/almaws/v1/items?item_barcode={barcode}&apikey={apikey}")
    
    # check for errors
    errors = check_errors(r)
    if errors['exist'] == True:
        gui.msgbox(title="Attention", message=errors['message'])
        gui.update_status(status_top=barcode, status_bottom=errors['message'], 
                          color="red")
        return
		
    # parse item record
    item_xml = r.text
    item_dict = xmltodict.parse(r.text, dict_constructor=dict) 
    
    title = item_dict['item']['bib_data']['title']
    mms_id = item_dict['item']['bib_data']['mms_id']
    holding_id = item_dict['item']['holding_data']['holding_id']
    item_pid = item_dict['item']['item_data']['pid']
	
	
	
#r = post_xml(url=f"https://api-na.hosted.exlibrisgroup.com/almaws/v1/conf/sets/{set_id}?op=add_members&apikey={apikey}", 
#             xml=set_xml)
	
	
# functions ###################################################################
def check_errors(r):
    errors_dict = {}
    
    if r.status_code != 200:
        errors = xmltodict.parse(r.text)
        error = errors['web_service_result']['errorList']['error']['errorMessage']
        errors_dict['exist'] = True
        errors_dict['message'] = error
    else: 
        errors_dict['exist'] = False
        errors_dict['message'] = ""
    
    return errors_dict

def post_xml(url, xml):
    headers = {'Content-Type': 'application/xml', 'charset':'UTF-8'}
    r = requests.post(url, data=xml.encode('utf-8'), headers=headers)
    return r
    
def put_xml(url, xml):
    headers = {'Content-Type': 'application/xml', 'charset':'UTF-8'}
    r = requests.put(url, data=xml.encode('utf-8'), headers=headers)
    return r

def generate_set_xml(set_id, mms_id, holding_id, item_pid, barcode):
    set_xml = \
f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<set link="https://api-na.hosted.exlibrisgroup.com/almaws/v1/conf/sets/{set_id}">
  <id>{set_id}</id>
  <number_of_members link="https://api-na.hosted.exlibrisgroup.com/almaws/v1/conf/sets/{set_id}/members">1</number_of_members>
<members total_record_count="1">
  <member link="https://api-na.hosted.exlibrisgroup.com/almaws/v1/bibs/{mms_id}/holdings/{holding_id}/items/{item_pid}">
    <id>{item_pid}</id>
    <description>{barcode}</description>
  </member>
</members>
</set>"""

    return set_xml
	
        
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