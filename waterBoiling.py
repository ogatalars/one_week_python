unit = str(input("What unit are you using?"))
temp = float(input("What is the temperature?"))
if unit == 'f':
    if temp == 212:
        print("Water is boiling")
    else:
        print("Water is not boiling")
if unit == 'c':
    if temp == 100:
        print("Water is boiling")
    else:
        print("Water is not boiling")
if unit == 'k':
    if temp == 373.15:
        print("Water is boiling")
    else:
        print("Water is not boiling")                       