# button
import tkinter as tk

# a window is an instance of Tkinter’s Tk class
# Create a new window and assign it to the variable window:
window = tk.Tk()

# Adding a widget to a window
# We'll the tk.Label class to add some text to a window. 
# This creates a Label widget with the text entered in parenthesis
greeting = tk.Label(text="Hello, Tkinter")

# Using the Label's pack() method to add the label to the window
greeting.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

window.mainloop()

