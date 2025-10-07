class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        pass
class Dog(Animal):
    def talk(self):
        print( "Woof! Woof!")
class Cat(Animal):
    def talk(self):
        print("Meow! Meow!")