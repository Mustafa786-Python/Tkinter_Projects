import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Login Form")
root.geometry("350x440")
root.configure(bg="#02343F")

# Creating Frame
frame = tk.Frame(root)
frame.configure(bg="#02343F")
frame.pack()


#creating command
def login(event = None):
    username = "mustafa"
    password = "12345677"

    if user_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title= "Login Sucess", message= "Login has been succesfull")
    else:
        messagebox.showinfo(title= "Invalid Login", message= "Login unsuccessful")

    user_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
        
    user_entry.focus_set()

def next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"


# widgets
login_label = tk.Label(frame, text="Login", font=(
    "Arial", 30), bg="#02343F", fg="#F0EDCC")
user_label = tk.Label(frame, text="Username", font=(
    "Arial", 16), bg="#02343F", fg="#F0EDCC")
password_label = tk.Label(frame, text="Password", font=(
    "Arial", 16), bg="#02343F", fg="#F0EDCC")
user_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))


user_entry.bind("<Return>", next_widget)
password_entry.bind("<Return>", login)


login_button = tk.Button(frame, text="Login", font=(
    "Arial", 30), bg="#D4A017", fg="#F0EDCC", command= login)

# login_button.bind("<Return>", login)


# Widegets placement
login_label.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=20)
user_label.grid(row=1, column=0, pady=10)
password_label.grid(row=2, column=0, pady=10)
user_entry.grid(row=1, column=1, pady=10)
password_entry.grid(row=2, column=1, pady=10)
login_button.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=10)

root.mainloop()
