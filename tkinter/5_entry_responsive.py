# enter your name
import tkinter as tk

def retrieve():
    text = entry_text1.get()
    label_response["text"] = f"Nice to meet you, {text}"


window = tk.Tk()
window.title("Hello")

label_text1 = tk.Label(text="Your name")
entry_text1 = tk.Entry(width=10)

label_text1.pack()
entry_text1.pack()

button_enter = tk.Button(
    text="Enter",
    command=button_press
)
label_response = tk.Label()

button_enter.pack()
label_response.pack()

window.mainloop()