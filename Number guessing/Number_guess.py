import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('o-o the number is too low')
        else:
            print('o-o the number is too high')
    print(f'fasza vagy!! You Got the number {random_number}')

guess(10)