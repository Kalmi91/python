import random


def game():
    num_lose = 0
    num_drow = 0
    num_win = 0
    if user_choice == computer_choice:
        print('Drow')
        num_drow += 1
    elif user_choice == 'r' and computer_choice == 's':
        print('You win!!')
        num_win +=1
    elif user_choice == 'p' and computer_choice == 'r':
        print('You win')
        num_win += 1
    elif user_choice == 's' and computer_choice == 'p':
        print('You win')
        num_win += 1
    elif user_choice == 'e':
        print('The game stoped!!')
        quit()
    else:
        print('You lose')
        num_lose += 1
    print(f'win: {num_win} lose: {num_lose} drow: {num_drow}')




user_choice = ''
while True:
    user_choice = input('What do you pick? Rock (R) Paper (P) Scissors (S) or (E) to exit\n').lower()
    computer_choice = random.choice(['r', 'p', 's'])
    game()



#
# x * 2 = x

# x = input('Tedd ide a számot: ')
# x = int(x)
#
# def plusz_one():
#     print(f'amit megadtál szám az az {x + 1} volt')
#
#
# plusz_one()