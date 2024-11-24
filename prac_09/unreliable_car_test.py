from unreliable_car import UnreliableCar


def main():
    """Test unreliable car"""

    reliable_car = UnreliableCar("Good", 100, 90)
    unreliable_car = UnreliableCar("Bad", 100, 5)

    for i in range(1, 6):
        print(f"Attempt to drive {i}km:")
        print(f"{reliable_car.name} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(i):2}km")

    print(reliable_car)
    print(unreliable_car)


main()