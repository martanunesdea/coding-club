import tkinter as tk

def change_blue():
    label.configure(fg = "blue")

def change_red():
    label.configure(fg = "red")
  
window = tk.Tk()
tk.Button(window, text='Choose Blue',command=change_blue).pack(pady=20)
tk.Button(window, text='Choose Red',command=change_red).pack(pady=20)

label = tk.Label(window, text = "Color", fg = "black")
label.pack()

window.geometry('180x180')
window.mainloop()