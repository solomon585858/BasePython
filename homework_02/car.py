"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine


# car = Car(10, 10, 5)
# car.start()
# print(car)
# print(Vehicle)
# if isinstance(car, Vehicle):
#     print("True")
# print(car.start())
# print(car.move(1))
# engine = Engine(volume=60, pistons=40)
# car.set_engine(engine)
# print(car.engine)
