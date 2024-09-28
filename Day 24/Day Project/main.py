
with open("./Day 24/Day Project/Input/Names/invited_names.txt", "r") as file:
  names = file.readlines()

with open("./Day 24/Day Project/Input/Letters/starting_letter.txt", "r") as file:
  list_letter = file.readlines()


for x in range(0, len(names)):
  names[x] = names[x].strip("\n")


for x in range(0, len(names)):
  print(names[x])
  fileName = f"letter_for_{names[x]}.txt"
  if x == 0:
    list_letter[0] = list_letter[0].replace('[name]', names[x])
  else:
    list_letter[0] = list_letter[0].replace(names[x-1], names[x])
  with open(f"./Day 24/Day Project/Output/ReadyToSend/{fileName}", "w") as file:
    for line in list_letter:
      file.write(line)
