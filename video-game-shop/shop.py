

class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.price = 0
        self.quantity = 0

    def buy(self):
        self.quantity -= 1
        # add_to_cart

    def check_availability(self):
        return (self.quantity > 0)
    

class ShoppingCart:
    def __init__(self):
        self.cart_id = 0
        self.total_items = 0
        self.total_price = 0
        self.items = []
    
    def checkout(self):
        return True

    def add(self, product):
        self.items.append(product)
        self.total_items += 1
        return True
    
    def save_for_later(self):
        # store somewhere
        pass


class BankDetails:
    def __init__(self):
        self.name
        self.email
        self.address
    
    def validate(self):
        pass

    def pay(self):
        pass


def main():
    p1 = Product()
    p2 = Product()

    cart = ShoppingCart()
    cart.add(p1)
    cart.add(p2)
    cart.checkout()
    


if __name__ == "__main__": main()