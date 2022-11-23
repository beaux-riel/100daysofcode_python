# Day 27 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Tkinter, *args, **kwargs and Creating GUI Programs - Playground Code

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1,2,3))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Volvo", model="244GL")
print(f"My first car was a {my_car.make} {my_car.model}.")
