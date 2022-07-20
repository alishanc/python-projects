import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

game_images = [rock, paper, scissors]

# user inputs as a string
user_choice = int(input("Choose.. 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!\n")
else:
    print(game_images[user_choice])

    # computer needs to chose #s between [0, 1, 2]
    # print(f"Computer chose\n {computer_choice}")
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!\n")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose :(\n")
    elif computer_choice > user_choice:
        print("You Lose :(\n")
    elif user_choice > computer_choice:
        print("You Win!\n")
    elif computer_choice == user_choice:
        print("Tie!\n")


print("""#Rules below:
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.\n""")

print("WOOOHOO I FREAKING DID IT!!!\n")


# Consolodated statements
# User's choice
# if int(user_choice) == 0:
#     print(f"You chose\n {rock}")
# if int(user_choice) == 1:
#     print(f"You chose\n {paper}")
# if int(user_choice) == 2:
#     print(f"You chose\n {scissors}")

# Computer's Choice
# if computer_choice == 0:
#     print(f"Computer chose\n {rock}")
# if computer_choice == 1:
#     print(f"Computer chose\n {paper}")
# if computer_choice == 2:
#     print(f"Computer chose\n {scissors}")
