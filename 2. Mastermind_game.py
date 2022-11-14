# Mastermind Game
# From: Python by examples, learning to program in 150 challenges
# Page 161
# Instruction:
"""You are going to make an on-screen version of the board game “Mastermind”. The computer will automatically generate
four colours from a list of possible colours (it should be possible for the computer to randomly select the same colour
more than once). For instance, the computer may choose “red”, “blue”, “red”, “green”. This sequence should not be
displayed to the user. After this is done the user should enter their choice of four colours from the same list the
computer used. For instance, they may choose “pink”, “blue”, “yellow” and “red”. After the user has made their
selection, the program should display how many colours they got right in the correct position and how many colours
they got right but in the wrong position. In the example above, it should display the message “Correct colour in the
correct place: 1” and “Correct colour but in the wrong place: 1”. The user continues guessing until they correctly enter
the four colours in the order they should be in. At the end of the game it should display a suitable message and tell
them how many guesses they took."""
import random
possible_colors = ['Red', 'Blue', 'Green', 'Yellow']
rounds_played = 0
com_res_list = []
user_res_list = []
cacp = 0  # Correct Answer Correct Place
cawp = 0  # Correct Answer Wrong Place


def com_res():
    for i in range(4):
        com_res_list.append(random.choice(possible_colors))
    return com_res_list


def user_res():
    print(f'{"_" * 80}\nChoose 4 colors from below (either enter the name of the color or the number):\n'
          f'1) Red\n'
          f'2) Blue\n'
          f'3) Green\n'
          f'4) Yellow\n'
          f'{"_" * 80}')
    while len(user_res_list) < 4:

        resp = input(f'Round {rounds_played + 1}: Enter your choice here:')
        if resp.isalpha() and resp.title() in possible_colors:
            user_res_list.append(resp.capitalize())
        elif resp.isdigit() and 0 < int(resp) < 5:
            user_res_list.append(possible_colors[int(resp) - 1])
        else:
            print('Please choose from the above options only.')
    else:
        print(('*'*10).center(80))
        return user_res_list


def answer_check():
    global cacp, cawp, rounds_played
    for i in range(4):
        if user_res_list[i] == com_res_list[i]:
            cacp += 1
            print(f'Color "{user_res_list[i]}" is rightly guessed at index {i}')
        elif user_res_list[i] in com_res_list:
            cawp += 1
            print(f'Color "{user_res_list[i]}" is chosen by the computer, but the index is wrong')
        else:
            continue
    else:
        if cacp == 4:
            exit()
        else:
            rounds_played += 1
            cacp = 0
            cawp = 0
            user_res_list.clear()


def master_mind():
    com_res()
    while rounds_played < 3:
        user_res()
        answer_check()
    else:
        return f'{"_" * 80}\n' \
               f'Correct Answer: {com_res_list}'


if __name__ == '__main__':
    print(master_mind())
