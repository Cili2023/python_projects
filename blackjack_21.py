import random

class BlackJack:

    def __init__(self):
        self.blackjack = 'BlackJack'
        self.game_on = True
        self.single_color_card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.player_wins = 0
        self.CPU_wins = 0
        self.player_big_wins = 0
        self.CPU_big_wins = 0

    def create_deck(self):
        new_deck = []
        for i in range(4):
            for card in self.single_color_card_deck:
                new_deck.append(card)
        return new_deck

    def deal_card(self, deck, turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

    def total(self, turn):
        total = 0
        face = ['J', 'K', 'Q']
        for card in turn:
            if card in range(1, 11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total

    def reveal_dealer_hand(self, dealer_hand):
        if len(dealer_hand) == 2:
            return dealer_hand[0]
        return dealer_hand

    def clear_wins(self):
        return [0, 0]

    def start_game(self):
        print('Welcome to the Blackjack game have fun!!')
        while self.game_on:
            deck = self.create_deck()
            player_hand = []
            dealer_hand = []
            player_in = True
            dealer_in = True
            for _ in range(2):
                self.deal_card(deck, dealer_hand)
                self.deal_card(deck, player_hand)

            while player_in or dealer_in:
                print(f'Dealer had {self.reveal_dealer_hand(dealer_hand)} and X')
                print(f'You have {player_hand} for a total of {self.total(player_hand)}')
                if player_in:
                    stay_or_hit = input('1: Stay\n2: Hit\n')
                if self.total(dealer_hand) > 20 or self.total(dealer_hand) > self.total(player_hand):
                    dealer_in = False
                else:
                    self.deal_card(deck, dealer_hand)
                if stay_or_hit == '1':
                    player_in = False
                else:
                    self.deal_card(deck, player_hand)
                if self.total(player_hand) >= 21:
                    break
                elif self.total(dealer_hand) >=21:
                    break

            print(f'\nYou have {player_hand} for a total of {self.total(player_hand)} and the dealer has {dealer_hand} for a total of {self.total(dealer_hand)}')

            if self.total(player_hand) == 21:
                print('BLACKJACK!!! You win')
                self.player_wins += 1
            elif self.total(dealer_hand) == 21:
                print('BLACKJACK!!! Dealer wins')
                self.CPU_wins += 1
            elif self.total(player_hand) > 21:
                print('You bust, Dealer wins')
                self.CPU_wins += 1
            elif self.total(dealer_hand) > 21:
                print('Dealer bust, You win')
                self.player_wins += 1
            elif self.total(dealer_hand) > self.total(player_hand):
                print('Dealer wins')
                self.CPU_wins += 1
            else:
                print('You win')
                self.player_wins += 1

            print(f'Player wins = {self.player_wins}, CPU wins = {self.CPU_wins}')

            if self.player_wins == 3:
                print('You win a big game!!')
                self.player_big_wins += 1
            elif self.CPU_wins == 3:
                print('CPU win big game!!')
                self.CPU_big_wins += 1
            if (self.player_big_wins > 0 or self.CPU_big_wins > 0) and (self.player_wins == 3 or self.CPU_wins == 3):
                print(f'Player big wins = {self.player_big_wins}\nCPU big wins = {self.CPU_big_wins}')
                self.player_wins, self.CPU_wins = self.clear_wins()
                print('If u want to play again press any key, if not press n or N')
                exit_game = input().lower()
                if exit_game == 'n':
                    break
