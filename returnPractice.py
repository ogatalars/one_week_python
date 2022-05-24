def is_even(num):
    if num % 2 == 0:
        return True
    return False
    
def sluggfiy(string):
    string = string.lower()
    string = string.replace(" ", "-")
    return string

def count_vowels(string):
    string = string.lower()
    count = 0
    for char in string:
        if char in "aeiou":
            count += 1
    return count