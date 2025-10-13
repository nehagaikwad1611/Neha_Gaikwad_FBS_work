from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.persons = 0

    @abstractmethod
    def toll(self):
        pass

class TwoWheeler(Vehicle):
    def __init__(self,persons):
        self.persons = persons

    def toll(self):
        toll = 20
        if self.persons > 2:
            toll += (self.persons - 2) * 20
        return toll

class ThreeWheeler(Vehicle):
    def __init__(self,persons):
        self.persons = persons

    def toll(self):
        toll = 30
        if self.persons > 3:
            toll += (self.persons-3) * 30
        return toll

class FourWheeler(Vehicle):
    def __init__(self,persons):
        self.persons = persons

    def toll(self):
        toll = 40
        if self.persons > 4:
            toll += (self.persons- 4)* 40
        return toll

class Heavyvehicle(Vehicle):
    def __init__(self, persons, wheels):
        self.persons = persons
        self.wheels = wheels

    def toll(self):
        toll = 60
        if self.persons > 6:
            toll += (self.persons - 6)*60
        return toll

while True:
    print("\n Toll Calculation system")
    print("1.Two wheeler")
    print("2.Three Wheeler")
    print("3.Four Wheeler")
    print("4.Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you for using toll calculation system ")
        break

    if choice == 1:
        

    


