programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
    123: "1, 2, 3"
}
"""
Use proper formatting, indents etc similar to json structure
Dictionaries store info in "key": "value" pairs
Value types important i.e. "Strings" or diff  variable definitions
"""
# Retrieve a key/value from a dictionary. Spelling counts!
# print(programming_dictionary["Bug"])
# print(programming_dictionary[123])

# # Adding to the dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# # Create an empty dictionary
# empty_dictionary = {}

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "Overwriting an existing entry"
# print(programming_dictionary)

# # Wipe an existing dictionary. Useful for clearing out previously stored data or start fresh
# programming_dictionary = {}
# print(programming_dictionary)

# # Loop through a dictionary. Will only print keys
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
