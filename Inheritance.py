class Animal:
    # __init__(self):
        def eat(self):
            print  "Eating "

class Dog(Animal):

    def bark(self):
        print "Barking"

d= Dog()
d.bark()
d.eat()