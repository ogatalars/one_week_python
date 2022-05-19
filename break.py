# We can use the break keyword to prematurely exit a loop. Usually this is done inside of a conditional
for char in 'pickleface':
    if char == 'f':
        break
    print(char)
# Continue, in another hand, the continue keyword is used to skip the rest of the loop and continue with the next iteration.
for char in 'FATCAT':
    if char == 'A':
        continue
    print(char)