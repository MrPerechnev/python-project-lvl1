from random import randint

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    question = randint(1, 100)
    correct_answer = even(question)
    return question, correct_answer
