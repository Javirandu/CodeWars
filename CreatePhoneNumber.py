"""
Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.
Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => 
returns "(123) 456-7890"
"""

"""
Map will be used in this method to apply str to all the elements of n list.
Then, this will return an object 
"""
def create_phone_number(n):
    prefix = n[:3]
    medium = n [3:6]
    final = n[6:]
    stringPrefix = "".join(map(str, prefix))
    stringMedium = "".join(map(str, medium))
    stringFinal = "".join(map(str, final))
    return f'({stringPrefix}) {stringMedium}-{stringFinal}'
