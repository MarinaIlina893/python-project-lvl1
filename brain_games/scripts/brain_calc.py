from brain_games.games import calc


def main():
    brain_calc()


if __name__ == '__main__':
    main()


def welcome_user():
    print('Welcome to the Brain Games!!')
    user_name = input('May I have your name?')
    print('Hello, {0}!'.format(user_name))
    return user_name


def brain_calc():
    user_name = welcome_user()
    print(calc.get_description())
    game_counter = 0
    while game_counter < 3:
        attempt = game_attempt()
        if not attempt:
            print("Let\'s try again, {0}!".format(user_name))
            break
        if game_counter == 2:
            print('Congratulations, {0}!'.format(user_name))
        game_counter += 1


def game_attempt():
    task = calc.generate_task()
    print('Question: {0}'.format(task))
    is_success = False
    user_answer = input('Your answer: ')
    correct_answer = calc.get_answer(task)
    if correct_answer == user_answer:
        print('Correct!')
        is_success = True
    else:
        print("\'{0}\' is wrong answer ;(. Correct answer was \'{1}\'".format(user_answer, correct_answer))
        is_success = False
    return is_success
