import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

word_list = ["camel","iloveu","monu","manoj","baby"]
chosen_word = random.choice(word_list)
print(logo)
# print(chosen_word)

blanks = []
lives = len(stages)

for blank in range(len(chosen_word)):
  blanks += "_"

while "".join(blanks) != chosen_word and lives >0:
    result = " ".join(blanks)
    print(result)
    guess = input("Guess a letter in word? ").lower()
    is_correct = False
    for letter in chosen_word:
        if letter == guess:
            # Replace blanks with letter
            blanks[chosen_word.index(letter)] = letter
            is_correct = True
            # all blanks are filled
            if "".join(blanks) == chosen_word:
                print("".join(blanks))
                print("Game over, You Won")
    if not is_correct:
        # loose a life
        print(stages[lives -1])
        lives -=1
        print("Loose a life...", lives)
        # have they run out of lives
        if lives == 0:
            print("Game Over")
