import copy

list1 = [1, 2, 3, 4, 5, [6, 7]]
list2 = copy.deepcopy(list1)

print(f"list1 : {list1}")
print(f"list2 : {list2}")

list1[0] = -1
list1[5][-0] = -6

print(f"list1 : {list1}")
print(f"list2 : {list2}")