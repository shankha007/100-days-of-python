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

choices = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

if human_choice < 0 or human_choice > 2:
    print("Wrong choice! Try again.")
else:
    comp_choice = random.randint(0, 2)
    print(choices[human_choice])

    print("Computer chose:")
    print(choices[comp_choice])

    if human_choice == comp_choice:
        print("Draw")
    elif (human_choice == 0 and comp_choice == 2) or (human_choice == 1 and comp_choice == 0) or (human_choice == 2 and comp_choice == 1):
        print("You won.")
    else:
        print("You lose.")