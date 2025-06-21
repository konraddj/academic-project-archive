def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
    if iterate_number == number and number %2 == 0: #https://learnpython.com/blog/multiple-conditions/#:~:text=Logical%20Operators,of%20the%20statements%20is%20true.
        return True
 else:
    return False
result = find_num([1,2,3,4,5,6,7,8], 7)
print(result)
