from random import randint, choice
NUMBER_MIN = 1
NUMBER_MAX = 100

TASK = 'What is the result of the expression?'


def generate():
    number1 = randint(NUMBER_MIN, NUMBER_MAX)
    number2 = randint(NUMBER_MIN, NUMBER_MAX)
    operators = ['+', '-', '*']
    random_operator = choice(operators)
    question = f'{number1} {random_operator} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer
