# extend() => accepts an iterable and appends each item from that iterable to the end of the list
nums = [1,2,3,4]
nums.extend('abc')
print(nums)

waitlist = ['Renato', 'João', 'Maria', 'Pedro']
people = ['Charlie', 'Casey', 'David', 'Dennis', 'Erin', 'Michael', 'Nathalie', 'Nicholas']
waitlist.extend(people)