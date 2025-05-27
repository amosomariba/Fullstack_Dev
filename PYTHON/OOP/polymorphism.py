class Vehicle:
    def move(self):
        print("The vehicle can move")


class Lorry(Vehicle):
    def move(self):
        print("The lorry also moves")


class Bicycle(Vehicle):
    def move(self):
        print("The bicycle can peddle")


l1 = Lorry()
b1 = Bicycle()

b1.move()
l1.move()


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Move")


class Boat(Vehicle):
    def move(self):
        print("Sail")


class Plane(Vehicle):
    def move(self):
        print("Fly")


class Bycicle(Vehicle):
    def move(self):
        print("Cycle")


vehicles = [
    Car("BMW", "X6"),
    Boat("Ibiza", "touring 20"),
    Plane("Boeing", "747"),
    Bycicle("Speedbike", "Nagasaki"),
]

for vehicle in vehicles:
    print(f"{vehicle.brand} {vehicle.model}:", end=" ")
    vehicle.move()
