import tkinter as tk
from tkinter import ttk
from datetime import date

class ToDoItem(tk.Frame):
    def __init__(self, parent, str_input, count):
        super().__init__(parent)
        self.is_checked = tk.IntVar()
        self.todo_button = ttk.Checkbutton(parent, text=str_input, variable=self.is_checked, command = lambda: self.kill(parent))
        self.todo_button.grid(row = count, column = 1, pady = 5)
        self.date_created = date.today()
        self.date_text = date.today().strftime("%d%b%Y")
        self.due_date = date.today()

    def is_done(self):
        if self.is_checked.get() == 1:
            return True
        else:
            return False

    def kill(self, parent):
        print("Active items", parent.active_items)
        self.todo_button.destroy()
        parent.update_total_items(1)

    def set_due_date(self):
        self.due_date = date.month("June")

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
        message = self.get_summary_text()

        popup = tk.Tk()
        popup.wm_title("Summary")
        label = ttk.Label(popup, text=message)
        label.grid(row=0, column=0, padx=5, pady=5)
        exit_btn = ttk.Button(popup, text="Exit", command = popup.destroy)
        exit_btn.grid(row=1, column=0, padx=5, pady=5)
        popup.mainloop()

    def get_summary_text(self):
        message = ""
        if self.completed_items > 0:
            message = "You completed " + str(self.completed_items) + " tasks today. Well done!\n"
        else: 
            message = "Tomorrow will be a better day :)\n"
        if self.active_items > 0:
            message = message + "You have " +  str(self.active_items) + " tasks to complete tomorrow"
        else:
            message = message + "You smashed it! Enter some new items for tomorrow"
        return message

        


if __name__ == "__main__":
    app = Application()
    app.mainloop()
 