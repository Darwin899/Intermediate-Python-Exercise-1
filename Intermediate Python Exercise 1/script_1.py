def get_unique_list(my_list):
    # Declare a list 
    uniq_list = []
    # Method to combine new values to unique_list from my_list
    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)
    return uniq_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
# Use print method to priint unique_list
print(unique_list)
