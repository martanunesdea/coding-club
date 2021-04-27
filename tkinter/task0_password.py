import tkinter as tk
 
def retrieve():
    print(my_entry.get())
    print(my_entry2.get())
 
window = tk.Tk()
window.geometry("200x150")

my_entry = tk.Entry(window, width = 20)
my_entry.insert(0,'Username')
my_entry.pack(padx = 5, pady = 5)
 
my_entry2 = tk.Entry(window, width = 15)
my_entry2.insert(0,'password')
my_entry2.pack(padx = 5, pady = 5)
 
Button = tk.Button(window, text = "Submit", command = retrieve)
Button.pack(padx = 5, pady = 5)
 
window.mainloop()