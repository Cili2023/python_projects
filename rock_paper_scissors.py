import random

class RockPaperScissors:

    def is_user_winner(self, player_choice, cpu_choice):
        if cpu_choice == 1 and player_choice == 2:
            print('You win')
            return True
        elif cpu_choice == 1 and player_choice == 3:
            print('You lose')
            return False
        elif cpu_choice == 2 and player_choice == 1:
            print('You lose')
            return False
        elif cpu_choice == 2 and player_choice == 3:
            print('You win')
            return True
        elif cpu_choice == 3 and player_choice == 1:
            print('You win')
            return True
        elif cpu_choice == 3 and player_choice == 2:
            print('You lose')
            return False
        elif cpu_choice == player_choice:
            print('Its draw')

    def start_game(self):

        print('Welcome to the rock, paper, scissors game')

        choices = [1, 2, 3]
        game_on = True
        player_big_games = 0
        cpu_big_games = 0

        while game_on:
            print('If you want to play press any key, if not press N')
            exit_game = input().lower()
            if exit_game == 'n':
                break

            player_wins = 0
            cpu_wins = 0

            while player_wins < 3 and cpu_wins < 3:
                while True:
                    try:
                        print('1. Rock \n2. Paper \n3. Scissors')
                        player_choice = int(input())
                        if 0 < player_choice < 4:
                            break
                    except ValueError:
                        print('Neispravna vrijednost, ponovi!')
                cpu_choice = random.choice(choices)
                result = self.is_user_winner(player_choice, cpu_choice)
                if result:
                    player_wins += 1
                elif result == False:
                    cpu_wins += 1
                print(f'Player: {player_wins}')
                print(f'CPU: {cpu_wins}')
            if player_wins == 3:
                print('You Win')
                player_big_games += 1
            else:
                print('You lose')
                cpu_big_games += 1
            print(f'Player: {player_big_games}')
            print(f'CPU: {cpu_big_games}')




