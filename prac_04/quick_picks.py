# had to look at solutions for a bit of help

import random

NUMBER_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBER_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_picks:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


main()
