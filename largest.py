# find out largest value in list
def func(l1):
    large = l1[0]
    for i in l1:
        if i > large:
            large = i
    return large
l1 = [12,34,56,78,23,45,13,24]
print(func(l1))