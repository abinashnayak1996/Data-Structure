import operator

d = {'r': 34, 'q': 12, 'h': 67, 'd': 45}
sort = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(sort)
