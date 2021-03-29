"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        res_cargo = self.cargo + number
        if res_cargo <= self.max_cargo:
            self.cargo = res_cargo
            return self.cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before


# plane = Plane(10, 20, 400, 40000, 50)
# print(plane)
# assert isinstance(plane, Vehicle)

