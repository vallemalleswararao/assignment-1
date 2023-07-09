def first_non_repeated_char(string):
    char_count = {}

    # Count the occurrences of each character
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeated character
    for char in string:
        if char_count[char] == 1:
            return char

    # Return None if there is no non-repeated character
    return None

# Get the string from the user
string = input("Enter a string: ")

non_repeated_char = first_non_repeated_char(string)

if non_repeated_char:
    print("The first non-repeated character is:", non_repeated_char)
else:
    print("There is no non-repeated character in the string.")