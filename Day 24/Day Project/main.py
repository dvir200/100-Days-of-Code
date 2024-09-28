#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Day 24/Day Project/Input/Names/invited_names.txt", "r") as file:
  names = file.readlines()

with open("./Day 24/Day Project/Input/Letters/starting_letter.txt", "r") as file:
  list_letter = file.readlines()

first_line_holder = list_letter[0] 

name1 = names[0].strip("\n")

new = first_line_holder.replace('[name]', name1)
print(new)

