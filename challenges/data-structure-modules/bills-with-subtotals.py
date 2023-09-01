from collections import Counter

prices = {"soap": 50, "toothpaste": 25, "shampoo": 45.50, "toothbrush": 15.99}


def generate_bill(order):
    print(f"{'Product':^10}{'Price':^10}{'Qty':^10}{'Sub-total':^10}")
    total = 0
    for product in order.items():
        sub_total = product[1] * prices.get(product[0])
        total += sub_total
        print(f"{product[0]:^10}"
              f"{'$' + str(prices.get(product[0])):^10}"
              f"{product[1]:^10}"
              f"{'$' + str(sub_total):^10}")

    print(f"{'Total: $' + str(total):^40}")


cart = Counter(soap=5, toothpaste=1, shampoo=2, toothbrush=3)
generate_bill(order=cart)
