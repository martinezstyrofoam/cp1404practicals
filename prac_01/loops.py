
menu = """Type letters 'A', 'B', 'C', or 'D' for a cool slew of loops!
'A' for a loop that displays all the odd numbers between 1 and 20 with a space between each one.
'B' for a loop that counts in 10s from 0 to 100.
'C' for a loop that counts down from 20 to 1.
'D' for a loop that asks you for a number and prints that many stars.
Anything else is a no-no."""
print(menu)
test_loop = input().upper()

while test_loop != "Q":
    if test_loop == "A": # 'sample'
        for i in range(1, 21, 2):
            print(i, end=' ')
        print()
    elif test_loop == "B": # 'a'
        for i in range(0, 101, 10):
            print(i, end=' ')
        print()
    elif test_loop == "C": # 'b'
        for i in range(20, 0, -1):
            print(i, end=' ')
        print()
    elif test_loop == "D": # 'c'
        print("Loop 'A' or 'B'?")
        test_loop_d = input().upper()
        star = "*"
        satr = ""
        star_no = 0
        if test_loop_d == "A":
            print("How many stars would you like? Whole numbers only!")
            stars = int(input())
            if stars == int():
                while star_no < stars:
                    satr = satr + star
                    star_no = star_no + 1
                print(f"Number of stars: {stars}")
                print(satr)
            print()
        elif test_loop_d == "B": # 'd'
            print("How many stars would you like? Whole numbers only!")
            stars = int(input())
            for i in range(1, stars, 1):
                while star_no < stars:
                    satr = satr + star
                    star_no = star_no + 1
                    print(satr)
            print()
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    print(menu)
    test_loop = input().upper()

