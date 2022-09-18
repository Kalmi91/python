import random

def game():
    én = input("What's your chouce? 'r' for rock, 'p' for paper, 's' for sciccors\n")
    bot = random.choice(['r', 'p', 's'])

    if én == bot:
        return 'it\'s a tie'

    if win(én, bot):
        return 'You won!'
    return  'You lost!'

def win(ember, gép):
    if (ember == 'r' and gép == 's') or (ember == 's' and gép == 'p') \
            or (ember == 'p' and  gép == 'r'):
        return True

print(game())