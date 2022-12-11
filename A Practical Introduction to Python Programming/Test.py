import random
# switch = False
user_score = {'Should Switch': 0, 'Should not Switch': 0}
N = 10000
for i in range(N):
    # Creating Doors
    monty_doors = list((1, 0, 0))
    random.shuffle(monty_doors)
    # Getting User's Choice
    user_pick = random.randint(1, 3)
    # while True:
    #     try:
    #         user_pick = eval(input('Pick a door number from 1-3: '))
    #         if user_pick in [1, 2, 3]:
    #             break
    #     except (NameError, EOFError):
    #         continue
    # Monty Eliminates a door
    while True:
        monty_pick = random.randint(1, 3)
        if monty_doors[monty_pick - 1] or monty_pick == user_pick:
            continue
        else:
            break
    # Ask if the user wants to change its choice
    switch = random.choice(['yes', 'no'])  # input('Would you like to change your door number?[Yes/No] ')
    if switch.lower() in ('yes', 'y'):
        while True:
            try:
                user_pick2 = random.randint(1, 3)
                # user_pick2 = eval(input('Pick a door number from 1-3: '))
                if user_pick2 == monty_pick:
                    continue
                elif user_pick2 in [1, 2, 3]:
                    break
            except (NameError, EOFError):
                continue
        if not monty_doors[user_pick2-1]:
            user_score['Should not Switch'] += 1
    else:
        if not monty_doors[user_pick-1]:
            user_score['Should Switch'] += 1
else:
    print(f"In %{(user_score['Should Switch']/N)*100:.2f} of occasions you would win if you switched.\n"
          f"In %{(user_score['Should not Switch']/N)*100:.2f} of occasions you would win if you didn't switch.")
