"""This is an address book app
    using the tkinter package
"""
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Address Book")
root.config(background="#242325")

label = tk.Label(root, text="CONTACTS", font="Helvetica 24 bold", fg="white", background="#343435")
label.pack(side="top", fill="x")


root.mainloop()
