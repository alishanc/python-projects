import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Write your code below this line 👇 harder way without using random.choice
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
payer = names[random_choice]

# using random choice func
random = random.choice(names)
print(f"{random} is going to buy the meal today!")
