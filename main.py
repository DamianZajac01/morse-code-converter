from playsound import playsound
import time


def play_morse_code(message):
    for character in message:
        if character == '•':
            playsound('short.mp3')
        elif character == '-':
            playsound('long.mp3')
        elif character == " ":
            time.sleep(.1)
        else:
            print('Invalid symbol!')


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

morse_symbols = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••',
                 '•---', '-•-', '•-••', '--', '-•', '---', '•--•', '--•-',
                 '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••']

user_input = input("Type the message: ").upper()

user_letters = []
letters_to_morse = []

for letter in user_input:
    user_letters.append(letter)
    index = letters.index(letter)
    letters_to_morse.append(morse_symbols[index])

final_message = ''
for symbol in letters_to_morse:
    final_message += symbol + '  '

print(f'Message in the morse code: \n {final_message}')
play_morse_code(final_message)
