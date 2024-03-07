morse_code_data = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '\\': '-...-',
}

print('''
 _   .-')                _  .-')    .-')      ('-.   
( '.( OO )_             ( \( -O )  ( OO ).  _(  OO)  
 ,--.   ,--.).-'),-----. ,------. (_)---\_)(,------. 
 |   `.'   |( OO'  .-.  '|   /`. '/    _ |  |  .---' 
 |         |/   |  | |  ||  /  | |\  :` `.  |  |     
 |  |'.'|  |\_) |  |\|  ||  |_.' | '..`''.)(|  '--.  
 |  |   |  |  \ |  | |  ||  .  '.'.-._)   \ |  .--'  
 |  |   |  |   `'  '-'  '|  |\  \ \       / |  `---. 
 `--'   `--'     `-----' `--' '--' `-----'  `------' 
''')


def generate_morse_code(text):
    morse_code = ''
    for c in text:
        morse_code += morse_code_data[c]
    print(morse_code)


def main():
    should_continue = True
    while should_continue:
        sentence = input('Enter your text? type exit to continue: ').upper().strip()
        if sentence == 'EXIT':
            should_continue = False
        else:
            generate_morse_code(sentence)


if __name__ == '__main__':
    main()
