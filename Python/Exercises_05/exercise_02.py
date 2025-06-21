def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
  if iterate_number == number:
   return True
 else:
  pass
result = find_num([1,2,3,4,5,6,7,8], 9)

if result is None: #return False instead of None if the value is not found
    result = False #https://bobbyhadz.com/blog/python-convert-none-to-empty-string

print(result)