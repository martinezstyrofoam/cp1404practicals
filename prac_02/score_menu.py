def main():
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)"""
    print(menu)
    choice = input(">>> ").upper()
    menu_loop(choice, menu)
    print("Bye!")


def menu_loop(choice, menu):
    while choice != "Q":
        if choice == "G":
            score = score_set()
        elif choice == "P":
            score_check(score)
        elif choice == "S":
            star_set(score)
        print(menu)
        choice = input(">>> ").upper()


def star_set(score):
    stars_no = 0
    stars = ""
    for i in range(score):
        while stars_no < score:
            stars = stars + "*"
            stars_no += 1
    print(stars)


def score_check(score):
    if 0 <= score <= 100:
        if score >= 90:
            print("Excellent!")
        elif score >= 50:
            print('Well you know what they say: "Ps get degrees". You passed.')
        else:
            print("Bad. Go watch the lecture recordings.")
    else:
        print("Invalid score")


def score_set():
    score = int(input("Enter score: "))
    return score


main()
