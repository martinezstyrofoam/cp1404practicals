"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# ans 1: If whatever isn't inputted not a proper/valid number. Like if someone put a word.
# ans 2: When the code tries to divide by zero.
# ans 3: put it all in a loop, when the "computing" is finally done, end the loop. For the nuclear option, delete
# the line that prints the zerodivisionerror and technically you'll have a 0% chance to encounter it./s