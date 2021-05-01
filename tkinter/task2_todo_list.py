import tkinter as tk
from tkinter import ttk

class ToDoItem(tk.Frame):
    def __init__(self, parent, str_input, count):
        super().__init__(parent)
        self.todoitem = ttk.Label(parent, text=str_input)
        self.todoitem.grid(row = count+1, column = 1)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To Do App")
        self.resizable(width=False, height=True)
        self.geometry("400x80")
        self.todo_count = 0

        self.my_entry_label = tk.Label(text="To do:")
        self.my_entry_label.grid(row = 0, column = 0, padx = 5, pady= 5)
        self.my_entry = tk.Entry(self, width = 20)
        self.my_entry.grid(row = 0, column = 1, pady = 5)
        
        self.Button = tk.Button(self, text = "Enter", command = self.retrieve)
        self.Button.grid(row = 0, column = 2, padx = 5, pady = 5)

        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(row = 1, column = 1)
    
    def retrieve(self):
        ToDoItem(self, self.my_entry.get(), self.todo_count)
        self.todo_count += 1

        

if __name__ == "__main__":
    app = Application()
    app.mainloop()
 