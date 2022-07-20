states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

number_of_states = len(states_of_america)
print(states_of_america[number_of_states -14])

# order is important
# print(states_of_america[29])
print(states_of_america[-1])

# Append & Extend function examples
states_of_america.append("AliLand")
print(states_of_america[-1])
states_of_america.extend(["ZainiLand", "IbrahimLand"])
print(states_of_america)

# changing values inside a list
states_of_america[1] = "Pencilvania"
print(states_of_america[1])


# index order       0               1        2          3          4
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
veggies = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, veggies]

print(dirty_dozen[1][2])

# print(dirty_dozen[5])
# print(dirty_dozen[-3])
