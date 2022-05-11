# The not operator changes True to False and False to True. 
False # false
not False # true
1 != 4 # true (é diferente do NOT)

temp = int(input("What is the temperature? "))
if not temp <= 0:
    print("It's a positive number, so it's warm.")
elif temp == 0:
    print("It's zero, so it's cold.")    
    
year = input("What is the year? ")


if not year.isnumeric():
    year = input("Please enter a number: ")
year = int(year)
print(f"You were born {2022-year} years ago.")
   