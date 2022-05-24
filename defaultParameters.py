# To give a parameter a default value if no argument is provided, simply add the defaut value in the argument list. (parameter = value)
def laugh(intensity = 10):
    print("HA " * intensity)
    
def slugfy(phrase, sep="-"):
    return phrase.lower().strip().replace(" ", sep)
    