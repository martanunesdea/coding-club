# getting user input
import tkinter as tk

# a window is an instance of Tkinter’s Tk class
# Create a new window and assign it to the variable window:
window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")

greeting.pack()

button = tk.Button(
    text="Click me!",
    width=5,
    height=2,
    bg="blue",   # bg: background colour
    fg="yellow", # fg: background colour
)

button.pack()

label = tk.Label(text="What's your name?")
entry = tk.Entry(fg="black", bg="white", width=50)

label.pack()
entry.pack()

window.mainloop()

