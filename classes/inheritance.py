class Animal:
    def __init__(self):
        self.age =1


    def eat(self):
        print('eat')


# Animal : Parent , Base 
# Mammal : Child , Base 

class Mammal(Animal):
    def walk(self):
        print("walk")


        
class Fish(Animal):
    def swim(self):
        print("walk")



m =Mammal()
m.eat()
