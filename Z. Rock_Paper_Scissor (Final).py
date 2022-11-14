from random import randint
valid_answers = {'Rock': 0, 'Paper': 1, 'Scissor': 2}
result_matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]  # result_matrix[user_choice][computer_choice]/
# 1:user wins, -1:comp wins, 0:tie
print_resp = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
user_res_dic = {'R': 'Rock', 'S': 'Scissor', 'P': 'Paper', 'Paper': 'Paper', 'Rock': 'Rock', 'Scissor': 'Scissor'}
user_score = 0
computer_score = 0
rounds_played = 0
rep = False


def number_of_rounds():  # Checks the number of rounds user wants to play
    while True:
        round_input = input('How many rounds would you like to play?')
        if round_input.isdigit():
            print('*' * 70)
            print(f'Let\'s have fun for {round_input} rounds!' if int(round_input) > 1 else
                  f'Let\'s have fun for {round_input} round!')
            print('You can exit the game at any time by pressing [Q/Quit]!')
            print('-' * 70)
            return int(round_input)
        else:
            print('Number of rounds must be an integer only. Please try again!')


def exit_condition(user_response):  # checks whether the user wants to quit
    if user_response.lower() == 'q' or user_response.lower() == 'quit':
        print('We hope to see you soon!')
        print(f'{"*" * 70}\n{"Final Results".center(70)}\nUser Score: {user_score}\nComputer Score: {computer_score}')
        if computer_score > user_score:
            print('Computer Wins. Better luck next time!')
        elif computer_score < user_score:
            print('Congratulations. You Win!')
        else:
            print('Looks like someone\'s as good as me!')
        print('*' * 70)
        exit()
    else:
        return user_response


def answer_check():  # checks whether user's response is valid
    while True:
        user_choice = input(f'Round {rounds_played + 1}: What\'s your choice?')
        for string in user_choice.title().split(' '):
            if string in user_res_dic:
                return valid_answers[user_res_dic[string]]
            else:
                continue
        else:
            exit_condition(user_choice)
            print('Please choose a valid option only to proceed!')


def score_calc(ans1, ans2):  # Evaluates scores
    global rounds_played, user_score, computer_score
    final_results = result_matrix[ans1][ans2]
    rounds_played += 1
    if final_results == 0:
        print('It\'s a tie! Let\'s try again!'.center(70, '_'))
    elif final_results == 1:
        user_score += 1
        print('Damn! You Won!'.center(70, '_'))
    else:
        computer_score += 1
        print('Ha Ha! I beat you!'.center(70, '_'))
    return f'Round {rounds_played}: My choice was "{print_resp[ans2]}", ' \
           f'Your choice was "{print_resp[ans1]}"\nUser Score: {user_score}\n' \
           f'Computer Score: {computer_score}\n{"="*70}'


def round_check(num_of_rounds):  # Checks whether rounds' limit is reached
    if user_score + computer_score == num_of_rounds:
        print(f'{"*" * 70}\n{"Final Results".center(70)}\nUser Score: {user_score}\nComputer Score: {computer_score}')
        if computer_score > user_score:
            print('Computer Wins. Better luck next time!')
        elif computer_score < user_score:
            print('Congratulations. You Win!')
        else:
            print('Looks like someone\'s as good as me!')
        print('*' * 70)
        return False
    else:
        return True


def repeat():  # Asks the user to see whether they want to play again
    while True:
        rpt = input('Would you like to play again? [Yes/No]')
        if rpt.upper() == 'YES' or rpt.upper() == 'Y':
            res()
            rps()
        elif rpt.upper() == 'NO' or rpt.upper() == 'N':
            print('Playing with you was fun :)')
            return False
        else:
            print("Please answer with [Yes/No] only!")


def res():  # If user wants to play the game, resets the scores
    global user_score, computer_score, rounds_played, rep
    user_score = 0
    computer_score = 0
    rounds_played = 0
    rep = True
    return user_score, computer_score, rounds_played, rep


def rps():  # All together - Rock-Paper-Scissor
    if not rep:
        print(f'{"*"*70}\n{"Welcome to my Game".center(70)}\nWe are going to play the old school Rock-Paper-Scissor '
              f'game!\nRules are easy:\n\t1)Rock smashes Scissor\n\t2)Paper covers Rock\n\t3)Scissor cuts Paper'
              f'\nCan you beat me? :D\n{"*"*70}')
    rounds_2_play = number_of_rounds()
    while round_check(rounds_2_play):
        user_ans = answer_check()
        print(score_calc(user_ans, randint(0, 2)))
    else:
        repeat()


if __name__ == '__main__':
    rps()
