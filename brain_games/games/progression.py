from random import randint

task = 'What number is missing in the progression?'


def get_progression(first_number, length, step):
    list = []
    for _ in range(length):
        first_number = first_number + step
        list.append(str(first_number))
    return list


def task_generation():
    number_min = 1
    number_max = 100
    step_min = 1
    step_max = 10
    length = 10
    step = randint(step_min, step_max)
    first_number = randint(number_min, number_max)
    number_start = 0
    number_end = 10
    list = get_progression(first_number, length, step)
    missing_number = randint(number_start, number_end - 1)
    correct_answer = str(list[missing_number])
    list[missing_number] = '..'
    question = ' '.join(list)
    return question, correct_answer
