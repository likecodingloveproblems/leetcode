class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.size = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        carType -= 1
        if self.size[carType] > 0:
            self.size[carType] -= 1
            return True
        else:
            return False


parking = ParkingSystem(1, 1, 0)
for car in [1, 2, 3, 1]:
    print(parking.addCar(car))
