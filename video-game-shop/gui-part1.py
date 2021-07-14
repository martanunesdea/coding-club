import tkinter as tk
from functools import partial
from tkinter import ttk
from shop import *

class Application(tk.Tk):
    def __init__(self, cart):
        super().__init__()
        # Initialise Tk attributes
        self.title("Video game shop")
        self.geometry("400x200")

        # Initialise custom attributes
        self.cart = cart

        # Load products
        self.load_products()

        # Load checkout button
        self.load_buttons()
        
    def load_products(self):
        self.item1 = ttk.Label(self, text = "Game n. 2")
        self.item1.grid(row=1, column=1, padx=5, pady=5)
        
        self.label1 = tk.StringVar()
        self.label1.set("")
        self.status_label = tk.Label(self, textvariable=self.label1)
        self.status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)


    def load_buttons(self):
        self.checkout_btn = ttk.Button(self, text = "Checkout", command = lambda: self.checkout())
        self.checkout_btn.grid(row=0, column=2, padx=5, pady=5)

    # using self.cart will update on other class methods.
    def add_to_cart(self, product):
        if self.cart.add(product) == True:
            self.label1.set(f'Added item {product.id} to cart')


    def checkout(self):
        return True


def main():
    cart = ShoppingCart()
    p1 = Product(0, "sample1")
    app = Application(cart)
    app.mainloop()
    
if __name__ == "__main__": main()



