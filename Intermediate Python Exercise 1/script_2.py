# Method to return combined dict with common keys and added values
def get_combined_dict(my_dict_1, my_dict_2):
    new_dict = {}
    for key, value in my_dict_1.items():
        if (key in my_dict_2.keys()):
            new_dict[key] = value + my_dict_2[key]

    return new_dict

# Declare the input dictionaries
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

# Calling the method on dictionaries
combined_dict = get_combined_dict(my_dict_1, my_dict_2)

# Printing the output
print(combined_dict)
