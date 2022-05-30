#  insert(index, element) - inserts an element at a given index
num = [7, 3, 9]
num.insert(1, 'Hi')
print(num) # [7, 'Hi', 3, 9]

waitlist = ['John', 'Bob', 'Alice']	
waitlist.insert(0, 'Tim')
waitlist.insert(-1, 'Tom')
print(waitlist)