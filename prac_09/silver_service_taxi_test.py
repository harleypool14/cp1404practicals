from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Lamborghini", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

    taxi = SilverServiceTaxi("Hummer", 200, 4)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()