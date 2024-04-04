import random
import hangman_art
import hangman_words



chosen_word = random.choice(hangman_words.word_list)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

print(hangman_art.logo)

#Create blanks
display = []
for letter in chosen_word:
  display.append("_")

game_done = False

#Playing the actual game :)
while game_done is False and lives > 0:
  user_input = input("Guess a Letter: ").lower()

  if user_input in display:
    print(f"The letter \"{user_input}\" already guessed")

  elif user_input not in chosen_word:
      print(f"You've guessed \"{user_input}\", that's not in the word. You lose a life.")
      lives -= 1
      print(hangman_art.stages[lives])

  else:
    print("Letter correct. Updating sketch...")
    for x in range(0, len(chosen_word)):
      if (user_input == chosen_word[x]):
        display[x] = str(user_input)
    print(display)
    if "_" not in display:
      game_done = True
      
if lives > 0:
  print("You Won!")
  print(hangman_art.stages[lives])
else:
  print("You Lost!")
  print(hangman_art.stages[lives])
