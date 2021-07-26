number = 10

count = 0
for i in range(number):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
        i += 1
    elif i % 3 == 0:
        count += 1
        i += 1
    elif i % 5 == 0:
        count += 1
        i += 1

    else:
        i += 1
    print(count)
