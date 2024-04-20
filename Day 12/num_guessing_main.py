from num_guessing_art import logo
import random

NUM_CHOSEN = random.randint(1, 100)


def game(difficulty):
  global NUM_CHOSEN
  if difficulty == "hard":
    attempts = 5
  elif difficulty == "easy":
    attempts = 10
  while attempts != 0:
    user_guess = int(input("Make a guess: "))
    if user_guess == NUM_CHOSEN:
      attempts = 0
      print(f"You got it! The answer was {NUM_CHOSEN}")
      quit()
    elif user_guess > NUM_CHOSEN:
      attempts -= 1
      if attempts == 0:
        None
      else:
        print("Too high")
        print("Guess again")
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif user_guess < NUM_CHOSEN:
      attempts -= 1
      if attempts == 0:
        None
      else:
        print("Too low")
        print("Guess again")
        print(f"You have {attempts} attempts remaining to guess the number.")
  print("You've run out of guesses. You lose.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_difficulty = input("Choose a difficulty. Type \'easy' or \'hard': ").lower()
game(user_difficulty)