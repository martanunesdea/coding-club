# getting user input
import tkinter as tk

# a window is an instance of Tkinter’s Tk class
# Create a new window and assign it to the variable window:
window = tk.Tk()

label = tk.Label(text="Name")
entry = tk.Entry(fg="yellow", bg="blue", width=50)

label.pack()
entry.pack()

window.mainloop()
name = entry.get()
print(name)
