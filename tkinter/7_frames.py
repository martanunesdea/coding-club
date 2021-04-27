import tkinter as tk
 
window = tk.Tk()
window.geometry("300x200")

top_frame = tk.Frame(window, bg = "orange", bd = 4) # bd:  border size
top_frame.pack()

left_frame = tk.Frame(window, bg = "yellow", bd = 2)
left_frame.pack(side=tk.LEFT)
 
right_frame = tk.Frame(window, bg = "green", bd = 2)
right_frame.pack(side=tk.RIGHT)
 
label = tk.Label(top_frame, text = "Welcome!")
label.pack()
 
button1 = tk.Button(left_frame, text = "Button 1")
button2 = tk.Button(right_frame, text = "Button 2")
button3 = tk.Button(left_frame, text = "Button 3")
 
button1.pack(padx = 3, pady = 3)
button2.pack(padx = 3, pady = 3)
button3.pack(padx = 3, pady = 3)

window.title("Frames")
window.mainloop()