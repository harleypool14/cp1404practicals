MIN_LENGTH = 6
password = input("Enter the password: ")
while len(password) < MIN_LENGTH:
    password = input("Enter the password: ")
print('*' * len(password))

