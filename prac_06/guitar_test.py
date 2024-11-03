from guitar import Guitar

CURRENT_YEAR = 2017


def run_tests():
    """Run tests for Guitar class."""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")


if __name__ == '__main__':
    run_tests()
