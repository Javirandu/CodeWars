

marks = [2, 3, 2, 2]
average = 0
def get_average(marks):
    sum = 0
    for x in marks:
        sum = sum + x
    num = len(marks)
    ans = sum/num
    return int(ans)

'''
the easyest way to resolve this is:
from statistics import mean
def get_average(marks):
    return int(mean(marks))
'''