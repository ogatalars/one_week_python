# Tuples are immutable, ordered collections (lists are mutable, ordered)
# there not so many methods on tuples
# tuple() - creates a tuple
# You cannot create a tuple with a single element

dishes = ('burrito', 'taco', 'fajita', 'quesadilla')
print(dishes[0])
print(dishes[0:2])
# You cannot alter a tuple
print(dishes.index('burrito'))
# You cannot add to a tuple, but you can use some methods to see
for dish in dishes:
    print(dish)
    
# Why use tuples? -> they are more efficient than lists; Use them for data that shouldn't change. Some methods return them like dict.items(); they can be used as keys in a dictionary.