class Car:
  name = "None"
  height = 1000
  speed = 200.00

  def __init__(self, name, height):
    self.name = name
    self.height = height
    print(self.name, "has weght", self.height)

  def set(self, name, height, speed):
    self.name = name
    self.height = height
    self.speed = speed

class Truck (Car):
  wheels = 8

audi = Car()
Kia = Car ()
Man = Truck()

audi.set("audi", 1450, 320.2)
Kia.set("GayMobile", 1500, 150.55)
Man.wheels = 12
Man.set ("Man", 4500, 100)

print (Kia.name)
print (audi.speed)
print (Man.wheels)