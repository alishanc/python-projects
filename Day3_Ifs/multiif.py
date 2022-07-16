print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can go on this ride")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Would you like a pic?! Y or N. ")
    if wants_photo == "Y":
        # Add $3
        # print(int(bill + 3)) <- my way (unit tested in Thonny)
        bill += 3
    print(f"Thanks! Your total is ${bill}. Please come back soon!")
    # ensure print function indentation aligns
else:
    print("You shall not pass")
