
menu = "Please enter the number of items."
print(menu)
shop_items_number = int(input("No. of items: "))
while shop_items_number < 0:
    print("Invalid number of items!")
    shop_items_number = int(input("No. of items: "))
if shop_items_number > 0:
    print(f"Number of items: {shop_items_number}")
    shop_items_total = 0
    for i in range(0, shop_items_number):
        shop_items_price = float(input("Price of item:"))
        shop_items_total += shop_items_price
    if shop_items_total > 100:
        shop_items_total = shop_items_total * 0.9
    print(f"Total price for {shop_items_number} is ${shop_items_total:.2f}")



