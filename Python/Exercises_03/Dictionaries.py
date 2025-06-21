my_dictionary={"FName":"John","Sname":"ORaw","Occupation":"Rocket Scientist"}
print(my_dictionary)
print("Works as a " + my_dictionary["Occupation"])

print("")

#create the initial dictionary
my_dictionary_1={"FName":"John","Sname":"ORaw","Occupation":"Rocket Scientist"}
print(my_dictionary_1)
#add a key:value pair
my_dictionary_1["Solary"] = "Not Enough!"
print(my_dictionary_1)
#edit one value
my_dictionary_1["Occupation"] = "Brian Surgeon!"
print(my_dictionary_1)

a = my_dictionary.items()
print(a)