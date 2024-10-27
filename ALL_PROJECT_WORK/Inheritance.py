class Vehicle():
    def general_usage(self):
        print('general usage: Transfortation')
class Car(Vehicle):
    def __init__(self):
        print('I am car')
        self.wheel=4
        self.has_roof=True
    def specific_usage(self):
        print('for travelling with family')

class Motercycle(Vehicle):
    def __init__(self):
        print('I am Moter cycle')
        self.wheel = 2
        self.has_roof = False

    def specific_usage(self):
        print('for riding,race')

c=Car()
c.specific_usage()
c.general_usage()
print('\n')
M=Motercycle()
M.specific_usage()
M.general_usage()
print(isinstance(c,Car))  #True
print(isinstance(c,Motercycle))  #False
print(issubclass(Car,Vehicle)) #true  car is derived from vehicle
print(issubclass(Car,Motercycle)) #False
