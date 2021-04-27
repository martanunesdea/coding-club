# button
import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")

greeting.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",   # bg: background colour
    fg="yellow", # fg: background colour
)

button.pack()
window.mainloop()

