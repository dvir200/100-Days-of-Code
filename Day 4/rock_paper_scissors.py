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

#Write your code below this line 👇
import random

list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))
if ((user_choice > 2) or (user_choice < 0)):
  print("You typed an invalid number. You lose")
  exit()

computer_choice = random.randint(0,2)

print(list[user_choice])
print("")
print("Computer Chose:")
print(list[computer_choice])
print("")



if (user_choice == computer_choice):
  print("Draw!")
elif ((user_choice == 0) and  (computer_choice == 2)):
  print("You Won!")
elif ((user_choice == 3) and  (computer_choice == 2)):
  print("You Won!")
elif ((user_choice == 1) and  (computer_choice == 0)):
  print("You Won!")
elif ((user_choice == 2) and  (computer_choice == 1)):
  print("You Won!")
else:
  print("You Lose!")