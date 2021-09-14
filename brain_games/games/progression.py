import array
import random


def get_description():
    return 'What number is missing in the progression?'


def generate_task():
    progression = generate_progression()
    hidden_position = random.randint(0, len(progression) - 1)
    task = ''
    for element in progression:
        if progression.index(element) == hidden_position:
            task = '{0}.. '.format(task)
        else:
            task = '{0}{1} '.format(task, str(element))
    return task.rstrip()


def get_answer(task):
    progression = task.split(' ')
    hidden_position = progression.index('..')
    ratio = calculate_ratio(progression, hidden_position)
    if hidden_position == 0:
        return str(int(progression[1]) - ratio)
    return str(int(progression[hidden_position - 1]) + ratio)


def calculate_ratio(progression, hidden_position):
    if hidden_position > 1:
        return int(progression[1]) - int(progression[0])
    elif hidden_position == 1:
        return int(progression[3]) - int(progression[2])
    return int(progression[2]) - int(progression[1])


def generate_progression():
    progression = array.array('i')
    progression.append(random.randint(0, 100))
    ratio = random.randint(1, 10)
    progression_size = random.randint(5, 10)
    index = 1
    while index < progression_size:
        progression.append(progression[index - 1] + ratio)
        index += 1
    return progression
