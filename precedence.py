#there are orders to use logical operators
# NOT, AND , OR *nesta ordem

day = "Monday"
is_vet = False
age = 56
#Veterans get in free on tusdays
#infants under 2 get in for free always

if age <= 2 or is_vet and day =="Tuesday":
    print("You get in free!")
if not age <= 2 or is_vet and day =="Tuesday":
    print("You get in free!")   