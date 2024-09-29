# Looked at the solution for this one for some guidance for line 9, 11, 12

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid amount")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Enter Price of item: "))
    total += price
if total > 100:
    total *= 0.9
print(f"Total price for {number_of_items} items is ${total:.2f}")
