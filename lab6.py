class Car:
    def __init__(self, tank, fuel, speed):
        self.tank = tank
        self.fuel = fuel
        self.speed = speed

    def distance(self):
        return self.tank / self.fuel

class Truck(Car):
    def __init__(self, tank, fuel, speed, weight):
        super().__init__(tank, fuel, speed)
        self.weight = weight

    def ratio(self):
        # соотношение веса к количеству топлива на 250 км
        return self.weight / (self.fuel * 250)

class Bus(Car):
    def __init__(self, tank, fuel, speed, passengers):
        super().__init__(tank, fuel, speed)
        self.passengers = passengers

    def ratio(self):
        #соотношение пассажиров к количеству топлива на 250 км
        return self.passengers / (self.fuel * 250)

truck = Truck(100, 50, 80, 200)
bus = Bus(100, 20, 60, 50)

distance_truck = truck.distance()
ratio_truck = truck.ratio()

distance_bus = bus.distance()
ratio_bus = bus.ratio()

print("Расстояние, пройденное грузовиком:", distance_truck)
print("Соотношение веса груза к топливу у грузовика:", ratio_truck)
print("Расстояние, пройденное автобусом:", distance_bus)
print("Соотношение числа пассажиров к топливу у автобуса:", ratio_bus)