#  Raise ValueError - We can raise our own exceptions(force them happen) whenever we want, using the raise keyword.
# raise IndexError
# raise Exception
# raise ValueError

# raise ValueError("This is a value error")

def get_user_name():
    inp = input('please enter your name: ')
    if not inp.isalpha():
        raise ValueError('Name must be alphabetic')
    return inp

def register_user():
    user = get_user_name()
    Database.save(user)