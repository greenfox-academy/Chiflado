from random import *

user_range = int(input('The number will be between 1 and ... '))

magic_number = randint(1, user_range + 1)

print('You have 5 lives! \nGuess a number between 1 and ' + str(user_range) + '! ')
lives = 5

def guess_the_number(magic_number, lives, user_range):
    while lives > 0:
        user_guess = int(input('Please guess a number: '))
        if magic_number == user_guess:
            print('Congratulation! You found the number: ' + str(magic_number))
            return
        elif magic_number < user_guess:
            lives -= 1
            print('The number is lower! You have ' + str(lives) + ' lives left')
            if lives == 0:
                print('Sorry you have no more lifes left, you lost! :(')
                return 
        elif magic_number > user_guess:
            lives -= 1
            print('The number is higher You have ' + str(lives) + ' lives left')
            if lives == 0:
                print('Sorry you have no more lifes left, you lost! :(\n The number was: ' + str(magic_number))
                return



guess_the_number(magic_number, lives, user_range)