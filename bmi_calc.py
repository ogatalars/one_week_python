height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
bmi = weight * 703 / (height * height)
if bmi >= 39.9:
    print(f"Your bmi is {bmi} and you are Morbidly Obese!")
elif bmi < 39.9 and bmi >= 35:
    print(f"Your bmi is {bmi} and you are Obese!")
elif bmi < 34.9 and bmi >= 30:
    print(f"Your bmi is {bmi} and you are a Overweight!")
elif bmi < 29.9 and bmi >= 25:
    print(f"Your bmi is {bmi} and you are a little overweight!")
elif bmi < 24.9 and bmi >= 18.5:
    print(f"Your bmi is {bmi} and you are a Normal!")
else:
    print(f"Your bmi is {bmi} and you are a Underweight!")
                   