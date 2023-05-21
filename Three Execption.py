def raise_key_error():
    try:
        my_dict = {'key': 'value'}
        print(my_dict['invalid_key'])
    except KeyError:
        print("Caught KeyError: The key does not exist in the dictionary.")

def raise_name_error():
    try:
        print(undefined_variable)
    except NameError:
        print("Caught NameError: The variable is not defined.")

def raise_index_error():
    try:
        my_list = [1, 2, 3]
        print(my_list[10])
    except IndexError:
        print("Caught IndexError: The index is out of range.")


# Raise and handle the exceptions
raise_key_error()
raise_name_error()
raise_index_error()
