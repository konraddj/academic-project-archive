"""
remove_brackets_test.py
By: Konrad Jeziorski
    Inspired by John O'Row's code
Date: 12/11/2022
*****************
Text output without the brackets
"""

def remove_brackets(string_with_brackets):
    string_without_brackets = string_with_brackets.strip('(')
    string_without_brackets = string_without_brackets.strip(')')
    return string_without_brackets
remove_brackets(string_with_brackets=str)

host_name = remove_brackets("(((This message has been stripped of brackets!)))")
print(host_name)

print("Finished test for oui"  "\nIf the test is run from a batch file in windows, press [ctrl][z] and then [Enter] to exit")