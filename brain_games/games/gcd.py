from random import randint
from math import gcd

task = 'Find the greatest common divisor of given numbers.'


def main():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer
