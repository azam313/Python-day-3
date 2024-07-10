import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Azam" and password == "123":
        messagebox.showinfo("login", "Login successful!")
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")

root = tk.Tk()
root.title("Login Page")
root.geometry("300x150")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
