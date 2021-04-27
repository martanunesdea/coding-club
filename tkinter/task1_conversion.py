# temperature converter
import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into label_c.
    """
    fahrenheit = entry_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    label_c["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


window = tk.Tk()
window.title("Temperature Converter")

frame_entry = tk.Frame(master=window)
entry_temperature = tk.Entry(master=frame_entry, width=10)
label_f = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")

entry_temperature.grid(row=0, column=0, sticky="e")
label_f.grid(row=0, column=1, sticky="w")

button_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius  # <--- Add this line
)
label_c = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frame_entry.grid(row=0, column=0, padx=10)
button_convert.grid(row=0, column=1, pady=10)
label_c.grid(row=0, column=2, padx=10)

window.mainloop()