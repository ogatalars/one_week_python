first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
# total_name = str(first_name + " " + last_name)
if(len(first_name) + len(last_name) == 12):
    print("Your name is american standard name.")
elif(len(first_name) + len(last_name) > 12):
    print("Your name is longer than the american standard.")
else:
    print("Your name is shorter than the american standard.")    
    

    