#!/usr/bin/env python3
from random import randint, choice

task = 'What is the result of the expression?'


def main():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operators = ['+', '-', '*']
    random_operator = choice(operators)
    question = f'{number1} {random_operator} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer


if __name__ == '__main__':
    main()