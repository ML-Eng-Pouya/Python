# Passwords
# From: Python by examples, learning to program in 150 challenges
# Page 164

user_dict = dict()
pass_score = 0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_username():
    again = True
    while again:
        user_id = input('Please enter your desired User-ID: ')
        if user_id.isdigit():
            print('User ID can not be all numeric.')
        elif user_id in user_dict:
            print('User ID already taken.')
        else:
            print('\nGreat. Now Choose your password.')
            user_dict[user_id] = get_pass(user_id)
            again = False


def get_pass(user_id):
    global pass_score
    print('It should:\n'
          '\t1) have at least 8 characters\n'
          '\t2) include uppercase letters\n'
          '\t3) include lower case letters\n'
          '\t4) include numbers\n'
          '\t5) include at least one special character such as !, £, $, %, &, <, * or @\n')
    again = True
    while again:
        user_pass = input('Please enter your password: ')
        if len(user_pass) >= 8:  # Checking Rule 1
            pass_score += 1
        for char in user_pass:  # Checking Rule 2
            if char in alphabet.upper():
                pass_score += 1
                break
        for char in user_pass:  # Checking Rule 3
            if char in alphabet.lower():
                pass_score += 1
                break
        for char in user_pass:  # Checking Rule 4
            if char in '0123456789':
                pass_score += 1
                break
        for char in user_pass:  # Checking Rule 5
            if char in '!£$%&<*@':
                pass_score += 1
                break
        if pass_score < 3:
            print('It is a weak Password')
        elif pass_score < 5:
            rpt = input('This password could be improved. Would you like to try again? [Yes/No] ')
            if rpt.lower() != 'yes' and rpt.lower()[0] != 'y':
                user_dict[user_id] = user_pass
                return user_pass
        else:
            print('You have selected a strong password.')
            user_dict[user_id]=user_pass
            again = False


def passwords():
    print('Please Choose a number from below to proceed:\n'
          '\t1) Create a User ID\n'
          '\t2) Change a Password\n'
          '\t3) Display all User IDs\n'
          '\t4) Quit\n')
    while True:
        print('*'*80)
        user_choice = int(input('Enter Selection:'))
        if user_choice == 1:
            get_username()
        elif user_choice == 2:
            get_pass(input('Please enter your User ID first: '))
        elif user_choice == 3:
            print(user_dict.keys())
        elif user_choice == 4:
            exit()
        else:
            print('Please Enter a valid option only:')


if __name__ == '__main__':
    passwords()
