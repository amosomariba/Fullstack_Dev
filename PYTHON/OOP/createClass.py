class Person:
    X = "Amos"
    y = "suchi"


p1 = Person()
print(p1.X)
print(p1.y)


class Car:
    def __init__(self, model, company, type):
        self.model = model
        self.company = company
        self.type = type


car1 = Car("BMW", "BMW", "SUV")
car2 = Car("GTR", "Nissan", "sedan")

print(car1.model)
print(car2.type)


class Car:
    def __init__(self, speedometer, manfa_date, model, company):
        self.speedometer = speedometer
        self.manfa_date = manfa_date
        self.model = model
        self.company = company

    def __str__(self):
        return f"My car is {self.model} and the company is {self.company}"


car3 = Car("10000km", 2015, "Mercedes", "Benz")
car2 = Car("106700km", 2017, "Toyota", "Cadilac")
print(car3)
print(car2)
print(car2.speedometer)


# Object Method
class Person:
    def __init__(self, firstName, secondName, age):
        self.firstName = firstName
        self.secondName = secondName
        self.age = age

    def myName(self):
        print(
            f"My fullname is {self.firstName} {self.secondName} and I am {self.age} years old."
        )


p1 = Person("Amos", "Omariba", 27)
p2 = Person("Onsongo", "Omariba", 30)

p1.myName()
p2.myName()
