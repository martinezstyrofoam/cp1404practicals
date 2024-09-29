
menu = """(H)ello
(G)oodbye
(Q)uit"""
name = input("Enter name: ")
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Good bye {name}")
    else:
        print("Invalid choice.")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")
