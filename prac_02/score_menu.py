def main():
    score = 0
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    choice = ''
    while choice != 'Q':
        print(MENU)
        choice = input("Enter Choice: ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            determine_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell")
        else:
            print("Invalid")


def get_valid_score():
    score = float(input("Enter valid score: "))
    while score <= 0 or score >= 100:
        print("Invalid score")
        score = float(input("Enter valid score: "))
    return score


def determine_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    print(f"Your result is: {score}")


def show_stars(score):
    stars = '*' * int(score)
    print(f"Stars: {stars}")


main()
