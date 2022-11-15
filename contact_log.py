"""This is an address book app
    using the tkinter package
"""
import tkinter as tk

BGCOLOR = "#343435"
BORDERCLR = "#9999CC"

root = tk.Tk()
root.geometry("500x500")
root.title("Address Book")
root.config(background=BGCOLOR)

data = []

# variable to hold the name
Name = ""
# variable to hold the number
Number = ""


# contactFrame = tk.Frame(root)
# contactFrame.columnconfigure(0, weight=1)
# contactFrame.columnconfigure(1, weight=1)

"""Frame to hold new contact
    and add new contact to list
"""
newContactFrame = tk.Frame(root, background=BGCOLOR,
                    highlightbackground=BORDERCLR, highlightthickness=2)

# title for new contact frame
title = tk.Label(newContactFrame, text="New contact",
                 font="arial 18 bold",fg="white", background=BORDERCLR)
title.pack(fill="x", ipady=10)

# name frame for entering name variable
nameFrame = tk.Frame(newContactFrame, background=BGCOLOR, pady=10, padx=10)
tk.Label(nameFrame, text="Name:", font="arial 14 bold", fg="white",
         background=BGCOLOR).pack(side="left")
tk.Entry(nameFrame, textvariable= Name,
          highlightcolor=BORDERCLR, highlightthickness=2).pack(fill="x", ipady=5)
nameFrame.pack(fill="x")

# telephone frame for entering number variable
telophoneFrame = tk.Frame(newContactFrame, background=BGCOLOR, padx=10)
tk.Label(telophoneFrame, text="Telephone:", font="arial 14 bold",
         background=BGCOLOR, fg="white").pack(side="left")
tk.Entry(telophoneFrame, textvariable= Number,
         highlightcolor=BORDERCLR, highlightthickness=2).pack(fill="x", ipady=5)
telophoneFrame.pack(fill="x", pady=10)

# button to save contacts
buttonFrame = tk.Frame(newContactFrame, bg=BGCOLOR)
tk.Button(buttonFrame, text="ADD", font="arial 14 bold",fg="white", background="#9999CC").pack(ipadx=20)
buttonFrame.pack(fill="x", padx=40, pady=10)

newContactFrame.pack( fill="x", padx=30, pady=10)
# savedFrame = tk.Frame(contactFrame, background=BGCOLOR,
#                       highlightbackground=BGCOLOR, highlightthickness=2)
# savedFrame.grid(column=1, row=0, sticky=tk.W+tk.E)
# savedContacts = tk.Label(savedFrame, text="Saved contacts", font="arial 14",
#                          fg="white", background=BGCOLOR)
# savedContacts.pack()

# contactFrame.pack(fill="x")

root.mainloop()
