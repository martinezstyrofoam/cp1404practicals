
sales = float(input("Enter sales: $"))
bonus1 = 0.1
bonus2 = 0.15

while sales >= 0:
    if sales < 1000:
        user_bonus = sales * bonus1
        print(f"Your bonus is: {user_bonus}")

    elif sales >= 1000:
        user_bonus = sales * bonus2
        print(f"Your bonus is: {user_bonus}")

    else:
        print("Error: Invalid number.")

    sales = float(input("Enter sales: $"))
print("Whoops! Please put a VALID NUMBER.")