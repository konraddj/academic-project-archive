"""
Simple Class by JOR, by convention, use camel case to name classes
"""
# Create a class
class JORzClass():

 # Constructor, called whenever an instance of the class is created.
 def __init__(self, my_greeting):
  print("Running constructor for JORzClass")
 # Create attributes and set initial values
  self.message = my_greeting
 def my_method(self):
  print(self.message)
my_class1 = JORzClass("Morning JOR!")
my_class1.my_method()
print(type(my_class1))

class KDJzClass():
 def __init__(self, my_goodby, high_five):
  print("Running constructor for KDJzClass")
  self.message1 = my_goodby
  self.message2 = high_five
 def my_method1(self):
  print(self.message1, self.message2)
my_class2 = KDJzClass("Goodby Konrad!","\nGive a high five")
my_class2.my_method1()
print(type(my_class2))

