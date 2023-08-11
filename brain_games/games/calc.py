from random import randint, choice

task = 'What is the result of the expression?'


def task_generation():
    number_min = 1
    number_max = 100
    number1 = randint(number_min, number_max)
    number2 = randint(number_min, number_max)
    operators = ['+', '-', '*']
    random_operator = choice(operators)
    question = f'{number1} {random_operator} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer
