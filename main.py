"""
Random number Generator
----------------------------------------------------------------
"""

import random

attempts_list = []


def show_score():
    if not attempts_list:
        print('There is currently no high score, it\'s yours for the taking!')
    else:
        print(f'The current high score is {min(attempts_list)} attempts')


def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play the guessing game?'
        '(Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('That\'s cool, Thanks!')
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number within the given range')

            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print('Nice! You got it!')
                print(f'It took you {attempts} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('That\'s cool, have a good one!')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)


#if __name__ == '__main__':
#    start_game()

'''
Rock Paper Scissors
-------------------------------------------------------------
'''

import os
import re


def check_play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)


def play_rps():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Rock, Paper, Scissors - Shoot!')

        user_choice = input('Choose your weapon'
                            ' [R]ock], [P]aper, or [S]cissors: ')

        if not re.match("[SsRrPp]", user_choice):
            print('Please choose a letter:')
            print('[R]ock, [P]aper, or [S]cissors')
            continue

        print(f'You chose: {user_choice}')

        choices = ['R', 'P', 'S']
        opp_choice = random.choice(choices)

        print(f'I chose: {opp_choice}')

        if opp_choice == user_choice.upper():
            print('Tie!')
            play = check_play_status()
        elif opp_choice == 'R' and user_choice.upper() == 'S':
            print('Rock beats scissors, I win!')
            play = check_play_status()
        elif opp_choice == 'S' and user_choice.upper() == 'P':
            print('Scissors beats paper! I win!')
            play = check_play_status()
        elif opp_choice == 'P' and user_choice.upper() == 'R':
            print('Paper beats rock, I win!')
            play = check_play_status()
        else:
            print('You win!\n')
            play = check_play_status()


if __name__ == '__main__':
    play_rps()
