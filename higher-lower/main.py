from art import logo, vs
from game_data import data
import random


def get_random_account():
    """
    returns a random account from data list
    """
    return random.choice(data)


def format_data(account):
    """
    Returns the data in format of name, description and country
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}"


def check_answer(guess, a_follower, b_follower):
    """
    Check the answer and returns a True or False
    """
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_a = get_random_account()
account_b = get_random_account()

while game_should_continue:
    account_a = account_b
    account_b = get_random_account()
    while account_a == account_b:
        account_b = get_random_account()
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if check_answer(user_guess, account_a["follower_count"], account_b["follower_count"]):
        print("Right")
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print("Wrong")
        game_should_continue = False
        print(f"Sorry! that's wrong, score: {score}")
