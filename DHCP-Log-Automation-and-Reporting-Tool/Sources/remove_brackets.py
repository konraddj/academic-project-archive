"""
remove_brackets.py
By: Konrad Jeziorski
Date: 12/11/2022
"""
# Removes each open or closed bracket and returns the value without them

def remove_brackets(string_with_brackets):
    string_without_brackets = string_with_brackets.strip('(')
    string_without_brackets = string_without_brackets.strip(')')
    return string_without_brackets
