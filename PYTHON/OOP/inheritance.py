# 1
class Person:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def fullName(self):
        print(f"My fullname is {self.fName} {self.lName}.")


p1 = Person("Amos", "Onsongo")

p1.fullName()

# 2

class Student(Person):
    def __init__(self, fName, lName):
        Person.__init__(self, fName, lName)


s1 = Student("Kevin", "Kembo")
s1.fullName()

# 3
class Student(Person):
    def __init__(self, fName, lName, age):
        super().__init__(fName, lName)
        self.age = age

    def details(self):
        print(f"My name is {self.fName} {self.lName} and I am {self.age} years old.")


s3 = Student("Chitai", "kevin", 23)

s3.details()

# 4
class Teacher(Student):
    def __init__(self, fName, lName, age, subject, country):
        super().__init__(fName, lName, age)
        self.subject = subject
        self.country = country

    def teaching(self):
        print(
            f"I come from {self.country} and I teach {self.subject} only and I am {self.age} old"
        )


t1 = Teacher("Bonny", "Mayaka", 43, "English", "Kenya")
t1.teaching()
