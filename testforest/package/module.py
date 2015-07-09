
name1 = 1

def function1():
  pass

class baseclass:

  classvariable = 2

  def basemethod1(self):
    pass


class class1(baseclass):
  
  classvariable = 1
  
  def method1(self):
    pass

  def method2(self):
    pass


def decorator(f):
  return f

@decorator
def function2():
  pass
