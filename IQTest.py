"""
iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

Careful: index must start at 1
"""
numbers =("2 4 7 8 10")
numbers = numbers.split()
even = 0
odd = 0
index = None
oddNumber = 0
evenNumber = 0
for number in numbers:
    number= int(number)
    division = number % 2
    if division == 0:
        even +=1
        evenNumber = number
    else:
        odd +=1
        oddNumber = number
if even < odd:
    print(str(evenNumber))
    index = numbers.index(str(evenNumber))
    print(index+1)
else:
    index = numbers.index(str(oddNumber))
    print(index+1)