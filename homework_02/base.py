from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=300, fuel=500, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            elif self.fuel == 0:
                raise LowFuelError
        return self.started

    def move(self, distance):
        expected = self.fuel - distance * self.fuel_consumption
        if expected < 0:
            raise NotEnoughFuel
        else:
            self.fuel = expected
            return self.fuel
