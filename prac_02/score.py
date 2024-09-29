def main():
    score = float(input("Enter score: "))
    score_check(score)


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


main()