def name_of_function(first_name):
 """
 Simple test function
 """
 print(f"Yoo hoo, hello {first_name}!")
name_of_function("JOR")

print("")

def calculate_circumference(radius):
 """
 Calculate the circumference of a circle based on its radius
 """
 return 2 * 3.142 * radius 
a = calculate_circumference(5)
print(a)

print("")

def calculate_circumference(radius = 1):
 """
 Calculate the circumference of a circle based on its radius
 """
 return 2 * 3.142 * radius 
a = calculate_circumference()
print(a)
