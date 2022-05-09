unit = str(input("Enter a unit: "))
temp = float(input("Enter a temperature: "))

if unit == 'fahreinheit':
    if temp <= 32:
        print("It's freezing outside!")
    else:
        print("It's not freezing outside!")
else:
    print("Im really bad with celsius")        
    
    
fav_color = "green"
fav_movie = "amadeus"
fav_food = "pizza"

if fav_color == "green":
    print("I love green too!")
    if fav_movie == "amadeus":
        print("I love amadeus too!")
        if(fav_food == "pizza"):
            print("I love pizza too!")    