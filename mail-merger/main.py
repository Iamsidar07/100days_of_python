with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    new_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as file:
        new_letter = starting_letter.replace("[name]", new_name)
        file.write(new_letter)
