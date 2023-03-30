from blackjack_21 import BlackJack
from quiz_game import PlayersQuiz
from rock_paper_scissors import RockPaperScissors


def main():
    games_on = True
    while games_on:
        try:
            print('Welcome to the Frans games please insert your choice.')
            choice = int(input('1: Rock, paper, scissors\n2: Blackjack\n3: Players quiz game\n4: Exit game\n'))
            if choice == 1:
                game = RockPaperScissors()
                game.start_game()
            elif choice == 2:
                game = BlackJack()
                game.start_game()
            elif choice == 3:
                game = PlayersQuiz()
                game.start_game()
            elif choice == 4:
                break
            else:
                print('Neispravan unos pokušajte ponovo.')
        except ValueError:
            print('Neispravan unos pokušajte ponovo.')


if __name__ == '__main__':
    main()
