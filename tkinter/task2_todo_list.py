import tkinter as tk
from tkinter import ttk


class ToDoItem(tk.Frame):
    def __init__(self, parent, str_input, count):
        super().__init__(parent)
        self.is_checked = tk.IntVar()
        self.todo_button = ttk.Checkbutton(parent, text=str_input, variable=self.is_checked, command = lambda: self.kill(parent))
        self.todo_button.grid(row = count, column = 1, pady = 5)

    def is_done(self):
        if self.is_checked.get() == 1:
            return True
        else:
            return False

    def kill(self, parent):
        print("Active items", parent.active_items)
        self.todo_button.destroy()
        parent.update_total_items(1)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To Do App")
        self.geometry("350x500")
        self.active_items = 0
        self.completed_items = 0
        self.position = 2
        self.todo_collection = []

        self.my_entry_label = tk.Label(text="To do:")
        self.my_entry_label.grid(row = 0, column = 0, padx = 5, pady= 5)
        self.my_entry = tk.Entry(self, width = 20)
        self.my_entry.grid(row = 0, column = 1, pady = 5)
        
        self.button_enter = ttk.Button(self, text = "Enter", command = self.enter)
        self.button_enter.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.button_summary = ttk.Button(self, text = "Summary", command = self.summary)
        self.button_summary.grid(row = 15, column = 1, padx = 5, pady = 5)


    def enter(self):
        self.todo_collection.append(ToDoItem(self, self.my_entry.get(), self.position))
        self.active_items = self.active_items + 1
        self.position += 1
        print(str(len(self.todo_collection)), " active items ", self.active_items)

    def update_total_items(self, number):
        self.active_items = self.active_items - 1
        self.completed_items = self.completed_items + 1

    def summary(self):
        if self.completed_items > 0:
            print("You completed", self.completed_items, "tasks today. Well done!")
        else: 
            print("Tomorrow will be a better day :)")
        if self.active_items > 0:
            print("You have", self.active_items, "tasks to complete tomorrow")
        else:
            print("You smashed it! Enter some new items for tomorrow")

        


if __name__ == "__main__":
    app = Application()
    app.mainloop()
 