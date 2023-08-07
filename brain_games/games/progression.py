from random import randint

task = 'What number is missing in the progression?'


def line_formation(first_number, step):
    list = []
    for _ in range(10):
        first_number = first_number + step
        list.append(str(first_number))
    return list


def generation(list, missing_number):
    missing_number = randint(0, 9)
    list = str(list[missing_number])
    list[missing_number] = '..'
    question = ' '.join(list)
    return question


def main():
    number_min = 1
    number_max = 100
    first_number = randint(number_min, number_max)
    step = randint(1, 10)
    list = line_formation(first_number, step)
    missing_number = randint(0, 9)
    correct_answer = str(list[missing_number])
    question = generation(list, missing_number)
    return question, correct_answer
