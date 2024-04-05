import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_text, shift_amount, type):
  #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
  message = ""
  if type.lower() == "encode":
    for x in user_text:
      if x not in alphabet:
        message += x
      else:
        message += alphabet[alphabet.index(x) + shift_amount]
    print(f"The encoded text is: {message}.")
  elif type.lower() == "decode":
    for x in user_text:
      if x not in alphabet:
        message += x
      else:
        message += alphabet[alphabet.index(x) - shift_amount]
    print(f"The decoded text is: {message}.")


#TODO-1: Import and print the logo from art.py when the program starts.
print(caesar_art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift % 26
  caesar(user_text=text, shift_amount=shift, type=direction)
  user_choice = input("Do you want to restart the cipher program? ")
  if user_choice.lower == "yes":
    user_choice =  True
  elif user_choice.lower == "no":
    user_choice =  False




#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).



