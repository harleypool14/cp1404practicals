MIN_LENGTH = 6


def main():
    password = get_password()
    asterisks(password)


def asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Enter the password: ")
    while len(password) < MIN_LENGTH:
        password = input("Enter the password: ")
    return password


main()
