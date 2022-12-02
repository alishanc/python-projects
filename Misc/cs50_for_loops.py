for i in range(3):
    # assigns 'i' to list value up to 3 and iterates
    print("meow")  # 3 times

students = ["Ali", "Zaini", "Ibrahim"]

for i in range(len(students)):
    print(i + 1, students[i])

# Dicts
houses = {"Franklin": "Wisconsin",
          "Chicago": "Illinois",
          "Lahore": "Pakistan"
          }

# print(houses["Franklin"])
# print(houses["Chicago"])
# print(houses["Lahore"])
for house in houses:
    print(house, houses[house], sep=", ")

locations = [
    {"city": "Franklin", "state": "Wisconsin", "zip": "53132"},
    {"city": "Chicago", "state": "Illinois", "zip": "606001"},
    {"city": "Lahore", "state": "Pakistan", "zip": None}
]

for location in locations:
    print(location["city"], location["state"], location["zip"], sep=", ")


def main():
    # print_column(3)
    print_square(3)


def print_square(size):
    #For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            # Print Brick
            print("#", end="")
        # To print a new row of bricks
        print()


# def print_column(height):
#     for _ in range(3):
#         print("#")

main()

