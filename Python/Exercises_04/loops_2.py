iterable_variable = [1,2,3,4,5,6]
for item in iterable_variable:
 if item %2 != 0: # the remainder of modulo 2 cannot be 0; odd numbers will be printed
    print(item)

print("")

iterable_variable = [1,2,3,4,5,6]
for item in iterable_variable:
 if item %2 != 1: # the remainder of modulo 2 cannot be 1; even numbers will be printed
    print(item)