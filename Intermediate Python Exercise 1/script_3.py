# Method to return the frequency dict from a string
def get_freq_dict(string):
    # Convert the string to lower
    string = string.lower()
    # Remove whitespace form string
    string = string.replace(" ", "")
    # Creating a new dict for frequency dictionary
    freq_dict = {}  
    # Calculating the frequency dictionary using loops  
    for i in string:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict

# Calling the get_freq_dict method on string 
string = "hello world"

# Use print metho to print the output
print(get_freq_dict(string))
