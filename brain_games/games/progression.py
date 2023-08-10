from random import randint

task = 'What number is missing in the progression?'


def main():
    number_min = 1
    number_max = 100
    step = randint(1, 10)
    list = []
    first_number = randint(number_min, number_max)
    for _ in range(10):
        first_number = first_number + step
        list.append(str(first_number))
    missing_number = randint(0, 9)
    correct_answer = str(list[missing_number])
    list[missing_number] = '..'
    question = ' '.join(list)
    return question, correct_answer
