import random

print('Welcome to the rock, paper, scissors game!!')
choices = [1, 2, 3]
big_cpu_wins = 0
big_player_wins = 0
while True:
    print('Do you want to play: \nN for no \nelse enter any key')
    stop = input()
    if stop == 'N' or stop == 'n':
        break
    cpu_wins = 0
    player_wins = 0
    we_have_a_winner = False
    while not we_have_a_winner:
        player_choice_input = ''
        while not player_choice_input.isnumeric():
            print('Enter your choice: \n1. Rock \n2. Paper \n3. Scissors')
            player_choice_input = input()
        player_choice = int(player_choice_input)
        cpu_choice = random.choice(choices)
        print(cpu_choice)
        if cpu_choice == 1 and player_choice == 3:
            print('You lose')
            cpu_wins += 1
        elif cpu_choice == 1 and player_choice == 2:
            print('You win')
            player_wins += 1
        elif cpu_choice == 2 and player_choice == 3:
            print('You win')
            player_wins += 1
        elif cpu_choice == 2 and player_choice == 1:
            print('You lose')
            cpu_wins += 1
        elif cpu_choice == 3 and player_choice == 2:
            print('You lose')
            cpu_wins += 1
        elif cpu_choice == 3 and player_choice == 1:
            print('You win')
            player_wins += 1
        elif cpu_choice == player_choice:
            print('Its draw')
        print(f'CPU: {cpu_wins}\nPlayer: {player_wins}')
        if cpu_wins == 3 or player_wins == 3:
            we_have_a_winner = True
    if cpu_wins == 3:
        print('YOU LOSE!')
        big_cpu_wins += 1
    else:
        print('YOU WON!')
        big_player_wins += 1
    print(f'CPU: {big_cpu_wins}\nPlayer: {big_player_wins}')

