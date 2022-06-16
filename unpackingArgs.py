#  Turning sequences into separete args

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total 

print(sum(3,4,6,10,11,203,12))
nums = [3,4,6,10,11,203,12] # list
print(nums)
# print(sum(nums)) #da erro
print(sum(*nums))