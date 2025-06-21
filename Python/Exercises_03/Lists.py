#single element
my_list = [1,2,3,4,"A"]
a = len(my_list)
print(a)
slice_1 = my_list[1:3:1]
print(slice_1)
my_charakter = my_list[-1]
print(my_charakter)

print("")

#concatenate lists
my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S","T","Fish",9,10]
concatenated_list = my_list_1 + my_list_2
print(concatenated_list)

print("")

#nested lists
my_list_3 = [1,2,3,4,"A"]
my_list_4 = ["S","T","Fish",9,10]
concatenated_list_1 = [my_list_3, my_list_4]
print(concatenated_list_1)


print("")

#lists are mutable
#sample one
my_list_5 = ["S","T","Fish",9,10]
print(my_list_5)
my_list_5[2] = "Chips"
print(my_list_5)

print("")

#sample twoo
my_list_6 = ["One","Two","Three"]
print(my_list_6)
my_list_6.append("Four")
print(my_list_6)
