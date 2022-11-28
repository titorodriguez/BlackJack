from art import logo
from random import choice

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# print(logo)

deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

player_amount = 0
computer_amount = 0

player_cards.append(choice(deck_cards))
computer_cards.append(choice(deck_cards))

game_over = False

while not game_over:
    player_cards.append(choice(deck_cards))
    computer_cards.append(choice(deck_cards))

    player_amount = sum(player_cards)
    computer_amount = sum(player_cards)

    print(f"Your cards: {player_cards}, current score: {player_amount}\n"
          f"Computer’s first card: {computer_cards[0]}")

    # if player_amount == 21:
    #     final_message(player_cards, computer_cards, player_amount, computer_amount)
    #     print("Win with a Blackjack")
    # elif computer_amount == 21:
    #     final_message(player_cards, computer_cards, player_amount, computer_amount)
    #     print("Lose, opponent has Blackjack")
    # elif player_amount > 21:
    #     final_message(player_cards, computer_cards, player_amount, computer_amount)
    #     print("You went over. You lose")
    # elif computer_amount > 21:
    #     final_message(player_cards, computer_cards, player_amount, computer_amount)
    #     print("Opponent went over. You win")
    # else:
    #     game_continue = input("Type ‘y’ to get another car, type ‘n’ to pass: ")

    if game_continue == 'n':
        print(f"Your final hand: {player_cards}, final score: {player_amount}\n"
              f"Computer's final hand: {computer_cards}, final score: {computer_amount}")


def final_message(player, computer, player_sum, computer_sum):
    print(f"Your final hand: {player}, final score: {player_sum}\n"
          f"Computer's final hand: {computer}, final score: {computer_sum}")


def game():
    if player_amount == 21:
        final_message(player_cards, computer_cards, player_amount, computer_amount)
        print("Win with a Blackjack")
    elif computer_amount == 21:
        final_message(player_cards, computer_cards, player_amount, computer_amount)
        print("Lose, opponent has Blackjack")
    elif player_amount > 21:
        final_message(player_cards, computer_cards, player_amount, computer_amount)
        print("You went over. You lose")
    elif computer_amount > 21:
        final_message(player_cards, computer_cards, player_amount, computer_amount)
        print("Opponent went over. You win")
    else:
        game_continue = input("Type ‘y’ to get another car, type ‘n’ to pass: ")


