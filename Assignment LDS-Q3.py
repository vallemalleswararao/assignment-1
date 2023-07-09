def are_rotations(str1, str2):
    # Check if lengths of both strings are the same
    if len(str1) != len(str2):
        return False

    # Concatenate str1 with itself
    temp = str1 + str1

    # Check if str2 is a substring of temp
    if str2 in temp:
        return True
    else:
        return False

# Get the two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_rotations(str1, str2):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")