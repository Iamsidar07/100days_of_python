import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
code_words = [data_dict[letter] for letter in word]
print(code_words)
