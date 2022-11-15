"""This is an address book app
    using the tkinter package
"""
import tkinter as tk

BGCOLOR = "#343435"

root = tk.Tk()
root.geometry("500x500")
root.title("Address Book")
root.config(background=BGCOLOR)

data = []

Name = ""
Number = ""


# contactFrame = tk.Frame(root)
# contactFrame.columnconfigure(0, weight=1)
# contactFrame.columnconfigure(1, weight=1)

addFrame = tk.Frame(root, background=BGCOLOR,
                    highlightbackground="black", highlightthickness=2)

addTitle = tk.Label(addFrame, text="Add contact", font="arial 14",fg="white", background=BGCOLOR)
addTitle.pack(pady=10)

nameFrame = tk.Frame(addFrame, background=BGCOLOR)
tk.Label(nameFrame, text="Name:", font="arial 10 bold", background=BGCOLOR).pack(side="left")
tk.Entry(nameFrame, textvariable= Name,
          highlightcolor="black", highlightthickness=1).pack(fill="x", pady=20, padx=20)
nameFrame.pack(fill="x")
addFrame.pack( fill="x", padx=30, pady=10)

telophoneFrame = tk.Frame(addFrame, background=BGCOLOR)
tk.Label(telophoneFrame, text="Telephone:", font="arial 10 bold", background=BGCOLOR).pack(side="left")
tk.Entry(telophoneFrame, textvariable= Number,
         highlightcolor="black", highlightthickness=1).pack(fill="x", padx=20)
telophoneFrame.pack(fill="x", pady=10)
# savedFrame = tk.Frame(contactFrame, background=BGCOLOR,
#                       highlightbackground=BGCOLOR, highlightthickness=2)
# savedFrame.grid(column=1, row=0, sticky=tk.W+tk.E)
# savedContacts = tk.Label(savedFrame, text="Saved contacts", font="arial 14",
#                          fg="white", background=BGCOLOR)
# savedContacts.pack()

# contactFrame.pack(fill="x")

root.mainloop()
