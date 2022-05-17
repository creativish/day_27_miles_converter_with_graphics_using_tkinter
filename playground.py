def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5, 6, 9, 3, 23))

def calculater(**kwargs):
    print(kwargs)

calculater(add=5, multi=56, subtract=98)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Mahindra", model="XuV 700")
print(my_car.make)
print(my_car.model)