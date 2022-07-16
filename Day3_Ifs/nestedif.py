print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can go on this ride")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Your total is $7.")
    elif age >= 18:
        print("Your total is $12.")
    else:
        print("Your total is $9.")
else:
    print("You shall not pass")
