from collections import Counter

inventory_counter = Counter(apple=50, mango=100, banana=120, orange=70)


def update_inventory(order):
    inventory_counter.subtract(order)
    return inventory_counter


client_order = Counter(apple=10, mango=12, banana=15, orange=5)

update_inventory(client_order)
print('New inventory updated:', inventory_counter)
