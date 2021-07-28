"""
Write a function that takes an array of numbers (integers for the tests) 
and a target number. It should find two different items in the array that,
when added together, give the target value. 
The indices of these items should then be returned in a tuple like so:
(index1, index2).

Example: twoSum [1, 2, 3] 4 === (0, 2)
"""


def two_sum(numbers, target):
    result = []
    for i in range(0,len(numbers)):
        for x in range(1,len(numbers)):
            if i!=x and numbers[i]+numbers[x] == target:
                    result.append(x)
                    result.append(i)
                    return result