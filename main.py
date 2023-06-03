import random


class blackjack():

    def __init__(self, player, pot):
        self.player = player
        self.pot = pot


    def Raise(pot):
        pot= pot + random.randrange(1,13)
        return pot

    def stay(pot):
        pot=pot
        return pot

player1=blackjack.Raise(0)
player2=blackjack.Raise(0)
player3=blackjack.Raise(0)

print("player 1 raise or stay? y or n")
i=input()
if i=='Y':
    player1=blackjack.Raise(player1)
    print('player 1 =',player1)
if i=='N':
    player1=blackjack.stay(player1)


print("player 2 raise or stay? y or n")
i=input()
if i=='Y':
    player2=blackjack.Raise(player2)
    print('player 2 =',player2)
if i=='N':
    player2=blackjack.stay(player2)


print("player 3 raise or stay? y or n")
i=input()
if i=='Y':
    player3=blackjack.Raise(player3)
    print('player 3 =',player3)
if i=='N':
    player3=blackjack.stay(player3)

print('second dealing \n')

print("player 1 raise or stay? y or n")
i = input()
if i == 'Y':
    player1 = blackjack.Raise(player1)
    print('player 1 =', player1)
if i == 'N':
    player1 = blackjack.stay(player1)

print("player 2 raise or stay? y or n")
i = input()
if i == 'Y':
    player2 = blackjack.Raise(player2)
    print('player 2 =', player2)
if i == 'N':
    player2 = blackjack.stay(player2)


print("player 3 raise or stay? y or n")
i = input()
if i == 'Y':
    player3 = blackjack.Raise(player3)
    print('player 3 =', player3)
if i == 'N':
    player3 = blackjack.stay(player3)

print('third dealing \n')

print("player 1 raise or stay? y or n")
i = input()
if i == 'Y':
    player1 = blackjack.Raise(player1)
    print('player 1 =', player1)
if i == 'N':
    player1 = blackjack.stay(player1)

print("player 2 raise or stay? y or n")
i = input()
if i == 'Y':
    player2 = blackjack.Raise(player2)
    print('player 2 =', player2)
if i == 'N':
    player2 = blackjack.stay(player2)


print("player 3 raise or stay? y or n")
i = input()
if i == 'Y':
    player3 = blackjack.Raise(player3)
    print('player 3 =', player3)
if i == 'N':
    player3 = blackjack.stay(player3)


print('\n \nplayer 1 =', player1)
print('player 2 =', player2)
print('player 3 =', player3)

