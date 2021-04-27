# using .pack() method
import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()
#frame1.pack(fill=tk.X)
# frame1.pack(fill=tk.Y, side=tk.LEFT)
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()
# frame2.pack(fill=tk.X)
# frame2.pack(fill=tk.Y, side=tk.LEFT)
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()
# frame3.pack(fill=tk.X)
# frame3.pack(fill=tk.Y, side=tk.LEFT)
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()




