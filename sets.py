#  Sets are UNORDERED collections of UNIQUE elements. So basically, there are no duplicates.
# Sets are used to store data that is not ordered.  We can alterate sets, operations.
# evens = {2, 4, 6, 8}
# odds = {1, 3, 5, 7, 9}
# não se pode colocar duplicados, nem lists ou tuples dentro 

set() # cria um empty set

evens = {2, 4, 6, 8}
evens.add(12)
evens.remove(2)
evens.discard(3) # remove o elemento, se existir
evens.clear() # remove todos os elementos