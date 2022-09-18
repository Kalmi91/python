import random
from words import szavak
import string

def get_valid_word(x):
    word = random.choice(x)
    while '-' in word or ' ' in word:
        word = random.choice(x)
    return word.upper()

def hangman():
    word = get_valid_word(szavak)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list =  [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word.')
                
        elif user_letter in used_letters:
            print('You used!! Try Again!!')
        else:
            print('Invalid Character. Try Again!!')
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')
        
hangman()

