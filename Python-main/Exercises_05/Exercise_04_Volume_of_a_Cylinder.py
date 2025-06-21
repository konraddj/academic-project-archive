Vol_cylinder = lambda radius, cylinder: 3.14159*radius**2*cylinder
radius = int(input("Enter the radius of the cylinder:"))
cylinder = int(input("Enter the height of the cylinder:"))
print(Vol_cylinder(radius, cylinder))