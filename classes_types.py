class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        pass
class Dog(Animal):
    def talk(self):
        print( self.name,"speaks Woof! Woof!")
class Cat(Animal):
    def talk(self):
        print(self.name,"speaks Meow! Meow!")