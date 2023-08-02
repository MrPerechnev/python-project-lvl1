from random import randint

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


def main():
    number_min = 1
    number_max = 100
    question = randint(number_min, number_max)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
