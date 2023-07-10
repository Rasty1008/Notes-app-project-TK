#importing required packages and Libraries

import re
from tkinter import *
from tkinter.ttk import * 
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog, simpledialog
from tkinter.scrolledtext import ScrolledText

#the root widget

root = Tk()
root.title("DataFlair Notepad")
root.resizable(0, 0)

#creating scrollable notepad window

notepad = ScrolledText(root, width = 90, height = 40)
file_name = " "

#defining functions for commands

def cmd_new(): #file menu new option
    global file_name
    if len(notepad.get("1.0", END+"-1c")) > 0:
        if messagebox.askyesno("Notepad", "Do you want to save changes?"):
            cmd_save()
        else:
            notepad.delete(0.0, END)
    root.title("Notepad")

def cmd_open(): #file menu open option
    fd = filedialog.askopenfile(parent = root, mode = "r")
    t = fd.read() #t  is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)

def cmd_save(): #file menu save option
    fd = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt")
    if fd != None:
        data = notepad.get("1.0", END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title = "Error", message = "Not able to save file!")

def cmd_save_as(): #file menu save as option 
    fd = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt")
    t = notepad.get(0.0, END) #t stands for the text gotten from notepad
    try:
        fd.write(t.rstrip())
    except: 
        messagebox.showerror(title = "Error", message = "Not able to save file!")

def cmd_exit(): # file menu Exit option
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()

def cmd_cut(): #edit menu Cut option
    notepad.event_generate("<<Cut>>")

def cmd_copy(): #edit copy option
    notepad.event_generate("<<Copy>>")

def cmd_paste(): #edit paste option
    notepad.event_generate("<<Paste>>")

def cmd_clear(): #edit clear option 
    notepad.event_generate("<<Clear>>")

def cmd_find(): #edit find option 
    notepad.tag_remove("Found", "1.0", END)
    find = simpledialog.askstring("Find", "Find what:")
    if find:
        idx = "1.0" #idx stands for index
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        lastidx = "%s+%dc" %(idx, len(find))
        notepad.tag_add("Found", idx, lastidx)
        idx = lastidx
    notepad.tag_config("Found", foreground = "white", background = "blue")
    notepad.bind("<1>", click)

def click(): #handling click event
    notepad.tag_config("Found", background = "white", foreground = "black")
    
def cmd_select_all(): #edit menu select all option 
    notepad.event_generate("<<Select>>")

def cmd_time_date(): #edit menu Time/Date option
    now = datetime.now()
    #dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Time/Date", dt_string)

def cmd_about(): #help menu about option
    label = messagebox.showinfo("About Notepad", "Notepad by - \nDataFlair")


#Add commands
#notepad menu items

notepad_menu = Menu(root)
root.configure(menu = notepad_menu)

#file menu
file_menu = Menu(notepad_menu, tearoff = False)
notepad_menu.add_cascade(label = "File", menu = file_menu)

#adding options in file menu
file_menu.add_command(label = "New", command = cmd_new)
file_menu.add_command(label = "Open...", command = cmd_open)
file_menu.add_command(label = "Save", command = cmd_save)
file_menu.add_command(label = "Save as...", command = cmd_save_as)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = cmd_exit)

#edit menu
edit_menu = Menu(notepad_menu, tearoff = False)
notepad_menu.add_cascade(label = "Edit", menu = edit_menu)

#adding options in edit menu
edit_menu.add_command(label = "Cut", command = cmd_cut)
edit_menu.add_command(label = "Copy", command = cmd_copy)
edit_menu.add_command(label = "Paste", command = cmd_paste)
edit_menu.add_command(label = "Delete", command = cmd_clear)
edit_menu.add_separator()
edit_menu.add_command(label = "Find", command = cmd_find)
edit_menu.add_separator()
edit_menu.add_command(label = "Select All", command = cmd_select_all)
edit_menu.add_command(label = "Time/Date", command = cmd_time_date)

#help menu
help_menu = Menu(notepad_menu, tearoff = False)
notepad_menu.add_cascade(label = "Help", menu = help_menu)

#adding options in help menu
help_menu.add_command(label = "About Notepad", command = cmd_about)

notepad.pack()
root.mainloop()
