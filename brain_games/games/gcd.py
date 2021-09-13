import random


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def generate_task():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    return '{0} {1}'.format(num1, num2)


def get_answer(task):
    task_split = task.split(' ')
    num1 = int(task_split[0])
    num2 = int(task_split[1])
    return str(get_gcd(num1, num2))


def get_gcd(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 > num2:
        return get_gcd(num1 % num2, num2)
    return get_gcd(num2 % num1, num1)
