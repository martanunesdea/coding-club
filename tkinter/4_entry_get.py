# getting user input
import tkinter as tk

def retrieve():
    print(entry.get())
 
window = tk.Tk()
window.geometry("200x100")

label = tk.Label(text="What's your name?")
entry = tk.Entry(fg="black", bg="white", width=50)

button = tk.Button(window, text = "Submit", command = retrieve)

label.pack()
entry.pack()
button.pack(padx = 5, pady = 5)

window.mainloop()

