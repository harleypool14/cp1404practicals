from car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable car class"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_distance = randint(0, 100)
        if random_distance >= self.reliability:
            distance = 0
        travel_distance = super().drive(distance)
        return travel_distance
