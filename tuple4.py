t1 = (4, 6, 9)
t2 = (3, 5, 1)
t3 = (8, 2, 7)
result = tuple(map(sum, zip(t1, t2, t3)))
print(result)