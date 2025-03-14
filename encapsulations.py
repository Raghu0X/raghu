class raghu:
  def __init__(self):
    self.pub = "ok"
    self.__prajwl="not ok"
  def rahul_private(self):
    print(self.__prajwl)
obj=raghu()
print(obj.pub)
obj.rahul_private()
