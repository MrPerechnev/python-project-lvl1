from random import randint
from math import gcd

task = 'Find the greatest common divisor of given numbers.'


def main():
    number_min = 1
    number_max = 100
    number1 = randint(number_min, number_max)
    number2 = randint(number_min, number_max)
    question = f'{number1} {number2}'
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer
