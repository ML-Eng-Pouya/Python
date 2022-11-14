# Shift Code Challenge
# From: Python by examples, learning to program in 150 challenges.pdf
# Page 158
# Instruction:
"""
A shift code is where a message can be easily encoded and is one of the simplest codes to use. Each letter is moved
forwards through the alphabet a set number of letters to be represented by a new letter. For instance, “abc” becomes
“bcd” when the code is shifted by one (i.e. each letter in the alphabet is moved forward one character). You need to
create a program which will display the following menu: If the user selects 1, they should be able to type in a message
(including spaces) and then enter a number. Python should then display the encoded message once the shift code has been
applied. If the user selects 2, they should enter an encoded message and the correct number, and it should display the
decoded message (i.e. move the correct number of letters backwards through the alphabet). If they select 3 it should
stop the program from running. After they have encoded or decoded a message the menu should be displayed to them again
until they select quit.
"""
alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def user_choice():
    while True:
        user_input = input('Enter your selection: ')
        if user_input.isdigit() and int(user_input) <= 3:
            return int(user_input)
        else:
            print('Wrong Input')
            continue


def encode():
    user_resp = input(f'{"*"*40}\nWhat\'s your message? ')
    while True:
        step = int(input('Enter a number (1-26): '))
        if 0 < step < 27:
            break
        else:
            print('Out of Range, Please try again')
    encoded_msg = ''
    for char in user_resp.upper():
        if char in ',;\'. "!@#$%^&*()-0123456789':
            encoded_msg += char
        elif (len(alphabet_string) - alphabet_string.index(char) - 1) < step:
            encoded_msg += alphabet_string[step - (len(alphabet_string) - alphabet_string.index(char))]
        else:
            encoded_msg += alphabet_string[alphabet_string.index(char) + step]
    else:
        return encoded_msg


def decode():
    user_resp = input(f'{"*"*40}\nWhat\'s your message? ')
    while True:
        step = int(input('Enter a number (1-26): '))
        if 0 < step < 27:
            break
        else:
            print('Out of Range, Please try again')
    decoded_msg = ''
    for char in user_resp.upper():
        if char in ',;\'. "!@#$%^&*()-0123456789':
            decoded_msg += char
        elif len(alphabet_string[:alphabet_string.index(char)]) < step:
            decoded_msg += alphabet_string[-(step - len(alphabet_string[:alphabet_string.index(char)]))]
        else:
            decoded_msg += alphabet_string[alphabet_string.index(char) - step]
    else:
        return decoded_msg


def shift_code():
    print('1) Make a code\n2) Decode a message\n3) Quit')
    ans = user_choice()
    if ans == 1:
        return encode()
    elif ans == 2:
        return decode()
    else:
        exit()


if __name__ == '__main__':
    print(shift_code())
