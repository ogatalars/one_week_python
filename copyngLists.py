#  copy() => copy() method returns a shallow copy of the list. Nested objects are not copied.
list1 = [12, 9, 3, 7]
list2 = list1.copy()
print(list1)
print(list2)
print(list1 is list2)
print(list1 == list2)
print(id(list1))
print(id(list2))

# The deepcopy() method returns a deep copy of the list. Nested objects are copied. but to do this you have to import copy module.