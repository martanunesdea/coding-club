import tkinter as tk
from tkinter import ttk

def save_entry(filename):
    text = text_entry.get("1.0", tk.END)
    save_to_file(text, filename)

def save_to_file(text, filename):
    if ".txt" in filename:
        print("file ready")
        pass
    else:
        filename = filename + ".txt"
    f = open(filename, "w+")
    f.write(text)
    f.close()

def load_entry():
    filename = filename_entry.get()
    filename = filename + ".txt"
    try:
        f = open(filename, "r")
        text = f.read()
        set_text_entry(text)
    except:
        set_error_label("Please enter valid filename")

def set_error_label(text):
    error_msg.set(text)

def set_text_entry(text):
    text_entry.delete(1.0,tk.END)
    text_entry.insert(1.0, text)

window = tk.Tk()
window.geometry("520x480")

write_entry_label = tk.Label(window, text = "Start a new entry from blank...");
write_entry_label.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5)

text_entry = tk.Text(window, width = 70)
text_entry.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

save_file_label = tk.Label(window, text = "Save as...");
save_file_label.grid(row = 2, column = 0, padx = 5, pady = 5)

save_file_entry = tk.Entry(window)
save_file_entry.insert(0, "Name of file")
save_file_entry.grid(row = 2, column = 1, padx = 5, pady = 5)

save_button = tk.Button(window, text = "Save", command =lambda:save_entry(save_file_entry.get()))
save_button.grid(row = 2, column = 2, columnspan = 3, padx = 5, pady = 5)

open_file_label = tk.Label(window, text = "Or load existing entry");
open_file_label.grid(row = 3, column = 0, padx = 5, pady = 5)

filename_entry = tk.Entry(window)
filename_entry.insert(0, "Name of file")
filename_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

load_button = tk.Button(window, text = "Open", command = load_entry)
load_button.grid(row = 3, column = 2, padx = 5, pady = 5)

error_msg = tk.StringVar()
error_msg.set("")
error_label = tk.Label(window, textvariable = error_msg)
error_label.grid(row = 4, column = 1, padx = 5, pady = 5)

 
window.mainloop()