#!/usr/bin/env python
import random


def get_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_task():
    return random.randint(0, 100)


def get_answer(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
