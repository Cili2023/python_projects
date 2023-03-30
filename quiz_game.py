from numpy.random import shuffle

class PlayersQuiz:

    def __init__(self):
        self.quiz = 'PlayersQuiz'
        self.croatia_players = {
            48: 'Dominik Kuzmanović',
            43: 'Dino Slavić',
            35: 'Mate Šunjić',
            62: 'Marin Jelinić',
            2: 'Lovro Mihić',
            57: 'Filip Glavaš',
            14: 'Paolo Kraljević',
            28: 'Željko Musa',
            53: 'Marin Šipić',
            40: 'Nikola Grahovac',
            52: 'Leon Šušnja',
            5: 'Domagoj Duvnjak',
            33: 'Luka Cindrić',
            18: 'Igor Karačić',
            58: 'Zvonimir Srna',
            17: 'Josip Šarac',
            51: 'Ivan Martinović',
            31: 'Luka Šebetić',
            10: 'Jakov Gojun'
        }
        self.denmark_players = {
            1: 'Niklas Landin',
            3: 'Niclas Kirkelokke',
            4: 'Magnus Landin',
            7: 'Emil Jacobsen',
            11: 'Rasmus Lauge',
            15: 'Magnus Saugstrup',
            18: 'Hans Lindberg',
            19: 'Mathias Gidsel',
            20: 'Kevin Moller',
            21: 'Henrik Mollgard',
            24: 'Mikel Hansen',
            25: 'Lukas Jorgensen',
            26: 'Johan Hansen',
            27: 'Michael Damgaard',
            32: 'Jacob Holm',
            34: 'Simon Hald',
            38: 'Mads Hoxer',
            43: 'Simon Pytlick',
            64: 'Lasse Moller'
        }

        self.france_players = {
            2: 'Yanis Lenne',
            5: 'Nedim Remili',
            7: 'Romain Lagarde',
            8: 'Elohim Prandi',
            9: 'Melvyn Richardson',
            10: 'Dika Mem',
            11: 'Nicolas Tournat',
            12: 'Vincent Gerard',
            13: 'Nikola Karabatić',
            14: 'Kentin Mahe',
            15: 'Mathieu Grebille',
            16: ' Charles Bolzinger',
            22: 'LUka Karabatic',
            23: 'Ludovic Fabregas',
            28: 'Valentin Porte',
            31: 'Dylan Nahi',
            39: 'Thibaud Briet',
            92: 'Remi Desbonnet'
        }

        self.countries = {
            1: 'Croatia',
            2: 'Denmark',
            3: 'France'
        }

    def start_game(self):

        correct_answers = 0
        print('Welcome to the handball quiz!!')
        print('Choose which county team would you like to guess:')
        countries_to_choose = self.countries.items()
        for kvp in countries_to_choose:
            print(f'{kvp[0]} - {kvp[1]}')
        country_choice = int(input())
        if country_choice == 1:
            guess_country = self.croatia_players
        elif country_choice == 2:
            guess_country = self.denmark_players
        elif country_choice == 3:
            guess_country = self.france_players
        else:
            guess_country = {}
        while True:
            try:
                choice = int(input('Choose what would you like to guess:\n1. Jersey number\n2. Players name\n'))
                if choice == 1:
                    guessing_list = [player for player in guess_country.values()]
                    shuffle(guessing_list)
                    for element in guessing_list:
                        try:
                            players_number = int(input(f'Whats the jersey number of player {element}'))
                            if guess_country.keys().__contains__(players_number) and element == guess_country[players_number]:
                                print('Correct!!')
                                correct_answers += 1
                            else:
                                print('Wrong answer...')
                        except ValueError:
                            print('Wrong answer...')
                            print(f'You have {correct_answers} out of {len(guessing_list)}')
                            break
                elif choice == 2:
                    guessing_list = [player for player in guess_country.keys()]
                    shuffle(guessing_list)
                    for element in guessing_list:
                        players_name = input(f"What's the name of jersey number {element}:")
                        if players_name.lower() == guess_country[element].lower():
                            print('Correct!')
                            correct_answers += 1
                        else:
                            print('Nice try! Wrong..')
                            print(f'You did {correct_answers} out of {len(guessing_list)}')
                        break

            except ValueError:
                print('Wrong choice, please try again.')