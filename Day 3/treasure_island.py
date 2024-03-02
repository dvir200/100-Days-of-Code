print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" ')

if (direction == "left"):
  lake = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. type "swim" to swim across.')
  if (lake == "wait"):
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
    door = door.lower()
    if (door == "yellow"):
      print ("You Win!")
    elif (door == "red"):
      print ("Burned by fire.")
      print("Game Over.")
    elif (door == "blue"):
      print ("Eaten by beasts.")
      print("Game Over.") 
    else:
      print("Game Over.") 
  else:
    print("Attacked by trout.")
    print("Game Over.") 
else:
  print("Fall into a hole.")
  print("Game Over.") 