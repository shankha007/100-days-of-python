def add(*args):
    total = 0
    for num in args:
        total += num

    return total

print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(calculate(5, add=3, multiply=5))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # get fn should be used as if not passed, it won't throw error
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)