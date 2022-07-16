# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# My Way further down

bmi = round(weight / height ** 2)
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# bmi = round(weight / height ** 2)

# if bmi <= 18.5:
#     print('"Your BMI is ' + str(round(bmi)) + ', you are underweight."')
# elif bmi <= 25:
#     print('"Your BMI is ' + str(round(bmi)) + ', you have a normal weight."')
# elif bmi <= 30:
#     print('"Your BMI is ' + str(round(bmi)) +
#           ', you are slightly overweight."')
# elif bmi <= 35:
#     print('"Your BMI is ' + str(round(bmi)) + ', you are obese."')
# else:
#     print('"Your BMI is ' + str(round(bmi)) + ', you are clinically obese."')


# I used "" formating to put entire output with variable in double quotes
# the coding exercise expected normal output w/o double quotes like this
# print("Your BMI is "  + str(round(bmi)) +  ", you are clinically obese.")
