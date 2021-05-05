import tkinter as tk
from tkinter import ttk
def retrieve():
    user = my_entry.get()
    password = my_entry2.get()
    label1.set(str(user))
 
window = tk.Tk()
window.geometry("200x150")

my_entry = tk.Entry(window, width = 20)
my_entry.insert(0,'Username')
my_entry.pack(padx = 5, pady = 5)
 
label_password = tk.Label(text="Password:")
label_password.pack()
my_entry2 = tk.Entry(window, width = 15)
my_entry2.insert(0,'password')
my_entry2.pack(padx = 5, pady = 5)
 

Button = tk.Button(window, text = "Submit", command = retrieve)
Button.pack(padx = 5, pady = 5)

# status bar
label1 = tk.StringVar()
label1.set("")
labelbar = tk.Label(window, textvariable=label1)
labelbar.pack(padx=10)

 
window.mainloop()