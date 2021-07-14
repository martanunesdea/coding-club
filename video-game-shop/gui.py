import tkinter as tk
from functools import partial
from tkinter import ttk
from shop import *

class Application(tk.Tk):
    def __init__(self, cart, products):
        super().__init__()
        # Initialise Tk attributes
        self.title("Video game shop")
        self.geometry("400x200")

        # Initialise custom attributes
        self.cart = cart
        self.products = products

        # Display products
        self.display_products()

        # Load checkout button
        self.load_checkout_btn()
        
    def display_products(self):
        # Iterate through Products, add Label and Button per Product
        label_list = []
        button_list = []
        for product in self.products:
            label = ttk.Label(self, text = product.name)
            button = ttk.Button(self, text = "Add to Cart", command = partial(self.add_to_cart, product))

            label.grid(row=1, column=product.id, padx=5, pady=5)
            button.grid(row=2, column=product.id, padx=5, pady=5)

            label_list.append(label)
            button_list.append(button)
        
        # Notification label
        self.label1 = tk.StringVar()
        self.label1.set("")
        self.status_label = tk.Label(self, textvariable=self.label1)
        self.status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    def load_checkout_btn(self):
        self.checkout_btn = ttk.Button(self, text = "Checkout", command = lambda: self.create_checkout_window())
        self.checkout_btn.grid(row=0, column=2, padx=5, pady=5)

    def create_checkout_window(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("Checkout")
        newWindow.geometry("200x200")

        row_available = 0
        for item in self.cart.items:
            label = tk.Label(newWindow, text=item.name)
            label.grid(row=row_available, column=0, padx=5, pady=5)
            row_available += 1
        
        row_available += 1
        # User entry: name, email, bank details
        name_label = tk.Label(newWindow, text="Name: ")
        name_label.grid(row=row_available, column=0, padx=5, pady=5)
        name = tk.Entry(newWindow, text="Name", width=10)
        name.grid(row=row_available, column=1, padx=5, pady=5)

        row_available += 1
        email_label = tk.Label(newWindow, text="Email: ")
        email_label.grid(row=row_available, column=0, padx=5, pady=5)
        email = tk.Entry(newWindow, text="Email", width=10)
        email.grid(row=row_available, column=1, padx=5, pady=5)

        # Confirm
        row_available += 1
        confirm = tk.Button(newWindow, text="Confirm", command=self.confirm_checkout())
        confirm.grid(row=row_available, column=0, padx=5, pady=5)

        return newWindow

    # using self.cart will update on other class methods.
    def add_to_cart(self, product):
        if self.cart.add(product) == True:
            self.label1.set(f'Added item {product.id} to cart')

    def remove_from_cart(self, id):
        return True

    def checkout(self):
        self.create_checkout_window()

    def confirm_checkout(self):
        result = self.cart.checkout()
        print(result)


def main():
    cart = ShoppingCart()
    p1 = Product(0, "sample1")
    p2 = Product(1, "sample2")
    p3 = Product(2, "sample3")

    products = [p1, p2, p3]
    app = Application(cart, products)
    app.mainloop()
    
if __name__ == "__main__": main()



