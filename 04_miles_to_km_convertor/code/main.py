import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Convetor")
window.geometry("350x300")
window.configure()


"-------------------------------------Frame 1----------------------------------------------"


'-----Functions-----------'


def miles_convert(event=None):
    miles_entry = entry.get()

    if miles_entry == "":
        messagebox.showwarning("warning", "The box is empty")
        return

    try:
        miles_entry = float(miles_entry)
    except ValueError:
        messagebox.showwarning("Warning", "Invalid Input")
        entry.delete(0, tk.END)
        return

    # Calculations
    km_output = miles_entry * 1.66
    output_string.set(f"{round(km_output, 3)} km")

    entry.focus_set()


'-------------------------'

# title
title = ttk.Label(master=window, text="Miles to Kilometer",
                  font="Calibri 24 bold", foreground="#004EAD")

# creating frame
frame1 = tk.Frame(master=window)
frame1.configure()

# Entries
entry = ttk.Entry(frame1, foreground="#004EAD")
mile = tk.Label(frame1, text="mi", foreground="#004EAD",)


style1 = ttk.Style()
style1.configure("My.TLabel", foreground="#ffffff", background="#004EAD")

# keybinding
entry.bind("<Return>", miles_convert)

# button
con_button = ttk.Button(frame1, text="Convert",
                        style="My.TLabel", command=miles_convert)

# placing
title.pack(pady=10)
entry.pack(side="left")
mile.pack(side="left")
con_button.pack(side="left", padx=10)
frame1.pack()

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font="Calibri 24 bold",
                         textvariable=output_string, foreground="#004EAD")
output_label.pack(pady=10)

"-------------------------------------Frame 2----------------------------------------------"


'-----Functions-----------'


def km_convert(event=None):
    km_entry = entry_2.get()

    if km_entry == "":
        messagebox.showwarning("warning", "The box is empty")
        return

    try:
        km_entry = float(km_entry)
    except ValueError:
        messagebox.showwarning("Warning", "Invalid Input")
        entry.delete(0, tk.END)
        return

    # Calculations
    miles_output = km_entry * (1/1.66)
    output_string_2.set(f"{round(miles_output, 3)} mi")

    entry_2.focus_set()


'-------------------------'

# title
title_2 = ttk.Label(master=window, text="Miles to Kilometer",
                  font="Calibri 24 bold", foreground="#004EAD")

# creating frame
frame2 = tk.Frame(master=window)
frame2.configure()

# Entries
entry_2 = ttk.Entry(frame2, foreground="#004EAD")
km = tk.Label(frame2, text="km", foreground="#004EAD",)


# style1 = ttk.Style()
# style1.configure("My.TLabel", foreground="#ffffff", background="#004EAD")

# keybinding
entry_2.bind("<Return>", km_convert)

# button
con_button_2 = ttk.Button(frame2, text="Convert",
                        style="My.TLabel", command=km_convert)

# placing
title_2.pack(pady=10)
entry_2.pack(side="left")
km.pack(side="left")
con_button_2.pack(side="left", padx=10)
frame2.pack()

# Output
output_string_2 = tk.StringVar()
output_label_2 = ttk.Label(master=window, text="Output", font="Calibri 24 bold",
                         textvariable=output_string_2, foreground="#004EAD")
output_label_2.pack(pady=10)


window.mainloop()
