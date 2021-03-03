# Duplicate elements remove
list1 = [67,34,12,68,23,34,12,56,67,68]
list2 =[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)