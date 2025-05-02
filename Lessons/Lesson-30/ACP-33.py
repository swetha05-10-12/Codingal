class BMW:
    def __init__(self, fuel_type, max_speed):
        self.fuel = fuel_type
        self.speed = max_speed

    def fuel_type(self):
        print("BMW Fuel Type:", self.fuel)

    def max_speed(self):
        print("BMW Max Speed:", self.speed, "km/h")


class Ferrari:
    def __init__(self, fuel_type, max_speed):
        self.fuel = fuel_type
        self.speed = max_speed

    def fuel_type(self):
        print("Ferrari Fuel Type:", self.fuel)

    def max_speed(self):
        print("Ferrari Max Speed:", self.speed, "km/h")


cars = [BMW("Petrol", 307), Ferrari("Petrol", 340)]

for car in cars:
    car.fuel_type()
    car.max_speed()
