from art import logo
import random

print(logo)
print("Welcome to the guess the number game.")
target = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100 :")
diffiucltilevel = input(
    "Choose your game difficulti level. Type 'easy' or 'hard': "
).lower()
if diffiucltilevel == "easy":
    number_of_chances = 10
else:
    number_of_chances = 5
is_game_over = False
while not is_game_over and number_of_chances > 0:
    print(f"You have {number_of_chances} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    number_of_chances -= 1
    if user_guess > target:
        print("Too high")
    elif user_guess < target:
        print("Too low")
    else:
        print("Won")
        is_game_over = True
    if not is_game_over:
        print("Guess again.")
