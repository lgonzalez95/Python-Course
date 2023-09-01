product = input("Enter a product name: ")
price = input("Enter the product price: ")

total_len = len(product) + len(price)

dots = "."*(25-total_len)

print(product+ dots+ price)