"""This is an address book app
    using the tkinter package
"""
import tkinter as tk

BGCOLOR = "black"
BORDERCLR = "white"
ENTRYBORDER = "#6B6767"

root = tk.Tk()
root.geometry("500x800")
root.title("Address Book")
root.config(background=BGCOLOR)

data = []

# variable to hold the name
Name = tk.StringVar()
# variable to hold the number
Number = tk.StringVar()

def add_contact():
    """ add new contact to contact list """
    if(Name.get() != "" and Number.get() != ""):
        data.append([Name.get(), Number.get()])
        update_contacts()
        clear()

def update_contacts():
    """update the contact list"""
    select.delete(0, "end")
    for name, number in data:
        select.insert("end", "  "+name+"  -  "+number)

def create_title(name, frame):
    """ create a title """
    title = tk.Label(frame, text=name,
                 font="chiller 18 bold",fg="white", background="black")
    title.pack(fill="x", ipady=10)

def delete_contact():
    """ remove contact from contact list"""
    if select.curselection():
        del data[int(select.curselection()[0])]
        update_contacts()

def delete_all_contact():
    """deletes all contact"""
    data.clear()
    update_contacts()

def clear():
    """clear the new contact fields"""
    Name.set("")
    Number.set("")

# Frame to hold new contact and add new contact to list
newContactFrame = tk.Frame(root, background=BGCOLOR,
                    highlightbackground=BORDERCLR, highlightthickness=1)

# title for new contact frame
create_title("New Contact", newContactFrame)

# name frame for entering name variable
nameFrame = tk.Frame(newContactFrame, background=BGCOLOR, pady=10, padx=10)
tk.Label(nameFrame, text="Name:", font="chiller 14 bold", fg="#6B6767",
         background=BGCOLOR).pack(side="left")
tk.Entry(nameFrame, textvariable= Name, font="14", foreground="white",
         background="black", insertbackground="white",
          highlightbackground=ENTRYBORDER, highlightthickness=1).pack(fill="x", ipady=5)
nameFrame.pack(fill="x")

# telephone frame for entering number variable
telophoneFrame = tk.Frame(newContactFrame, background=BGCOLOR, padx=10)
tk.Label(telophoneFrame, text="Telephone:", font="chiller 14",
         background=BGCOLOR, fg="#6B6767").pack(side="left")
tk.Entry(telophoneFrame, textvariable= Number, font="14", foreground="white",
         background="black", insertbackground="white",
         highlightbackground=ENTRYBORDER, highlightthickness=1).pack(fill="x", ipady=5)
telophoneFrame.pack(fill="x", pady=10)

# button to save contacts
buttonFrame = tk.Frame(newContactFrame, bg=BGCOLOR)
tk.Button(buttonFrame, text="Add", font="chiller 14 bold",fg="white",
          border=0, background="#2545D5", command=add_contact,
          activebackground="#1E39B1", activeforeground="white").pack(ipadx=20)
buttonFrame.pack(fill="x", padx=40, pady=10)

newContactFrame.pack( fill="x", padx=30, pady=10)

# Display the contact list
contactListFrame = tk.Frame(root, background=BGCOLOR,
                    highlightbackground=BORDERCLR, highlightthickness=1)

create_title("My Contacts", contactListFrame)

scroller = tk.Scrollbar(contactListFrame, orient="vertical", border=0)
select = tk.Listbox(contactListFrame, yscrollcommand=scroller.set, height=12,
                    activestyle="none", selectbackground="#212020", border=0,
                    font="consolas 14", foreground="white", background=BGCOLOR)
scroller.config(command=select.yview)
scroller.pack(side="right", fill="y")
select.pack(fill="x", ipadx=10, ipady=10)

# contact list actions
actionButtonFrame = tk.Frame(contactListFrame, bg=BGCOLOR)
tk.Button(actionButtonFrame, text="DELETE", font="chiller 14 bold",fg="white",
          activebackground="#A02929", activeforeground="white",
          command=delete_contact, border=0, background="#BC4C4C").pack(ipadx=20, fill="x")
tk.Button(actionButtonFrame, text="DELETE ALL", font="chiller 14 bold",fg="white",
          activebackground="#A02929", activeforeground="white",
          command=delete_all_contact, border=0, background="#BC2F2F").pack(ipadx=20, fill="x")
buttonFrame.pack(pady=10)
actionButtonFrame.pack(fill="x",)

contactListFrame.pack(fill="x", padx=30, pady=10)

root.mainloop()
