class Human:
  MAX ENERGY =100

  def __init__(self,name=, age=0, energy=Human.MAX_ENERGY):
    self.name="Human"
    self.age=0
    self.energy =Human.MAX_ENERGY


  def display(self):
    print(f"{self.name}")

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
