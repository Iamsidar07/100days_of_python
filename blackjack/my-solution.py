from art import logo
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

user_cards = [random.choice(cards), random.choice(cards)]
dealer_cards = [random.choice(cards), random.choice(cards)]
is_game_over = False


def blackjack():
    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Dealers's first card: {dealer_cards[0]}")
    wanna_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if wanna_another_card == "y":
        # continue
        print("Get another card.")
        user_cards.append(random.choice(cards))
        blackjack()

    else:
        # declare winner
        while dealer_score < 17:
            dealer_cards.append(random.choice(cards))
            dealer_score = sum(dealer_cards)
        if dealer_score > 21:
            print(f"You won, dealer cards: {dealer_cards}")
            is_game_over = True
        elif dealer_score < user_score:
            print(f"You won, dealer cards: {dealer_cards}")
            is_game_over = True
        elif dealer_score == user_score:
            print(f"Draw, dealer cards: {dealer_cards}")
            is_game_over = True
        else:
            print(f"You loose, dealer cards: {dealer_cards}")
            is_game_over = True
        if is_game_over:
            start_game()


def start_game():
    wanna_play_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    )
    if wanna_play_game == "y":
        print(logo)
        blackjack()
    else:
        print("Goodbye")


start_game()
