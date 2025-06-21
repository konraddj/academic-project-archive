my_set=set()
print(type(my_set))
print(my_set)
my_set.add(1)
my_set.add(2)
my_set.add(2) #This add is ignored. no error / collection of unique objects
print(my_set)
