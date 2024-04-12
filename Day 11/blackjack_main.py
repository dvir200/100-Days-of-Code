from blackjack_art import logo
import random
import os

# Need to add the scenario of a blackjack (2 cards, an ace and a 10)

def card_sum(list):
    sum = 0
    for item in list:
        sum += item
    return sum


def game_status(user_list, computer_list):
    print(f"Your cards: {user_list}, current score {str(card_sum(user_list))}")
    print(f"Computer's first card: {str(computer_list[0])}")


def winner(user_list, computer_list):
    if card_sum(computer_list) > 21:
        print("Computer went over 21. You win.")
    elif card_sum(user_list) > card_sum(computer_list):
        print("You won")
    elif card_sum(user_list) < card_sum(computer_list):
        print("Opponent went over. You lose")
    elif card_sum(user_list) == card_sum(computer_list):
        print("It's a draw")


def game():
    print(logo)
    user_playing = True
    choice = ""
    computer_cards = []
    user_cards = []
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    while card_sum(computer_cards) < 17:
        card_chosen = random.choice(cards)
        if card_chosen == 11:
            if card_sum(computer_cards) + card_chosen > 21:
                computer_cards.append(card_chosen % 10)
            else:
                computer_cards.append(card_chosen)
        else:
            computer_cards.append(card_chosen)
    if card_sum(computer_cards) > 21:
        print(f"Your cards: {user_cards}, current score {str(card_sum(user_cards))}")
        print(f"Computer's cards: {computer_cards}, current score {str(card_sum(computer_cards))}")
        winner(user_cards, computer_cards)
        if input("Do you want to play a game of Blackjack? type \'y' or \'n'. ") == "y":
            os.system('cls')
            game()
        else:
            exit()

    print(computer_cards)
    game_status(user_cards, computer_cards)
    while card_sum(user_cards) < 21 and user_playing == True:
        choice = input("type \'y' to get another card, type \'n' to pass. ")
        if choice == "y":
            user_cards.append(random.choice(cards))
            game_status(user_cards, computer_cards)
        elif choice == "n":
            user_playing = False
    if card_sum(user_cards) > 21:
        game_status(user_cards, computer_cards)
        print("You went over. You lose.")
        if input("Do you want to play a game of Blackjack? type \'y' or \'n'. ") == "y":
            os.system('cls')
            game()
        else:
            exit()
    elif card_sum(user_cards) <= 21 and user_playing == False:
        print(f"Your cards: {user_cards}, current score {str(card_sum(user_cards))}")
        print(f"Computer's cards: {computer_cards}, current score {str(card_sum(computer_cards))}")
        winner(user_cards, computer_cards)
        if input("Do you want to play a game of Blackjack? type \'y' or \'n'. ") == "y":
            os.system('cls')
            game()
        else:
            exit()
        

    

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game()

