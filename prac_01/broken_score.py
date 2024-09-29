
score = float(input("Enter score: "))
if 0 <= score <= 100:
    if score >= 90:
        print("Excellent!")
    elif score >= 50:
        print('Well you know what they say: "Ps get degrees". You passed.')
    else:
        print("Bad. Go watch the lecture recordings.")
else:
    print("Invalid score")


