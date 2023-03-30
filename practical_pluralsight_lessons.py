#DICTIONARIES-movio_schedule

#currnet_movies = {'Green Mile' : '15:00h',
#                 'Hacksaw Ridge' : '18:00h',
#                  'Armagedon' : '21:00',
#                  'Home Alone' : '23:00'}
#print('We are showing the following movies:')
#for key in currnet_movies:
#    print(key)
#movie = input('What movie would you like the showtime for?\n')
#showtime = currnet_movies.get(movie)
#if showtime == None:
#    print('Requested showtime isnt playing')
#else:
#    print(movie, 'is playing at', showtime)
#---------------------------------------------------------------------
#contacts = {
#    'number':4,
#    'students':
#    [
#        {'name':'Luka Smaic', 'email':'luka.smaic@gmail.com'},
#        {'name':'Fran Cili', 'email':'fran.cili@gmail.com'},
#        {'name':'Noa Koljenik', 'email':'noa.koljenik@gmail.com'},
#    ]
#}
#for student in contacts['students']:
#    print(student['email'])

import random

game_on = True

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)#randint-funkcija za dobivanje nasumičnog cijelog broja, u zagradama smo odredili range.
    return dice_total
while game_on:

    player1 = input('Enter first player name: ')
    player2 = input('Enter second player name: ')

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1, 'pts')
    print(player2, 'rolled', roll2, 'pts')

    if roll1 > roll2:
        print(player1, 'won!!')
    elif roll2 > roll1:
        print(player2, 'won!!')
    else:
        print('Its draw!')
    print('If you want to play again press any key but if u want to quit press q')
    quit = input().lower()
    if quit == 'q':
        break