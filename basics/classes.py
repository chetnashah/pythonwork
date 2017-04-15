# null equivalent in python is None

# naming convention class names should start with Capital letter
class Person:
    health = 100 # static class varible shared by all instances also has serious gotchas e.g. refer http://stackoverflow.com/questions/68645/static-class-variables-in-python/69067#69067

    #unlike Java, you cannot have multiple constructors in Python
    def __init__(self, city=None): # the constructor
        print("constructor called!")
        self.city = city # member gets added in costructor
        self.age = 55 # member gets added in constructor
    def createName(self, name): # first parameter should be self
        self.name = name # member name gets added to class, after this method called
    def displayName(self):
        return self.name
    def saying(self):
        print("hello %s" % self.name)
    def getHealth(self):
        return self.health
    def dealDamage(self, amount):
        self.health = self.health - amount
        if self.health <= 0:
            print("Dude dead")
        else:
            print("Go on")

#create class instance like following
# first = Person()  #Create an instance of class, No new keyword, simple function invocation notation

# first.createName('Chetna') Note self is automatically passed from instance
# first.displayName() Note, self is automatically passed from instance

# essentially self is the placeholder for the object itself
