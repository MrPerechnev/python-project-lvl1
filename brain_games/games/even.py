from random import randint

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def main():
    number_min = 1
    number_max = 100
    question = randint(number_min, number_max)
    correct_answer = is_even(question)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
