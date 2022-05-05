# str.upper() -> None arguments are used to make the string uppercase
# str.strip([char]) -> option arguments
# str.split([char]) -> option arguments too
name = "   hello"
print(name.strip())
name2 = "-----name" 
print(name2.strip("-"))

prices = "1.99 2.99 3.99 4.99 5.99"
print(prices.find('9')) # returns the index of the first occurrence of the specified value in the string, if nots returns -1 
print(prices.find('90000')) # returns -1 porque não achou o valor
print(prices.count('9')) # returns the number of occurrences of the specified value in the string