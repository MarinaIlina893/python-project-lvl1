#!/usr/bin/env python

import random


def main():
    brain_even()


if __name__ == '__main__':
    main()


def welcome_user():
    print('Welcome to the Brain Games!!')
    user_name = input('May I have your name?')
    print('Hello, {0}!'.format(user_name))
    return user_name


def brain_even():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_counter = 0
    while game_counter < 3:
        attempt = game_attempt()
        if not attempt:
            print("Let\'s try again, {0}!".format(user_name))
            break
        if game_counter == 2:
            print('Congratulations, {0}'.format(user_name))
        game_counter += 1


def generate_number():
    return random.randint(0, 100)


def get_answer(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def valid_answer(answer):
    return answer in ('yes', 'no')


def game_attempt():
    question = generate_number()
    is_success = False
    print('Question: ', question)
    user_answer = input('Your answer: ')
    correct_answer = get_answer(question)
    if valid_answer(user_answer):
        if correct_answer == user_answer:
            print('Correct!')
            is_success = True
        else:
            print("\'{0}\' is wrong answer ;(. Correct answer was \'{1}\'".format(user_answer, correct_answer))
            is_success = False
    print('{0} is not valid answer'.format(user_answer))
    return is_success
