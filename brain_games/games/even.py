from random import randint

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    number_min = 1
    number_max = 100
    question = randint(number_min, number_max)
    correct_answer = even(question)
    return question, correct_answer
