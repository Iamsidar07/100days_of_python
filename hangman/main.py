import random
from arts import logo, stages
from word_list import word_list


chosen_word = random.choice(word_list)
print(logo)

blanks = []
lives = len(stages)
score = 0
total_attempts = 0
wrong_attempts = 0
right_attempts = 0


def show_result():
    print(chosen_word)
    print(
        f"Score: {score}\nAccuracy: {round((right_attempts/total_attempts)*100,2)}%\nTotal attempts: {total_attempts}\nRight Attempts: {right_attempts}\nWrong Attempts: {wrong_attempts}"
    )


for blank in range(len(chosen_word)):
    blanks += "_"

while "".join(blanks) != chosen_word and lives > 0:
    result = " ".join(blanks)
    print(result)
    guess = input("Guess a letter in word? ").lower()
    is_correct = False
    index = 0
    total_attempts += 1
    for letter in chosen_word:
        if letter == guess:
            # Replace blanks with letter
            blanks[index] = letter
            is_correct = True
            # all blanks are filled
        index += 1
    if is_correct:
        score += random.randint(10, 20)
        right_attempts += 1
        if "".join(blanks) == chosen_word:
            print("Game over, You Won")
            show_result()

    else:
        score -= random.randint(0, 10)
        wrong_attempts += 1
        # loose a life
        print(stages[lives - 1])
        lives -= 1
        print(f"Loose a life..., {lives} lives left")
        # have they run out of lives
        if lives == 0:
            print("Game Over")
            show_result()
