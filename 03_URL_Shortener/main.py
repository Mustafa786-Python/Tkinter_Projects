import tkinter as tk
from tkinter import messagebox
import pyshorteners


def shorten_link(event=None):
    long_url = long_url_entry.get().strip()
    short_url_entry.delete(0, tk.END)

    if long_url == "":
        messagebox.showwarning("Warning", "The short link box is empty")
        return

    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    short_url_entry.insert(0, short_url)


def copy_command():
    short_url = short_url_entry.get().strip()

    if short_url == "":
        messagebox.showwarning("Empty Url", "Invalid Your!. The box is empty")
        return

    root.clipboard_clear()
    root.clipboard_append(short_url)
    messagebox.showinfo("Clipboard Notificatio", "The link copied")
    root.update()


def next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"


root = tk.Tk()
root.title("Link Shortener")
root.geometry("450x320")
root.configure(bg="#00539C")

# Widgets
long_url_label = tk.Label(root, text="Long Url Shortner",
                          bg="#00539C", fg="#FFFFFF", font=("Courier New", 16))
long_url_entry = tk.Entry(root, font=("Courier New", 16))
short_url_label = tk.Label(root, text="Short Url Shortner",
                           bg="#00539C", fg="#FFFFFF", font=("Courier New", 16))
short_url_entry = tk.Entry(root, font=("Courier New", 16))

long_url_entry.bind("<Return>", next_widget)


shorten_url_button = tk.Button(root, text="Link Shorten", bg="#00539C", fg="#FFFFFF", font=(
    "Courier New", 16), command=shorten_link)
copy_button = tk.Button(root, text="Copy Text", bg="#00539C",
                        fg="#FFFFFF", font=("Courier New", 16), command=copy_command)

# Placement
long_url_label.pack(pady=10)
long_url_entry.pack(pady=10, fill="x")
short_url_label.pack(pady=10)
short_url_entry.pack(pady=10, fill="x")
shorten_url_button.pack(pady=10)
copy_button.pack(pady=10)
tk.mainloop()
