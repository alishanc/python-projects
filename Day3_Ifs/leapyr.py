year = int(input("Which year do you want to check? "))
# Write your code below this line 👇

# leap = year % 4
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year")
else:
    print("Not leap year.")
