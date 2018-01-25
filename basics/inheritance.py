# the basic way to declare dervied class is
# class DerivedClassName(BaseClassName):
#    pass

# This is a classical class, not a new style class
class Person:
  
  def __init__(self, first="John", last="Doe"):
    self.firstname = first
    self.lastname = last
  
  def Name(self):
    return self.firstname + " " + self.lastname

# Employee extends Person,
# Person is not a new-style class so super cannot be used in derived class
class Employee(Person):

  def __init__(self, first="EJohn", last="EDoe", eid="1001"):
    Person.__init__(self, first, last)
    self.eid = eid
  
  def GetEmplyee(self):
    return self.Name() + ", " +self.eid

x = Person("Marge", "simpson")
y = Employee("Homer","Simpson")

print(x.Name())
print(y.GetEmplyee())