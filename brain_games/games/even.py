from random import randint
NUMBER_MIN = 1
NUMBER_MAX = 100

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate():
    question = randint(NUMBER_MIN, NUMBER_MAX)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
