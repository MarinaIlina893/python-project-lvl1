import random


def get_description():
    return 'What is the result of the expression?'


def generate_task():
    operators = ['+', '-', '*']
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(operators)
    return '{0} {1} {2}'.format(num1, operator, num2)


def get_answer(task):
    task_split = task.split(' ')
    num1 = int(task_split[0])
    operator = task_split[1]
    num2 = int(task_split[2])
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    return str(num1 * num2)
