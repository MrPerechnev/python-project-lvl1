from random import randint
from math import gcd
NUMBER_MIN = 1
NUMBER_MAX = 100

TASK = 'Find the greatest common divisor of given numbers.'


def generate():
    number1 = randint(NUMBER_MIN, NUMBER_MAX)
    number2 = randint(NUMBER_MIN, NUMBER_MAX)
    question = f'{number1} {number2}'
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer
