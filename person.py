#The class/blueprint for my objects
class Person:
  #class attribute ->constant visible to all objects of the class
  MAX_ENERGY=100
  #Initialiser(special method, invoked only once,at creation)
  def __init__(self,name,age=0,weight=10,energy=100):
    self.name =name 
    self.age =age
    self.weight=weight
    self.energy=energy
  
  
  
  
  def hello(self):
    print(F"Heloo my name is{self.name}. Im am {self.age} and i weight {self.weight}kg. Nice to meet ya")
  
  
  def grow(self):
    self.age+=1

  def eat(self,food, weight):
    self.weight+=weight
    print(f"{self.name} have eaten{food}and now weights{self.weight}")


if__name__== " __main__" :
    






Piotr=Person("piotr",66,81,65)
Anca=Person("anca",18)
Mihai=Person('mihai')
Tim=Person("tim",weight=87)


Anca.hello()
Tim.hello()
Piotr.hello()
Mihai.hello()

Piotr.grow()
Piotr.hello()

Tim.eat("Lasagna",2)
Tim.hello()