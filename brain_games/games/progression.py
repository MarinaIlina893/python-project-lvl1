from array import *
import random


def get_description():
    return 'What number is missing in the progression?'


def generate_task():
    progression = array('i', )
    progression.append(random.randint(0, 100))
    ratio = random.randint(1, 10)
    progression_size = random.randint(5, 10)
    hidden_position = random.randint(0, progression_size - 1)
    i = 1
    while i < progression_size:
        progression.append(progression[i-1]+ratio)
        i += 1
    task = ''
    for x in progression:
        if progression.index(x) != hidden_position:
            task = task + str(x) + ' '
        else:
            task += '.. '
    return task.rstrip()


def get_answer(task):
    progression = task.split(' ')
    hidden_position = progression.index('..')
    ratio = calculate_ratio(progression, hidden_position)
    if hidden_position != 0:
        return str(int(progression[hidden_position-1]) + ratio)
    else:
        return str(int(progression[1])-ratio)


def calculate_ratio(progression, hidden_position):
    if hidden_position > 1:
        return int(progression[1])-int(progression[0])
    elif hidden_position == 1:
        return int(progression[3])-int(progression[2])
    return int(progression[2]) - int(progression[1])
