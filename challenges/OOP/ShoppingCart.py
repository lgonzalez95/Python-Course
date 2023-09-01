class Order:
    cart = []

    def add_to_cart(self, item):
        Order.cart.append(item)

    def remove_from_cart(self, item):
         Order.cart.remove(item)

    def __len__(self):
        return len(Order.cart)

    def __str__(self):
        return 'Items in the cart: ' + ', '.join(Order.cart)


o = Order()
o.add_to_cart('Rice')
o.add_to_cart('Beans')
o.add_to_cart('Sugar')
print(len(o))
print(o)

print()

o.remove_from_cart('Rice')
print(len(o))
print(o)