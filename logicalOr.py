# The or operator will evaluate to True if either of the operands is True (just one of the operands needs to be True)
'a' == 'b' or 1 < 5 # True
day = str(input("What day of the week is it? "))

if day == 'saturday' or day == 'sunday':
    print("It's the weekend!")
else:
    print('It is not the weekend.')    