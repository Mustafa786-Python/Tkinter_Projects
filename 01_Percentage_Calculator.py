import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox

# Creating Root window
root = tk.Tk()
root.title("Percentage Calulator")
root.geometry("600x600")


"-------------------------  Frame   -----------------------------"
frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# name label
name_label = tk.Label(frame, text=" Name :   ")
name_label.grid(row=0, column=0, pady=10, padx=10)

# name input
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, sticky="ew", columnspan=2, pady=10, padx=10)

# total mark label
total_label = tk.Label(frame, text="    Total Marks :   ")
total_label.grid(row=0, column=3, pady=10, padx=10)

# total mark input
total_entry = tk.Entry(frame)
total_entry.grid(row=0, column=4, sticky="ew", columnspan=2, pady=10, padx=10)

# Subject Label
name_label = tk.Label(frame, text=" Subjects :   ")
name_label.grid(row=1, column=0, pady=10, padx=10)

"-----  Subjects labels ----------"
# Maths
math_label = tk.Label(frame, text=" Physics  ")
math_label.grid(row=1, column=1, columnspan=2)

# physics
physics_label = tk.Label(frame, text=" Maths   ")
physics_label.grid(row=1, column=3, columnspan=2)

# Computer
computer_label = tk.Label(frame, text=" Computer ")
computer_label.grid(row=1, column=5, columnspan=2)

"-----  Subjects Entries ----------"
# Maths
math_entry = tk.Entry(frame)
math_entry.grid(row=2, column=1, sticky="ew", columnspan=2)

# physics
physics_entry = tk.Entry(frame)
physics_entry.grid(row=2, column=3, sticky="ew", columnspan=2)

# Computer
computer_entry = tk.Entry(frame)
computer_entry.grid(row=2, column=5, sticky="ew", columnspan=2)


"---------Creating Table---------"
columns = ("name", "p%")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("name", text="Name")
tree.heading("p%", text="Percentage")
tree.grid(row=3, column=1, columnspan=7, pady=10, sticky="nsew")

"------------Making Function-----------------"
# back function


def entry_delete(event):
    event.widget.tkfocusPrev().focus()
    return "break"

# next function


def next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"


def add_item(event=None):
    name = name_entry.get()
    t_marks = total_entry.get()
    math = math_entry.get()
    phy = physics_entry.get()
    com = computer_entry.get()

    if not name or not t_marks or not phy or not com:
        messagebox.showwarning(f"Input Error", "Please fill all labels")
        return

    try:
        t_marks = float(t_marks)
        math = float(math)
        phy = float(phy)
        com = float(com)
    except ValueError:
        messagebox.showwarning(f"Input Error", "Value must be numbers")
        name_entry.delete(0, tk.END)
        total_entry.delete(0, tk.END)
        math_entry.delete(0, tk.END)
        physics_entry.delete(0, tk.END)
        computer_entry.delete(0, tk.END)
        name_entry.focus_set()
        return

    per = ((math + phy + com) / t_marks) * 100

    tree.insert("", tk.END, values=(name.title(), f"{per:3.f}%"))

    # delete all entries
    name_entry.delete(0, tk.END)
    total_entry.delete(0, tk.END)
    math_entry.delete(0, tk.END)
    physics_entry.delete(0, tk.END)
    computer_entry.delete(0, tk.END)

    # Cursor to first entry
    name_entry.focus_set()

    return "break"


def delete_item():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning(f"Selection Error:", "Select an item")

    for item in selected:
        tree.delete(item)

    return "break"


"Keyboard Funtion"
# Enter
name_entry.bind("<Return>", next_widget)
total_entry.bind("<Return>", next_widget)
math_entry.bind("<Return>", next_widget)
physics_entry.bind("<Return>", next_widget)

# Add item
computer_entry.bind("<Return>", add_item)

# back

total_entry.bind("<Tab>", entry_delete)
math_entry.bind("<Tab>", entry_delete)
physics_entry.bind("<Tab>", entry_delete)
computer_entry.bind("<Tab>", entry_delete)

"Add Buttons"
add_btn = tk.Button(frame, text="ADD", command=add_item)
add_btn.grid(row=2, column=7, padx=10)

# delete button
tk.Button(root, text="Delete Selected", command=delete_item).grid(
    row=3, column=0, columnspan=4, pady=5)

root.mainloop()
