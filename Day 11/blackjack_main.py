from blackjack_art import logo
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def player_sum(list):
    sum = 0
    for item in list:
        sum += item
    return sum

def game():
    print(logo)
    user_playing = True
    computer_cards = []
    user_cards = []
    user_cards.append(random.choice())
    while player_sum(computer_cards) < 17:
        computer_cards.append(random.choice())
    print(f"Your cards: {user_cards}, current score{str(player_sum(user_cards))}")
    print(f"Computer's first card: {str(user_cards[0])}")
    while player_sum(user_score) > 21 or user_playing == False:
        if input("type \'y' to get another card, type \'n' to pass. ") == "y":
            user_cards.append(random.choice())

    

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if input("Do you want to play a game of Blackjack? type \'y' or \'n'. ") == "y":

