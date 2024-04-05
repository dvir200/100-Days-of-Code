import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_text, shift_amount, type):
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


print(caesar_art.logo)


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





