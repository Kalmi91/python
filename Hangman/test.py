x = [1, 2, 3, 4, 5, 4, 5, 6, 7 ]
y = [1, 2, 4, 5, 6]
x = set(x)


def number_chacker():

    user_guess = input('Guess a number: ')
    x = [1, 2, 3, 4, 5, 4, 5, 6, 7]
    if user_guess in x:
        print('fasz')

print(number_chacker())
print(type(x))


