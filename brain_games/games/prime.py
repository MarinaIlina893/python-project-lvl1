import random


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_task():
    return random.randint(1, 100)


def get_answer(task):
    if is_prime(task):
        return 'yes'
    return 'no'


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    divider = 3
    while divider ^ 2 <= number and number % divider != 0:
        divider += 2
    return number == divider
