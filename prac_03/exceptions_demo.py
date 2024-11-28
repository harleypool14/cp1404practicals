"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Questions:

1. When will a ValueError occur?

Answer: A value error will occur when a number with decimals is entered, letters or is empty.

2. When will a ZeroDivisionError occur

Answer: ZeroDivisionError will occur when when the number 0 is entered in the denominator area.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Answer: Yes you could change it by having it so if the denominator = 0 it prints a 
error message and lets you choose another denominator.
"""