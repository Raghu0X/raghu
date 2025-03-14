class Circle:
  def __init__(self,radius):
     self.radius = radius
  def area(self):
        return 3.14 * self.radius * self.radius
circle1 = Circle(5)
print(f"Area:", circle1.area())
