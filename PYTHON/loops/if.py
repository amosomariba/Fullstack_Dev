fruits = ["mangoes", "bananas", "pawpaw", "apples"]

if "oranges" in fruits:
    print("oranges")

else:
    print("No fruit like that name in the basket")


age = int(input("Please enter your age here: "))
student = input("Are you a student? True or False : ")

is_student = student.lower() == "true"

if is_student and age > 18:
    print("You qualify to join the club.")

else:
    print("You are a child.")
