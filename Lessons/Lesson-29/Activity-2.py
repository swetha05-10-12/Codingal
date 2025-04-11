from abc import ABC, abstractmethod

class animal(ABC):

    def move(self):
        pass

class Human(animal):

    def move (self):
        print("I can walk and run")

class Snake(animal):
    
    def move (self):
        print("I can crawl")

class Lion(animal):
    
    def move (self):
        print("I can roar")

class Dog(animal):
    
    def move (self):
        print("I can crawl")

a=Human()
a.move()

b=Snake()
b.move()

c=Lion()
c.move()

d=Dog()
d.move()



