import higher_lower_art
import higher_lower_game_data
import random
import os

SCORE = 0
print(higher_lower_art.logo)

def game(game_data):
  global SCORE
  user_choice = ""
  looper = True
  compare_a = random.choice(game_data)
  compare_b = random.choice(game_data)
  
  #while loop exist in case two variables the same
  while compare_a == compare_b:
    compare_b = random.choice(game_data)
  
  print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
  print(higher_lower_art.vs)
  print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
  print()
  
  #input check
  while looper == True:
    user_choice = input("who has more followers? Type \'A' or \'B': ")
    user_choice = user_choice.upper()
    if user_choice == 'A':
        looper = False
    elif user_choice == 'B':
        looper = False
  
  #translating user choice to comparing
  if user_choice == 'A' and compare_a['follower_count'] > compare_b['follower_count']:
    SCORE += 1
    os.system('cls')
    game(higher_lower_game_data.data)
  elif user_choice == 'B' and compare_a['follower_count'] < compare_b['follower_count']:
    SCORE += 1
    os.system('cls')
    game(higher_lower_game_data.data)
  else:
    os.system('cls')
    print(f"Sorry, that's wrong. Final score: {SCORE}")


game(higher_lower_game_data.data)