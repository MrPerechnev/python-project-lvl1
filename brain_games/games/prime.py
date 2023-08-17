from random import randint
NUMBER_MIN = 1
NUMBER_MAX = 100

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


def generate():
    question = randint(NUMBER_MIN, NUMBER_MAX)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
