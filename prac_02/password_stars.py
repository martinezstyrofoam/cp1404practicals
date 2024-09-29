print("Enter a password. The password must be at least 10 characters long.")

def main():
    password_loop = 0
    while password_loop == 0:
        get_password()
        password_loop = 1
    print("Password has been set.")

def get_password():
    password_enter = input((str(">>> ")))
    if len(password_enter) >= int(10):
        set_asterisks()
    elif len(password_enter) < int(10):
        print("Password must be at least 10 characters long.")


def set_asterisks():
    asterisk_no = 0
    asterisks = ""
    for i in range(1, len(password_enter)):
        while asterisk_no < len(password_enter):
            asterisks = asterisks + "*"
            asterisk_no += 1
    print(f"Your password is: {asterisks}")



main()