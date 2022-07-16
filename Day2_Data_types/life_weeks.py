# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇s

days = 90 * 365 - int(age) * 365
weeks = 90 * 52 - int(age) * 52
months = 90 * 12 - int(age) * 12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)
print(f"Yaaayyyy!! You did it SONNNN!!!")



### longer uglier way ###
# days = int(age) * 365
# days90 = 90 * 365
# days_left = days90 - day